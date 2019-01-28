# 引入pymysql模块
import pymysql

#构建连接对象
con = pymysql.connect(host="localhost", user="night", password="361365",database="westernworld",port=3306)

#创建游标
cur = con.cursor()

# 开始交互
# result = cur.execute("call W_procedure") #用于执行的方法
rows = cur.execute("select * from user")
result=cur.fetchall()
print(result)

# 释放游标
cur.close()
#释放连接
con.close()