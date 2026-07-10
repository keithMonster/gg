#!/usr/bin/env node
/**
 * data.js 图完整性校验：悬空引用 / 反向边 / 重复 id / 缺字段 / 占位残留
 * 用法：node validate.js   （exit code = 违规数）
 */
global.window = {};
require('./data.js');
const D = window.KM_DATA;
const ids = new Set(D.nodes.map(n => n.id));
let errs = [], edges = 0, papers = 0;

const dup = D.nodes.map(n => n.id).filter((v, i, a) => a.indexOf(v) !== i);
if (dup.length) errs.push('重复 id: ' + dup);

for (const n of D.nodes) {
  for (const t of (n.basedOn || [])) {
    edges++;
    if (!ids.has(t)) { errs.push(`${n.id} -> 悬空引用 ${t}`); continue; }
    const tn = D.nodes.find(x => x.id === t);
    if (tn.layer < n.layer) errs.push(`${n.id}(L${n.layer}) -> ${t}(L${tn.layer}) 方向反了（basedOn 只准指向同层或更深层）`);
  }
  papers += (n.papers || []).length;
  if (!n.title || !n.summary || !n.body) errs.push(n.id + ' 缺字段');
  if (n.body && n.body.includes('待考证')) errs.push(n.id + ' body 残留占位');
  for (const p of (n.papers || [])) {
    if (!p.url) errs.push(`${n.id} 论文缺链接: ${p.title}`);
    if ((p.takeaway || '').includes('占位')) errs.push(`${n.id} 论文残留占位: ${p.title}`);
  }
}

const byLayer = [0, 1, 2, 3, 4].map(l => D.nodes.filter(n => n.layer === l).length);
console.log(`节点: ${D.nodes.length}（${byLayer.join('/')}）| 边: ${edges} | 论文: ${papers}`);
console.log(errs.length ? '❌\n' + errs.join('\n') : '✅ 校验通过');
process.exit(errs.length);
