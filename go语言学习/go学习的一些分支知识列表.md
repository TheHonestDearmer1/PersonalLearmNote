## gin框架

Gin 是一个用 Go (Golang) 编写的 Web 框架。 它具有类似 martini 的 API，性能要好得多，多亏了 [httprouter](https://link.zhihu.com/?target=https%3A//github.com/julienschmidt/httprouter)，速度提高了 40 倍。 如果您需要性能和良好的生产力，您一定会喜欢 Gin。 **特性** 快速：基于 Radix 树的路由，小内存占用。没有反射。可预测的 API 性能。 支持中间件：传入的 HTTP 请求可以由一系列中间件和最终操作来处理。 例如：Logger，Authorization，GZIP，最终操作 DB。 Crash处理：Gin 可以 catch 一个发生在 HTTP 请求中的 panic 并 recover 它。这样，你的服务器将始终可用。例如，你可以向 Sentry 报告这个 panic！ Json验证：Gin 可以解析并验证请求的 JSON，例如检查所需值的存在。 **路由组** 更好的组织路由。是否需要授权，不同的 API 版本…… 此外，这些组可以无限制地嵌套而不会降低性能。 **错误管理** Gin 提供了一种方便的方法来收集 HTTP 请求期间发生的所有错误。最终，中间件可以将它们写入日志文件，数据库并通过网络发送。 **内置渲染** Gin 为 JSON，XML 和 HTML 渲染提供了易于使用的 API **可扩展**

## Go语言框架三件套（Web/RPC/GORM)

[Go语言框架三件套（Web/RPC/GORM) - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/601286934?utm_id=0)

## rabbitMQ