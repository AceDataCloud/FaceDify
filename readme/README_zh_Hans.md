# Face Transform

作者：acedatacloud。插件类型：工具提供商。

在 Dify 中调用 Ace Data Cloud Face Transform API。插件免费，API 调用按当前服务价格计费。

## 工具

| 工具 | API |
|---|---|
| `face_transform` | `/face/analyze` |

## 配置与工作流

从 https://platform.acedata.cloud/console/credentials 创建此服务的 Token，在 Dify 中使用 `acedata_bearer_token` 授权，无需填写 Bearer 前缀。审核期间可通过 Dify 官方远程调试方式连接独立测试环境；官方市场上架后再从 Marketplace 安装。

创建“开始 → Face Transform 工具 → 输出”。按工具中的说明选择模型和参数，数组或对象参数使用 JSON。此服务没有免费任务校验接口，配置时只验证 Token 格式；实际调用时验证服务权限。

输出包含 status、success、task_id、trace_id、data、result、media_urls。完成的图片以 Dify 图片消息展示，其他媒体返回结果链接。错误会使工具节点失败。以上工具表定义本版本支持的接口。

模型和参数以当前公开 API 为依据。插件固定连接 api.acedata.cloud，关闭重定向和付费自动重试，不添加模型回退；任务输出不包含保存的原始请求、账户或路由信息。请在 https://platform.acedata.cloud/models 查看价格，在 https://platform.acedata.cloud/console/usages 按任务及追踪 ID 核对扣费。Dify 节点执行次数不等于 API 计费记录。

仅提交有权使用的内容，不要把 Token 放入提示词或导出的工作流。隐私说明见仓库 PRIVACY.md。

源码：https://github.com/AceDataCloud/FaceDify 。支持：dev@acedata.cloud。
