# React组件开发技能

## 描述
专门用于创建和开发React组件的技能，包括函数组件、类组件、Hooks使用等。

## 核心能力
- 创建React函数组件和类组件
- 使用React Hooks (useState, useEffect, useContext等)
- 组件生命周期管理
- Props和State管理
- 事件处理和用户交互
- 组件样式和CSS-in-JS
- 组件测试和调试

## 适用场景
- 创建用户界面组件
- 数据展示组件
- 表单组件
- 交互式组件
- 可复用组件库

## 技术栈
- React 16.8+
- JavaScript/TypeScript
- JSX
- CSS/SCSS/Styled-components
- React Testing Library

## 示例代码
```jsx
import React, { useState, useEffect } from 'react';

const UserDataComponent = ({ userId }) => {
  const [userData, setUserData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchUserData(userId)
      .then(data => {
        setUserData(data);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching user data:', error);
        setLoading(false);
      });
  }, [userId]);

  if (loading) {
    return <div>Loading...</div>;
  }

  return (
    <div className="user-data">
      <h2>{userData?.name}</h2>
      <p>Email: {userData?.email}</p>
      <p>Role: {userData?.role}</p>
    </div>
  );
};

export default UserDataComponent;
```

## 最佳实践
1. 使用函数组件和Hooks
2. 保持组件单一职责
3. 合理使用memo优化性能
4. 编写清晰的PropTypes或TypeScript类型
5. 遵循React命名约定