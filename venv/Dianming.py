import os,random,sys,json
#创建名单json数据
Allname="宋俊熠，耿红鸽，陈燕，毛孟珍，韩勇，王振兴，曹翔，" \
      "熊文洁，张梦梦，牛浩旭，李翔，靳凯元，裴祖光，谢兆闯，" \
      "付斌，郝宜枫，杜志强，许金波，胡文壮，付文彩，雷胜强，" \
      "曹建超，张万新，史文飞，宋群鹏"
Alname=Allname.split("，")
x=dict.fromkeys(Alname,0)
NameDict={"py1809":x}
print(NameDict)
# 序列化,创建Json
def CreatJs(path="DianBing.txt"):#读取文件
    global NameDict
    if not os.path.exists(path):
        with open(path,"w",encoding="utf-8") as f_w:
            json.dump(NameDict,f_w)
    else:
        with open(path,"r",encoding="utf-8") as f_r:
            NameDict=json.load(f_r)
# CreatJs()
def DanMj(path="DianBing.txt"):#随机点名
    while True:
        listA=list(NameDict["py1809"].keys())
        random.shuffle(listA)
        temp=listA[random.randint(0,len(NameDict["py1809"].keys())-1)]
        NameDict["py1809"][temp]+=1
        print(temp,NameDict["py1809"][temp])
        if input("结束点名，请输入q或Q:").lower()=="q":
            with open(path,"w",encoding="utf-8") as f_w:
                json.dump(NameDict,f_w)
                print(NameDict)
                break
# DanMj()
def Sortcount(path="DianBing.txt"):#排序
    listB=[]
    for i,j in NameDict["py1809"].items():
        listB.append([i,j])
    listB.sort(key=lambda x:x[1],reverse=True)
    print(listB)
# Sortcount()
def Delone(path="DianBing.txt"):
    f=True
    while f:
        temp=input("请输入要删除的一个名字：")
        while temp=="" or temp not in NameDict["py1809"].keys():
            temp = input("请输入要删除的名字：")
        del NameDict["py1809"][temp]
        with open(path,"w",encoding="utf-8") as f_w:
            json.dump(NameDict,f_w)
            print("数据更新完成\n",NameDict)
        if input("是否还要继续删除（y/n）").lower()=="n":
            f=False
# # Delone()
def AddUser(path="DianBing.txt"):
    print(NameDict)
    if os.path.exists(path):
        f = True
        while f:
            temp = input("请输入要添加的一个名字：")
            while temp == "" or temp in NameDict["py1809"].keys():
                temp = input("输入错误请输入要添加的名字：")
            NameDict["py1809"][temp]=0
            with open(path, "w", encoding="utf-8") as f_w:
                json.dump(NameDict, f_w)
                print("数据更新完成\n", NameDict)
            if input("是否还要继续添加（y/n）").lower() == "n":
                f = False
# # AddUser()
def main():
    while True:
        t=input("欢迎来到**点名系统,请选择:\n1.点名。2.排序。3.删除。4.添加。5.退出")
        CreatJs()
        if t=="1":
            DanMj()
        elif t=="2":
            Sortcount()
        elif t=="3":
            Delone()
        elif t=="4":
            AddUser()
        elif t=="5":
            sys.exit()
        else:
            print("输入有误，重新选择")
main()
