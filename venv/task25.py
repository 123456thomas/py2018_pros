# 1.当前程序目录下创建py文件夹，目录里创建十个子文件 夹,并且命名为1-10
# 2.在子文件夹1-10里，偶数文件夹下创建新文件夹，命名 end
# 3.将子文件夹中2,4,8里的end重命名为end2，end4， end8
# 4.删除子文件2
# 5.打印py文件夹中所有文件夹名称
# 6.删除py及其所有子文件夹
# 7.浮点数20.73，向上取整，向下取整，正弦值
# 8.弧度π/4，π/2,对应的度

# #任务1
# # import os
# # if not os.path.exists(("py")):
# #     os.mkdir("py")
# #     for i in range(10):
# #         os.makedirs(r"py/%s"%str(i+1))
#
# #任务2：
# # import os
# # for i in range(10):
# #     if (i+1)%2==0:
# #         os.makedirs(r"py/%s/end"%str(i+1))
# #方法2
# #任务3
# # import os
# # for i in [2,4,8]:
# #     os.rename(r"py/%s/end"%str(i),r"py/%s/end"%str(i)+str(i))
# #任务4
# # import os
# # path=os.path.abspath(r"py/2")
# # print(path)
# # os.removedirs(path+r"\end2")
# #任务5
# # import os
# # listA=os.listdir("py")
# # print(listA)
# #任务6
# def Delfiles(path):
#     import os
#     listA=os.listdir(path)
#     print(listA,path)
#     for i in listA:           #如果为空则返回上级，
#         temp=os.path.join(path, i)
#         # print(i)
#         if os.path.isdir(temp):
#             Delfiles(temp)
#             # os.rmdir(temp)
#         # else:
#             # os.remove(temp)
# path=r"D:\Py1809Project\venv\py"
# Delfiles(path)
# def RemDir2(path):
#     import os
#     listA=os.listdir(path)
#     for i in listA:
#         temp=os.path.join(path,i)
#         if os.path.isdir(temp):
#             RemDir2(temp)
#             os.mkdir(temp)
#         else:
#             os.remove(temp)
#
# def RemDir1(str1):
#     import os
#     path=os.path.abspath(str1)
#     # x=os.path.split(path)
#
#     # return RemDir2(path)
# # RemDir1("py")
#
# # import os
# # path=os.path.abspath("py")
# # os.remove(path)
# # x=os.path.split(path)
# # name=os.path.basename(x[0])
# # listA=os.listdir(name)
# # print(path,x,name,listA)
# # 任务7
# # import math
# # t1=math.ceil(20.73)
# # t2=math.floor(20.73)
# # t3=math.sin(math.pi*(20.73/180))
# # print(t1,t2,t3)
# #任务8：弧度π/4，π/2,对应的度
# # import math
# # t1=(math.pi/4)/(math.pi)*180
# # t2=(math.pi/2)/(math.pi)*180
# # print(t1,t2)

def CreatDirs(path,name):
    import os
    for i in range(1):
        for j in range(5):
            for k in range(5):
                temp=os.path.join(path,name)
                CreatDirs(path, name)

CreatDirs(r"D:\","流星阁")

