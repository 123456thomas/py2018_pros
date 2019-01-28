"""
__title__ = ''
__author__ = 'Thompson'
__mtime__ = '2018/9/25'
# 爬取http://www.jokeji.cn/hot.htm笑话集，获取页面编码，保存html文件
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

from urllib import request,parse
import chardet

# 设置请求头
headers = {"User-Agent": 'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)'}
urls = "http://www.jokeji.cn/hot.asp?"
# me_page=1

page = int(input("页码："))
for i in range(page):
    # 抓取页面
    urlss = urls + "me_page=%s"%i
    req = request.Request(urlss,headers=headers)
    response = request.urlopen(req)
    html = response.read()
    charset = chardet.detect(html)['encoding']
    print(charset)
    html = html.decode(charset,'ignore')
    with open('jocke%s.html'%i,'w',encoding='utf8') as f_w:
        f_w.write(html)

