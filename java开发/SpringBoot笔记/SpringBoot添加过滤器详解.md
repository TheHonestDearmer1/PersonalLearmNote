 

**目录**

[一、过滤器详解](#t0)

[二、SpringBoot 添加过滤器](#t1) 

* * *

#### 一、过滤器详解

过滤器（Filter）是 [Java](https://so.csdn.net/so/search?q=Java&spm=1001.2101.3001.7020) Web 应用中的一种重要组件，用于对请求和响应进行拦截和处理。它可以用于执行各种任务，如请求预处理、请求和响应的转换、授权检查、日志记录、字符编码处理等。在 Java Web 开发中，过滤器通常用于全局性的操作，以确保在进入和离开 Web 应用程序时执行相同的逻辑。

1.  **过滤器接口：** 在 Java Servlet 规范中，过滤器是一个实现了 `javax.servlet.Filter` 接口的类。该接口定义了三个主要方法：
    
    *   `init(FilterConfig filterConfig)`: 在过滤器被初始化时调用，通常用于执行一次性的初始化工作。
    *   `doFilter(ServletRequest request, ServletResponse response, FilterChain chain)`: 在请求进入过滤器时调用，可对请求和响应进行处理，然后将请求传递给下一个过滤器或目标 Servlet。
    *   `destroy()`: 在过滤器被销毁时调用，通常用于清理资源。
2.  **过滤器链（Filter Chain）：** 多个过滤器可以按照配置的顺序形成一个过滤器链。每个过滤器都可以选择在请求被传递给下一个过滤器之前或之后执行逻辑。过滤器链通常由 Servlet 容器（如 Tomcat 或 Jetty）维护。
    
3.  **过滤器配置：** 过滤器可以通过配置在 `web.xml` 文件中或使用 Servlet 3.0+ 注解进行配置。在 `web.xml` 中配置的过滤器称为部署描述符配置的过滤器，而使用注解配置的过滤器称为编程式配置的过滤器。
    
4.  **过滤器的应用场景：** 过滤器可以用于各种应用场景，包括但不限于：
    
    *   认证和授权：检查用户是否已登录，是否有权限访问某个资源。
    *   请求和响应日志记录：记录请求和响应的详细信息，用于调试和监控。
    *   字符编码处理：确保请求和响应中的字符编码正确。
    *   输入数据校验和清理：验证和清理用户输入数据，防止安全漏洞（如 XSS 攻击）。
    *   图像、视频或其他多媒体转换：将请求中的媒体内容转换为不同的格式。
    *   请求重定向：根据某些条件将请求重定向到不同的目标。
    *   缓存控制：管理浏览器缓存策略。
5.  **过滤器的执行顺序：** 过滤器的执行顺序由它们在 `web.xml` 或注解中的声明顺序决定。首先执行部署描述符中声明的过滤器，然后按照编程式配置的顺序执行过滤器。
    
6.  **过滤器的异常处理：** 过滤器可以捕获并处理异常，然后选择将请求传递给下一个过滤器或中断请求的处理流程。通常，过滤器可以使用 `HttpServletResponse` 来发送错误响应。
    
7.  **过滤器的生命周期：** 过滤器的生命周期由 Servlet 容器管理。容器在启动时初始化过滤器，之后每次请求都会创建新的过滤器实例，并在请求处理完毕后销毁它。
    

#### 二、SpringBoot 添加过滤器 

在 Spring Boot 中添加过滤器（Filter）是通过实现 `javax.servlet.Filter` 接口并将其注册到应用程序中的方法来实现的。过滤器可以用于对请求和响应进行[预处理](https://so.csdn.net/so/search?q=%E9%A2%84%E5%A4%84%E7%90%86&spm=1001.2101.3001.7020)或后处理，通常用于执行一些与请求/响应相关的操作，例如日志记录、授权检查、字符编码处理等。

1.  **创建过滤器类：** 首先，您需要创建一个类，实现 `javax.servlet.Filter` 接口，并实现 `doFilter` 方法来定义过滤器的逻辑。以下是一个简单的示例：
    
    ```java
    import javax.servlet.Filter;
    import javax.servlet.FilterChain;
    import javax.servlet.FilterConfig;
    import javax.servlet.ServletException;
    import javax.servlet.ServletRequest;
    import javax.servlet.ServletResponse;
    import java.io.IOException;
    
    public class MyFilter implements Filter {
    
        @Override
        public void init(FilterConfig filterConfig) throws ServletException {
            // 初始化方法
        }
         
        @Override
        public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain)
                throws IOException, ServletException {
            // 在请求处理前执行的逻辑
            // 您可以在这里执行任何与请求相关的操作
            // 例如，日志记录、授权检查、字符编码处理等
         
            // 继续执行过滤器链,也就是意思是通过这个过滤器校验通过了
            chain.doFilter(request, response);
         
            // 在请求处理后执行的逻辑
            // 您可以在这里执行任何与响应相关的操作
        }
         
        @Override
        public void destroy() {
            // 销毁方法
        }
    
    }
    ```
    
2.  **配置过滤器：** 在 Spring Boot 中，您可以通过 `FilterRegistrationBean` 类来配置和注册自定义过滤器。通常，您需要在 Spring Boot 的配置类中进行配置。以下是一个示例：
    
    ```java
    import org.springframework.boot.web.servlet.FilterRegistrationBean;
    import org.springframework.context.annotation.Bean;
    import org.springframework.context.annotation.Configuration;
    
    @Configuration
    public class MyFilterConfig {
    
        @Bean
        public FilterRegistrationBean<MyFilter> myFilter() {
            FilterRegistrationBean<MyFilter> registrationBean = new FilterRegistrationBean<>();
            registrationBean.setFilter(new MyFilter());
            registrationBean.addUrlPatterns("/api/*"); // 配置过滤的 URL
            return registrationBean;
        }
    
    }
    ```
    
    在上面的示例中，我们创建了一个 `FilterRegistrationBean` 并将自定义的 `MyFilter` 实例设置为过滤器。然后，使用 `addUrlPatterns` 方法指定要过滤的 URL 模式。
    
3.  **配置 URL 模式：** 在 `addUrlPatterns` 方法中，您可以指定要过滤的 URL 模式。在上述示例中，所有以 "/api/" 开头的请求都将被 `MyFilter` 过滤。
    
4.  **其他配置：** 您可以根据需要添加其他配置，例如过滤器的顺序、过滤器名称等。
    
5.  **运行应用程序：** 确保您的 Spring Boot 应用程序处于运行状态，过滤器将会拦截匹配的请求。
    

这样，就将自定义过滤器添加到了 Spring Boot 应用程序中。过滤器将按照配置的顺序对请求进行处理。

`ServletRequest`、`ServletResponse` 和 `FilterChain` 是 `javax.servlet` 包中的接口，用于处理 HTTP 请求和响应以及过滤器链。

- `ServletRequest` 接口代表了客户端的请求，包含了客户端发送的信息，比如请求头、请求参数、请求方法等。它是所有请求对象的父接口，常用的子接口是 `HttpServletRequest`。
- `ServletResponse` 接口代表了服务器对客户端请求的响应，包含了响应的信息，比如响应状态码、响应头、响应正文等。它是所有响应对象的父接口，常用的子接口是 `HttpServletResponse`。
- `FilterChain` 接口代表了过滤器链，用于按照指定的顺序依次调用多个过滤器。每个过滤器可以决定是否将请求传递给下一个过滤器或处理程序。

在过滤器的 `doFilter()` 方法中，传入的参数 `request` 是一个 `ServletRequest` 类型的对象，用于获取请求信息；`response` 是一个 `ServletResponse` 类型的对象，用于操作响应；`chain` 是一个 `FilterChain` 类型的对象，用于调用后续的过滤器链或处理程序。

通过 `request` 和 `response` 对象，您可以获取请求头、请求参数、请求方法，设置响应状态码、响应头、响应正文等。通过 `chain.doFilter(request, response)` 方法，将**请求传递给下一个过滤器或处理程序进行处理**（结束请求）。

需要根据实际需求，使用具体的子接口实现类（如 `HttpServletRequest` 和 `HttpServletResponse`）来进行操作和获取更具体的信息。



#### 请求和回应类型强制转换得到session等http信息

在Java中，ServletRequest是Servlet API中的一个接口，HttpServletRequest是继承自ServletRequest的子接口。ServletRequest对象是用来接收客户端的请求信息，HttpServletRequest对象则扩展了ServletRequest，提供了更多的方法来获取和操作HTTP请求的特定信息。

当创建一个Filter时，`doFilter`方法的参数`ServletRequest`和`ServletResponse`是通用的接口类型，不能直接访问到HttpServletRequest和HttpServletResponse对象的方法。因此，为了使用HttpServletRequest对象的方法，需要进行强制类型转换，将ServletRequest对象转换为HttpServletRequest对象。

一旦将ServletRequest对象转换为HttpServletRequest对象，就可以通过HttpServletRequest对象来获取HTTP请求的特定信息，例如获取当前会话（Session）对象。

在代码中，首先将servletRequest强制类型转换为HttpServletRequest对象，然后通过HttpServletRequest对象获取当前的会话（session），即`HttpSession session = request.getSession();`。通过这种方式，我们可以在过滤器中访问和操作当前会话的信息。

#### 往拦截的respone写入返回信息并结束请求

```java
            PrintWriter out = new HttpServletResponseWrapper(
                    (HttpServletResponse) servletResponse).getWriter();
            out.write("{\n"
                    + "    \"status\": 10009,\n"
                    + "    \"msg\": \"NEED_ADMIN\",\n"
                    + "    \"data\": null\n"
                    + "}");
            out.flush();
            out.close();
```

在这段代码中，`getWriter()` 方法返回一个 `PrintWriter` 对象，用于向客户端发送响应字符流数据。然后，使用 `write()` 方法将指定的字符串写入输出流，将数据发送给客户端。

具体来说，通过 `getWriter()` 方法获取到 `PrintWriter` 对象后，可以使用它的 `write()` 方法将文本或其他数据写入输出流。在这段代码中，通过 `write()` 方法将一个 JSON 格式的响应信息写入输出流，该信息包括一个名为 `status` 的字段，其值为 `10007`，一个名为 `msg` 的字段，其值为 `"NEED_LOGIN"`，以及一个名为 `data` 的字段，其值为 `null`。

最后，通过调用 `flush()` 方法强制将信息立即发送给客户端，然后调用 `close()` 方法关闭输出流，释放资源。完成后，响应数据将被传送回客户端。这段代码的目的是返回一个 JSON 形式的错误响应信息给客户端，告知客户端需要登录才能访问相应的资源。



文章知识点与官方知识档案匹配，可进一步学习相关知识

[Java技能树](https://edu.csdn.net/skill/java/?utm_source=csdn_ai_skill_tree_blog)[首页](https://edu.csdn.net/skill/java/?utm_source=csdn_ai_skill_tree_blog)[概览](https://edu.csdn.net/skill/java/?utm_source=csdn_ai_skill_tree_blog)136384 人正在系统学习中

本文转自 <https://blog.csdn.net/TreeShu321/article/details/132857990?spm=1001.2101.3001.6650.1&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-1-132857990-blog-120136004.235%5Ev39%5Epc_relevant_anti_t3_base&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-1-132857990-blog-120136004.235%5Ev39%5Epc_relevant_anti_t3_base&utm_relevant_index=2>，如有侵权，请联系删除。