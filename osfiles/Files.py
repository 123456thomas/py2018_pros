import os
listAll=[]
def CreatFiles(path,name,listA):
    """在一个路径下创建多层指定数目的目录,其中listA为每层中目录的个数"""
    for j in range(0,listA[0]):
        temp = os.path.join(path, name + str(j))
        if not os.path.exists(temp):
            os.mkdir(temp)
        if len(listA)==1:
            continue
        listB=listA[1:]
        CreatFiles(temp,name,listB)

def FindAll(path):
    """接受一个路径，查找该路径下的各层所有目录和文件，然后存在一个列表中，返回该列表"""
    x=os.listdir(path)
    for i in x:
        temp=os.path.join(path,i)
        listAll.append(temp)
        if os.path.exists(temp) and os.path.isdir(temp):
            FindAll(temp)
    return listAll

def RenameFiles(path,name):
    """给路径下的所有目录和文件重新命名"""
    x=os.listdir(path)
    for i in x:
        temp=os.path.join(path,i)
        if os.path.isfile(temp):
            a=i.split(".")
            t=os.path.join(path,name+str(x.index(i))+"."+a[1])
            os.rename(temp,t)
        else:
            t=os.path.join(path,name+str(x.index(i)))
            os.rename(temp,t)
            RenameFiles(t,name)

def DelFiles(path):
    """删除路径下的所有目录和文件，以及该本身文件夹"""
    if os.path.exists(path):
        if len(os.listdir(path))==0:
            os.removedirs(path)  #多级的删除
        else:
            x=os.listdir(path)
            for i in x:
                temp = os.path.join(path,i)
                if os.path.isdir(temp):
                    DelFiles(temp)
                else:
                    os.remove(temp)
