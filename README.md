# DevToolkit — 免费开发者在线工具站

> 用 GitHub Pages + Jekyll 搭建的轻量变现网站。
> 免费工具获取流量 → 数字产品变现。

## 快速开始

### 1. 环境要求
- Ruby 2.7+（Jekyll 依赖）
- Bundler（`gem install bundler`）

### 2. 本地运行
```bash
cd 项目目录
bundle exec jekyll serve
```
浏览器打开 `http://localhost:4000`

### 3. 部署
推送到 GitHub，在仓库 Settings → Pages 中启用 GitHub Pages。

## 项目结构

```
├── CLAUDE.md            # AI 助手指引
├── docs/                # 项目标准文档
│   ├── 00-overview.md   # 项目总览
│   ├── 01-requirements.md # PRD 需求
│   ├── 02-tech-spec.md  # 技术规范
│   ├── 03-design-spec.md# 设计规范
│   ├── 04-execution-plan.md # 执行计划
│   ├── 05-monetization.md   # 变现策略
│   ├── 06-compliance.md     # 合规文档
│   └── 07-promotion.md      # 推广计划
├── devlog/              # 开发日志
├── _layouts/            # Jekyll 布局
├── _includes/           # 可复用组件
├── assets/              # 静态资源
└── index.html           # 首页
```

## 变现路线

```
免费工具（流量入口）
    → 建立信任
    → 产品着陆页
    → Gumroad 购买（自动交付）
```

## 技术栈
- **托管：** GitHub Pages（免费）
- **生成器：** Jekyll
- **样式：** 纯 CSS（零构建）
- **脚本：** 原生 JavaScript
- **收款：** Gumroad（数字产品）+ Buy Me a Coffee（打赏）

## 代办清单
- [ ] 注册 Gumroad 账号
- [ ] 注册 PayPal 账号
- [ ] 确定第一款产品方向
- [ ] 完成网站全部页面
- [ ] 部署上线
- [ ] SEO + 推广

## 许可
MIT License
