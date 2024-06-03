# DrissionPage
## 官方网站链接
https://www.drissionpage.cn/get_start/before_start

## 基本概念
DrissionPage 以页面为单位将两者整合，对 Chromium 协议 和 requests 进行了重新封装，实现两种模式的互通，并加入常用的页面和元素控制功能，可大幅降低开发难度和代码量。
用于操作浏览器的对象叫 Driver，requests 用于管理连接的对象叫 Session，Drission 就是它们两者的合体。Page 表示以 POM 模式封装。

### 使用逻辑
无论是控制浏览器，还是收发数据包，其操作逻辑是一致的。

即先创建页面对象，然后从页面对象中获取元素对象，通过对元素对象的读取或操作，实现数据的获取或页面的控制。

因此，最主要的对象就是两种：页面对象，及其生成的元素对象。

### 主要对象
主页面对象有 3 种，它们通常是程序的入口：

ChromiumPage：单纯用于操作浏览器的页面对象
WebPage：整合浏览器控制和收发数据包于一体的页面对象
SessionPage：单纯用于收发数据包的页面对象

衍生物：

ChromiumTab：ChromiumPage生成的标签页对象
WebPageTab：WebPage生成的标签页对象
ChromiumFrame：<iframe>元素对象
ChromiumElement：浏览器元素对象
SessionElement：静态元素对象
ShadowRoot：shadow-root 元素对象