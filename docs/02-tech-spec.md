# 02 — 技术规范

## 技术栈
| 层 | 技术 | 版本要求 |
|----|------|---------|
| 托管 | GitHub Pages | - |
| 静态生成 | Jekyll | 4.x（GitHub Pages 默认） |
| 样式 | CSS3（无预处理器） | - |
| 脚本 | 原生 JavaScript (ES6+) | - |
| 模板 | Liquid（Jekyll 内置） | - |
| 域名 | `{username}.github.io/{repo}` | - |

## 目录约定
```
├── _layouts/       # 页面布局模板（Liquid）
├── _includes/      # 可复用组件（header, footer 等）
├── _posts/         # 博客文章（文件名格式：YYYY-MM-DD-title.md）
├── assets/         # 静态资源（CSS/JS/图片）
├── docs/           # 项目文档
├── devlog/         # 开发日志
└── index.html      # 首页
```

## 命名规范
- **文件名：** 小写英文 + 连字符（kebab-case），如 `privacy-policy.md`
- **CSS 类名：** kebab-case，如 `.hero-section`
- **JS 变量：** camelCase，如 `const toolInput = ...`
- **Jekyll 变量：** snake_case，如 `{{ site.title }}`

## CSS 规范
- 不使用 CSS 框架（Bootstrap/Tailwind）
- 使用 CSS 自定义属性（变量）管理颜色和间距
- 移动优先的响应式设计
- 断点：`768px`（平板）、`1024px`（桌面）

## JS 规范
- 原生 JS，不引入 jQuery
- 每个工具放在独立文件中，按需加载
- 使用 `defer` 属性异步加载
- 不做 XHR 请求（静态站不需要）

## 性能目标
- 单页总大小 < 500KB（含图片）
- 首次内容绘制 (FCP) < 1.5s
- 图片使用 WebP 格式，加 lazy loading
- CSS/JS 不压缩（保持可读性），不打包

## 兼容性
- Chrome（最近2个版本）
- Firefox（最近2个版本）
- Safari（最近2个版本）
- Edge（最近2个版本）
- 移动端浏览器
