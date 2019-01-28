"""
__title__ = ''
__author__ = 'Thompson'
__mtime__ = '2018/9/25'
# 5、批量爬取贴吧数据
# 输入贴吧名称， 起始页码， 结束页码， 爬取贴吧数据， 以‘第x页.html’ 命名， 保存为html 文件.
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
import chardet

# 设置请求头
headers = {"User-Agent": 'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)'}
urls = "https://tieba.baidu.com/f?"
search = input("贴吧搜索：")
while True:
    try:
        search_num1 = int(input("起始贴吧页数："))
        search_num2 = int(input("终止贴吧页数："))
        if search_num1>search_num2:
            tem = search_num1
            search_num1 = search_num2
            search_num2 = tem
        break
    except:
        pass
search = parse.urlencode({"kw": search})
print(search)
urls = urls + search

for i in range(search_num1,search_num2+1):
    # 抓取页面
    page ="&pn=" + str((i-1)*50)
    urlss = urls + page
    print(urlss)
    req = request.Request(urlss, headers=headers)
    print(req)
    try:
        response = request.urlopen(req)
    except:
        break
    # 读取并存取数据
    html =response.read()
    charset = chardet.detect(html)['encoding']
    print(charset)
    html = html.decode("utf8")
    filename = "page" +str(i) + ".html"
    with open(filename, "w",encoding="utf8") as f_w:
        f_w.write(html)


