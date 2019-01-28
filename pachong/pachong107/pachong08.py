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

# 导入请求模块，编码/编译
from urllib import request,parse
import chardet, os

# 设置请求头
headers = {"User-Agent": 'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)'}
urls = "http://yunqi.qq.com/bk/"
# http://yunqi.qq.com/bk/so2/n10p3
if not os.path.exists('data'):
    os.mkdir('data')
for i in range(1,6):
    # 抓取页面
    urlss = urls + "so2/n10p%s"%i
    print(urlss)
    req = request.Request(urlss,headers=headers)
    response = request.urlopen(req)
    html = response.read()
    charset = chardet.detect(html)['encoding']
    print(charset)
    html = html.decode(charset,'ignore')
    # path = os.path.join("data","yunqi_*.txt")
    # print(path)
    with open("data/yunqi_.txt",'a',encoding='utf8') as f_w:
        f_w.write(html)
        f_w.write("\n")