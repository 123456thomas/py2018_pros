"""
__title__ = ''
__author__ = 'Thompson'
__mtime__ = '2018/9/25'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
# level 1：
# 1、 什么是 http 协议？
#  http即超文本传输协议，基于TCP/IP通信协议族的网络协议，属于七层网络模型中的应用层。浏览器作为http客户端，
# 想http服务端发送请求，服务器收到请求后，向浏览器发送响应信息

# 2、 http 和 https 的区别？
#     http属于明文传输，在浏览器上可以看到明文，不安全；端口是80
#     https增加了一个ssl层，对传输的内容进行加密，相比于http更加安全。端口为443
# 3、 什么是爬虫，有哪些分类？
#     通过代码或者脚本，按照一定的规则从网页上获取数据的方式，可以分为：通用爬虫、
# 聚焦爬虫、增量式抓取、深度爬虫
# 4、 数据爬取的步骤有哪些？
#     一般分为三步：网页抓取、数据提取、数据储存。
# 5、批量爬取贴吧数据
# 输入贴吧名称， 起始页码， 结束页码， 爬取贴吧数据， 以‘第x页.html’ 命名， 保存为html 文件
# 6、从西刺网查找代理ip，通过代理ip爬取腾讯首页，打印爬取内容
#
#
#
# level 2：
# 7、爬取http://www.jokeji.cn/hot.htm笑话集，获取页面编码，保存html文件(爬取5页）
# 8、爬取云起书院http://yunqi.qq.com/bk,要求设置UA，爬取前5页，把内容保存在.\data\yunqi_*.txt文件中(爬取5页）