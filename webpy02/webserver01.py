from http.server import HTTPServer,BaseHTTPRequestHandler
# 提供了创造web服务器的功能
import os

# 导入解析模块，求取get的路径和返回值
from urllib import parse

# 导入正则模块
import  re


# 编写请求回调类，对于web请求，常用的有两种
class RequestCallBack(BaseHTTPRequestHandler):
    # 经过服务端的get请求
    def do_GET(self):
        print("收到GET请求")
        # print(parse.urlparse(self.path))
        path = parse.urlparse(self.path).path
        # query为问号后方的键值对
        query = parse.urlparse(self.path).query
        if path=="/favicon.ico":#排除图片路径
            return
        # 给出文件的相对路径
        root="webroot" + path
        print(root)
        print(query)
        # 返回状态码,200表示有响应
        self.send_response(200)
        # 返回头部，关键字、值，可以设置多个请求头
        self.send_header("Content Type","text/html")
        # 结束设置头部
        self.end_headers()
        # 在body里写书html文件，即写入页面信息
        #1）一段文字的写入
        # html="""
        #     <html>
        #         <body>
        #             <div id="pswid">
        #                 <p>至饿时，这是一个最好的世界也是一个最坏的世界</p>
        #                 <h4>你迎客</h4>
        #             </div>
        #         </body>
        #
        #     </html>
        # """
        #2）导入静态页面
        with open(root,"r",encoding="utf8") as f:
            self.wfile.write(f.read().encode("utf8"))
        # 3）动态页面（交互更新）
        with open(root,"r",encoding="utf8") as f:
            filestr = f.read()
            print(filestr)
            #替换
            filestr = re.sub("{%.*?%}",query,filestr)
            self.wfile.write(filestr.encode("utf8"))
    # 经过服务端的post请求，在表中提交两次才能获取数据（需要一次提交激活）
    def do_POST(self):
        print("收到POST请求")
        info = self.rfile.read().decode("utf8")
        print(info,type(info))
        # 接收返回数据，正则匹配
        result=re.findall("username=(.*?)$",info,re.I)
        print(result[0])
# 构造http服务器
sadd=("192.168.12.23",9090)
sever=HTTPServer(sadd,RequestCallBack)
# 开启服务
sever.serve_forever()
print("服务启动了")
