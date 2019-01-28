
# 导入request请求
from urllib import request


# 导入编码库
import chardet
# 设置请求头
headers = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0" }
req = request.Request('https://www.jianshu.com/',headers=headers)
# 榨取数据
response = request.urlopen(req)
print(type(response))
html = response.read()
charset = chardet.detect(html)['encoding']
print(charset)
html = html.decode(charset)
with open('jianshu01.txt','w',encoding=charset) as f_w:
    f_w.write(html)

