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

from urllib import request,parse
import chardet,json

headers = {'User-Agent':'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)'}

url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"

# 表单构建
Form_Data = {}

Form_Data['from'] = 'AUTO'
Form_Data['to'] = 'AUTO'
Form_Data['smartresult'] = 'dict'
Form_Data['client'] = 'fanyideskweb'
Form_Data['salt'] = '1537857955340'
Form_Data['sign'] = '6b7991fb756c4184630db11382d640b0'
Form_Data['doctype'] = 'json'
Form_Data['version'] = '2.1'
Form_Data['keyfrom'] = 'fanyi.web'
Form_Data['action'] = 'FY_BY_REALTIME'
Form_Data['typoResult'] = 'false'

req =request.Request(url,headers=headers)
while True:
    tom = input("请输入")
    Form_Data['i'] = tom
    data = parse.urlencode(Form_Data).encode('utf-8')

    # post请求
    response = request.urlopen(req, data=data)

    # 读取请求的结果
    html = response.read().decode()
    print(html)
    translate_result = json.loads(html)
    result = translate_result["translateResult"][0][0]['tgt']
    # 打印翻译结果
    print('翻译的结果：', result)