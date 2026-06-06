# 03 — 设计规范

## 品牌风格
- **调性：** 简洁、专业、可信赖
- **关键词：** 极简主义、开发者友好、高效

## 色彩系统
```css
:root {
  /* 主色调 — 蓝色系（信任感、技术感） */
  --color-primary: #2563eb;       /* 主色 */
  --color-primary-hover: #1d4ed8; /* 悬停 */
  --color-primary-light: #dbeafe; /* 浅色背景 */

  /* 中性色 */
  --color-bg: #ffffff;            /* 页面背景 */
  --color-bg-secondary: #f8fafc;  /* 次级背景 */
  --color-text: #0f172a;          /* 主文字 */
  --color-text-secondary: #64748b;/* 次级文字 */
  --color-border: #e2e8f0;        /* 边框 */

  /* 暗色模式 */
  --color-bg-dark: #0f172a;
  --color-bg-dark-secondary: #1e293b;
  --color-text-dark: #f1f5f9;
  --color-text-dark-secondary: #94a3b8;
  --color-border-dark: #334155;

  /* 功能色 */
  --color-success: #16a34a;
  --color-warning: #d97706;
  --color-error: #dc2626;
}
```

## 字体
```css
body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto,
               'Helvetica Neue', Arial, 'Noto Sans SC', sans-serif;
  line-height: 1.6;
}
/* 代码块 */
code, pre {
  font-family: 'JetBrains Mono', 'Fira Code', 'Cascadia Code', Consolas,
               'Courier New', monospace;
}
```

## 间距系统
使用 4px 基准网格：
- `xs: 4px` | `sm: 8px` | `md: 16px` | `lg: 24px` | `xl: 32px` | `2xl: 48px` | `3xl: 64px`

## 组件规范

### 按钮
- 主按钮：主色背景 + 白色字 + 8px 16px padding + 6px 圆角
- 次按钮：透明背景 + 主色边框 + 主色字
- CTA 按钮（购买）：稍大一号，用亮色突出（如琥珀色）

### 卡片
- 白色背景 + 1px 边框 + 8px 圆角 + 浅阴影

### 导航
- 顶部固定，简洁（Logo + 3-5个链接）

## 页面布局
- 最大内容宽度: `960px`
- 居中布局: `margin: 0 auto`
- 首屏 Hero 区：标题 + 副标题 + CTA 按钮
- 工具区：卡片式排列，每个工具一个卡片
