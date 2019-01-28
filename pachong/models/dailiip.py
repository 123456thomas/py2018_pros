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
from urllib import request
import chardet

headers = {'User-Agent':'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)'}

# 定义代理ip
proxy = {'http':'110.52.235.249:9999'}
# 1、定义代理处理器对象
proxy_handler = request.ProxyHandler(proxy)
# 2、创建opener对象
opener = request.build_opener(proxy_handler)
# 使用UserAgent
opener.addheaders = [('User-Agent','Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)')]
# 3、安装opener
request.install_opener(opener)

# req = request.Request('https://www.jianshu.com',headers=headers)
response = request.urlopen('https://www.jianshu.com')
print(type(response))
html = response.read()
charset = chardet.detect(html)['encoding']
print(charset)
html = html.decode(charset)
with open('jianshu02.txt','w',encoding=charset) as f_w:
    f_w.write(html)