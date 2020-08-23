# JD-Spider

该项目用于爬取京东的商品信息

## 说明

采用 selenium 作为爬虫工具，爬取完数据后使用 flask 起服务，采用 Vue3(Option API) 编写 web 界面展示结果。

### selenium WebDriver

在[selenium 浏览器支持列表](https://www.selenium.dev/documentation/zh-cn/getting_started_with_webdriver/browsers/)中查看并下载 Chrome 的驱动（项目采用 Chrome），将下载好的文件放置在`bin`目录下（或者添加在环境变量中，代码中的`executable_path`需要变化）。

## 参考链接

1. [selenium 文档](https://selenium-python-zh.readthedocs.io/en/latest/installation.html)
2. [python flask 文档](https://dormousehole.readthedocs.io/en/latest/quickstart.html)
3. [vite project](https://github.com/vitejs/vite)
