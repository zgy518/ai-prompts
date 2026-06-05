# CLAUDE.md — 项目 AI 助手指引

## 项目目标
用 GitHub Pages + Jekyll 搭建轻量变现网站，辅助独立开发者通过数字产品赚钱。

## AI 职责边界（重要）

### ✅ AI 负责
- 技术实现：HTML/CSS/JS、Jekyll 配置、GitHub Pages 部署
- 文档编写：标准文档、开发日志、README
- 创意意见：提供产品/工具/推广创意供产品经理参考
- 自动化：格式化、代码优化、SEO 标签生成
- 问题排查：网站兼容性、性能、部署问题

### ❌ AI 不越界（产品经理决策）
- 产品方向的最终选择
- 定价策略的最终决定
- 目标用户画像的确定
- 品牌命名和定位
- 主动推进产品开发阶段

### 工作原则
- 当被问到产品相关问题时，给出分析但不替产品经理做决定
- 可以给出多个选项 + 优劣对比，让产品经理选择
- 技术上准备好"随时能接"，但产品决策不下来不开工

## 核心原则
- 一切改动面向"赚钱"目标，不做过度工程
- 优先用最轻量的方案（纯 HTML/CSS，避免引入框架除非必要）
- AI 可以辅助制作产品内容、文案、设计（在收到明确指令时）
- 每次修改后更新 devlog

## 文件结构速查

| 路径 | 用途 |
|------|------|
| `CLAUDE.md` | 本文件，AI 工作指引 |
| `README.md` | 项目说明 & 快速开始 |
| `docs/00-overview.md` | 项目总览与目标 |
| `docs/01-requirements.md` | 产品需求文档 (PRD) |
| `docs/02-tech-spec.md` | 技术规范 |
| `docs/03-design-spec.md` | 设计规范 |
| `docs/04-execution-plan.md` | 分阶段执行清单 |
| `docs/05-monetization.md` | 变现策略 |
| `docs/06-compliance.md` | 合规文档（隐私政策/服务条款） |
| `docs/07-promotion.md` | 推广计划 |
| `docs/08-changelog.md` | 变更日志 |
| `devlog/template.md` | 日志模板 |
| `devlog/YYYY-MM-DD.md` | 每日开发日志 |
| `_config.yml` | Jekyll 配置 |
| `_layouts/default.html` | 默认布局模板 |
| `_includes/` | 可复用组件 |
| `assets/css/style.css` | 主样式文件 |
| `assets/js/main.js` | 主脚本文件 |

## AI 工作流程

1. **收到新需求** → 查阅 `docs/01-requirements.md`，确认是否已有相关定义
2. **开始编码前** → 查阅 `docs/02-tech-spec.md` 和 `docs/03-design-spec.md`，确保遵循规范
3. **与赚钱相关决策** → 查阅 `docs/05-monetization.md`，确保不偏离变现目标
4. **修改完成后** → 更新 `docs/08-changelog.md` + 写当日 `devlog/YYYY-MM-DD.md`

## 技术栈约束
- 托管：GitHub Pages（免费）
- 生成器：Jekyll（GitHub 原生支持）
- 样式：纯 CSS，无框架（除非规范中另有约定）
- 脚本：原生 JS，无框架
- 收款：面包多 mbd.pub（国内主力）+ PayPal（海外）+ Buy Me a Coffee（打赏）

## 禁止事项
- 不要引入 npm/webpack/vite 等构建工具（保持零构建）
- 不要使用 React/Vue 等前端框架
- 不要做用户系统/登录（GitHub Pages 无法做服务端）
- 不要在未阅读 docs 对应标准文件前随意修改代码
