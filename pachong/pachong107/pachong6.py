"""
__title__ = ''
__author__ = 'Thompson'
__mtime__ = '2018/9/25'
# 6、从西刺网查找代理ip，通过代理ip爬取腾讯首页，打印爬取内容
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

# 导入模板
from urllib import request,parse
import chardet, zlib

# 设置请求头
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0)"}

# 定义代理地址
proxy ={'http': "211.159.219.225:8118"}

# 创建代理处理器对象
proxy_handler = request.ProxyHandler(proxy)

# 创建opener对象
opener = request.build_opener(proxy_handler)

# 安装opener
request.install_opener(opener)

# 抓取网页
req = request.Request("https://www.qq.com/",headers=headers)
response = request.urlopen(req)
html = response.read()
print(html)
# 解压缩处理
encoding = response.info().get('content-encoding')
if encoding == "gzip":
    html = zlib.decompress(html, 16 + zlib.MAX_WBITS)
    print(html)
elif encoding == 'deflate':
    try:
        html = zlib.decompress(html, -zlib.MAX_WBITS)
    except zlib.error:
        html = zlib.decompress(html)

# 获取编码方式
charset = chardet.detect(html)['encoding']
print(charset)
# 'ignore'如果解码错误，跳过
html = html.decode(charset,'ignore')
print(html)

# 写入文本
with open('Tencent.html', 'w',encoding='utf8') as f_w:
    f_w.write(html)