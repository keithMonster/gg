# 前端网站开发技能

## 描述
专门用于前端网站开发的综合技能，包括HTML、CSS、JavaScript以及现代前端框架的使用。

## 核心能力
- HTML5语义化标记
- CSS3样式设计和布局
- JavaScript交互编程
- 响应式设计和移动端适配
- 前端框架使用(React, Vue, Angular)
- 前端工程化和构建工具
- 性能优化和SEO
- 用户体验设计

## 适用场景
- 企业官网开发
- 电商网站前端
- 管理后台界面
- 移动端H5页面
- 单页应用(SPA)
- 渐进式Web应用(PWA)

## 技术栈
- HTML5/CSS3/JavaScript(ES6+)
- React/Vue.js/Angular
- TypeScript
- Sass/Less/Styled-components
- Webpack/Vite/Parcel
- Babel/PostCSS
- ESLint/Prettier

## 示例代码
```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>用户数据展示页面</title>
    <style>
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }
        
        .user-card {
            background: #fff;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            padding: 20px;
            margin-bottom: 20px;
            transition: transform 0.2s;
        }
        
        .user-card:hover {
            transform: translateY(-2px);
        }
        
        .user-avatar {
            width: 60px;
            height: 60px;
            border-radius: 50%;
            object-fit: cover;
        }
        
        .user-info {
            display: flex;
            align-items: center;
            gap: 15px;
        }
        
        .loading {
            text-align: center;
            padding: 40px;
            color: #666;
        }
        
        @media (max-width: 768px) {
            .container {
                padding: 10px;
            }
            
            .user-info {
                flex-direction: column;
                text-align: center;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>用户数据展示</h1>
        <div id="userList">
            <div class="loading">加载中...</div>
        </div>
    </div>

    <script>
        class UserDataDisplay {
            constructor(containerId) {
                this.container = document.getElementById(containerId);
                this.users = [];
            }
            
            async fetchUsers() {
                try {
                    // 模拟API调用
                    const response = await fetch('/api/users');
                    this.users = await response.json();
                    this.render();
                } catch (error) {
                    this.renderError('加载用户数据失败');
                }
            }
            
            render() {
                if (this.users.length === 0) {
                    this.container.innerHTML = '<div class="loading">暂无用户数据</div>';
                    return;
                }
                
                const userCards = this.users.map(user => `
                    <div class="user-card">
                        <div class="user-info">
                            <img src="${user.avatar || '/default-avatar.png'}" 
                                 alt="${user.name}" class="user-avatar">
                            <div>
                                <h3>${user.name}</h3>
                                <p>邮箱: ${user.email}</p>
                                <p>角色: ${user.role}</p>
                                <p>注册时间: ${new Date(user.createdAt).toLocaleDateString()}</p>
                            </div>
                        </div>
                    </div>
                `).join('');
                
                this.container.innerHTML = userCards;
            }
            
            renderError(message) {
                this.container.innerHTML = `<div class="loading" style="color: #e74c3c;">${message}</div>`;
            }
        }
        
        // 初始化
        document.addEventListener('DOMContentLoaded', () => {
            const userDisplay = new UserDataDisplay('userList');
            userDisplay.fetchUsers();
        });
    </script>
</body>
</html>
```

## 最佳实践
1. 语义化HTML结构
2. 移动优先的响应式设计
3. 性能优化和懒加载
4. 无障碍访问支持
5. SEO友好的页面结构
6. 模块化和组件化开发
7. 代码规范和团队协作