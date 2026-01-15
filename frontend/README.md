# Frontend (Azure Static Web Apps)

这是一个极简静态页面：在浏览器端把 `report.md` 渲染成可阅读的 HTML。

## 本地预览（零安装）

仓库根目录执行：

- `python3 -m http.server 8000 --directory frontend`
- 浏览器打开：`http://localhost:8000`

> 说明：直接双击打开 `index.html` 在部分浏览器会触发跨域限制，导致 `fetch(report.md)` 失败；用本地静态服务器即可。

## 使用方式

- 默认渲染：`frontend/report.md`

## 部署到 Azure Static Web Apps

你不需要在这台机器安装 Node。

在 Azure Static Web Apps 创建资源并连接到 GitHub 仓库时，设置（或在 GitHub Actions workflow 里设置）类似：

- `app_location`: `frontend`
- `api_location`: (留空)
- `output_location`: (留空)

这样 SWA 会把 `frontend/` 作为静态站点根目录进行部署。

### 可选：使用 SWA CLI 初始化（仅在有 Node 的环境）

如果你在另一台机器/CI 上有 Node，可使用：

- `npx swa init --yes`

> 按最佳实践：不要手写 `staticwebapp.config.json` 或 `swa-cli.config.json`；它们应由 SWA CLI 生成。
