# 1、写一个方法，在方法内依次打印出列表每个元素的
# 值。
# 2、写一个方法，计算列表所有元素的和(注意返回值)。
# 3、写一个方法，计算列表所有奇数下标元素的和(注意返
# 回值)。
# 4、写一个方法，计算列表所有偶数下标元素的和(注意返回值)。
# 5、写一个方法可以计算两个数的和，想想这个方法有哪
# 些参数，返回值。39 / 486、写一个方法可以计算两个数的商(分母不能为0)，想想
# 这个方法有哪些参数，返回值是什么。
# 7、写一个方法将传入的天、小时、分钟、秒的总和转换
# 为秒，比如0天、2
# 小时、5
# 分、7
# 秒，他们代表的总秒数为
# 2 * 3600 + 5 * 60 + 7 = 7507秒。
# 想想这个方法有哪些参数， 返回值是什么类型。
# 8、写一个方法交换整型列表中两个指定下标元素的值。
# 想想这个方法有哪些参数，返回值是什么类型。
# 9、写一个方法计算整型列表中所有能被3整除元素的个
# 数。
#
# 想想这个方法有哪些参数，返回值是什么类型。
# 10、写一个方法将整型数字(int)
# 转换为格式化的字符串(string)，现要求如下： a.可以指定转换后[字符串的长度];
# b.当数字的长度不足指定的长度，让这个字符串右对齐， 指定[左边补的字符(char)];
# 例如，假设现在将指定的数字转换为固定长度为8的字符
# 串，如果长度不足，左边补
# '0'，那么27这个数字就会转换
# 为字符串
# "00000027"。
# 根据要求，想想这个方法有哪些参数，返回值是什么类
# 型。
# 11.
# 用方法实现找出一个int类型列表中最大值和最小值
# 12.
# 判断一个数是否是质数(素数)？该如何声明方法？ 13.
# 将指定的秒数转变为几小时几分几秒。
# 14.
# 使用Random类给一个数组的所有元素赋随机初值（不
# 重复）。
# 40 / 4815.
# 判断一个整型数组是否是对称的。
# 所谓对称就是第一
# 个元素等于最后一个元素，第二个元素等于倒数第二个元
# 素，依次类推，例如【7，3，1，3，7】就是对称的。
# 16.
# 打印一个元组的所有值。
# 17.
# 查找一个元组中某个值是否存在，如果存在返回这个
# 值的索引，否则返回 - 1。
# 18.
# 将一个列表反转过来，比如【2，3，1，4，7】转换为 【7，4，1，3，2】 19.
# 求一个列表的最大值。
# 20.
# 求一个列表的最小值。
# 21.
# 写一个方法，实现在列表中指定的的位置前插入一个
# 值。
# 22.
# 写一个方法，删除列表中指定位置的元素。
#  任务1
# def Lieprint(list1):
#     for i in list1:
#         print(i)
#     return
# Lieprint([1,2,3,5,6,7,8,9,'a','s'])

# 任务2
# def List_sum(list1):
#     _sum=0
#     for i in list1:
#         _sum+=i
#     return _sum
# print(List_sum([1,2,3,5,6,7,8,9]))

#任务3
# def Jibiao_sum(list1):
#     _sum = 0
#     for i in range(len(list1)):
#         if 1%2==1:
#             _sum+=list1[i]
#     return _sum
# print(Jibiao_sum([1, 2, 3, 5,5, 6, 7, 8, 9]))

#任务4
# def Jibiao_sum(list1):
#     _sum = 0
#     for i in range(len(list1)):
#         if i%2==0:
#             _sum+=list1[i]
#     return _sum
# print(Jibiao_sum([1, 2, 3, 5,5, 6, 7, 8, 9]))

#任务5
# def Two_sum(Numa=0,Numb=0):
#     return Numa+Numb
# print(Two_sum(35.8,50))
# 有两个默认形参，没有值输入时，默认输入为两个0，返回值是输入两个数的和

# 任务6
# def Shang_math(a,b):
#     if b==0:
#         print("输入错误，分母不能为0")
#         return
#     return a//b
# print(Shang_math(68,4))
#有两个形参，必须要有输入，否则报错。返回的是值

#方法7
# def Second(day=0,hour=0,min=0,sec=0):
#     second=((day*24+hour)*60+min)*60+sec
#     return second
# print(Second(3,6,24,25))
#有四个默认的形参，返回的是整型数据，返回的是值

#方法8
# def Exchange(listA,point1,point2):
#     if (point1 or point2) >len(listA)-1 or (point1 or point2)<0:
#         print("交换位点不存在")
#         return
#     temp=listA[point1]
#     listA[point1]=listA[point2]
#     listA[point2]=temp
#     return listA #可变类型，返回原来的指向，可以不用返回
# x=["a",3,5,"sdf",7,10]
# print(Exchange(x,3,5))
#有一个列表，两个索引，共三个形参，返回一个列表（的指向）

#任务9
# def Fun_list(listA):
#     count_=0
#     if type(listA)!=list:
#         print("输入错误，输入的必须为元素为整型的列表")
#         return
#     for i in range(len(listA)):
#         if type(listA[i])!=int:
#             print("输入错误，输入的必须为元素为整型的列表")
#             return
#         if listA[i]%3==0:
#             count_+=1
#     return count_
# print(Fun_list([0,6,8,-3,7,12]))
# 方法中有一个形参列表，返回一个整型
#任务10：
# def Int_str(Num=0,length=1):
#     Num=str(Num)
#     if len(Num)<length:
#         Num=Num.rjust(length,"0")
#     return Num
# print(Int_str(32,6))
#方法2
# def Int_str(Num=0,length=1):
#     Num=list(str(Num))
#     if len(Num)<length:
#         Num.insert(0,(length-len(Num))*"0")
#     Num="".join(Num)
#     print(Num)
#     return Num
# print(Int_str(32,6))
#有两个形参，第一个值给整型值，第二个是长度，返回一个字符串
#任务11
# def Max_min(listA):
#     """用于整型列表中，最大、最小值的获取"""
#     return [max(listA),min(listA)]
# print(Max_min([22,56,89,0,12,-6,101,6,2]))
#任务12
# def Isprima(x):
#     """输入的值必须是大于0的整数"""
#     if x>=2:
#         for i in range(2,x):
#             if x%i==0:
#                 return False
#         return True
# print(Isprima(100))
#任务13
# def time_hms(sec=0):
#     hour=sec//3600
#     min=sec%3600//60
#     second=sec%60
#     return {hour:"小时",min:"分",second:"秒"}
##return "%s小时%s分钟%s秒"%(hour,min,second)
# print(time_hms(100))

#任务14
# def randint_list(lenth):
#     temp=[]
#     import random
#     while True:
#         t=random.randint(1,lenth)
#         if t not in temp:
#             temp.append(t)
#         if len(temp)==lenth:
#             return temp
# listA=randint_list(20)
# print(listA)

#任务15
# def Isduichen(listA):
#     for i in range(len(listA)//2):
#         if listA[i]!=listA[len(listA)-i-1]:
#             return False
#     return True
# listA=[1,3,5,3,1]
# print(Isduichen(listA))

#任务16
# def Prtuple(Tuple1):
#     for i in Tuple1:
#         print(i,end=" ")
# tupleA=(1,3,5,'a','gh')
# Prtuple(tupleA)

#任务17
# def Istuple(X,TupleA):
#     for i in range(len(TupleA)):
#         if TupleA[i]==X:
#             return i
#     return -1
# tuple1=(1,4,6,9,"a")
# # a=Istuple("b",tupleA)
# b=lambda x,tupleA:-1 if x not in tupleA else tupleA.index(x)
# b(0,tuple1)
# print(b)

#任务18
# def Exduichen(listA):
#     for i in range(len(listA)//2):
#         temp=listA[i]
#         listA[i]=listA[len(listA)-i-1]
#         listA[len(listA)-i-1]=temp
#         # return listA  没有返回时，虽然返回None,但listB已经交换，
# listB=[1,3,5,3,1,8,15,23]
# Exduichen(listB)
# print(listB)

#
#
# import time
# x=input("请输入时间（如2018-3-25）")
# y=time.strptime(x,"%Y-%m-%d")
# print(type(y),y,"今天是%s"%(y[6]+1))
# import time
# import sys
# import os
# while True:
#     t=time.localtime()
#     y=time.strftime("%Y{}%m{}%d{} {}%w %H{}%M{}%S{}",t).format("年","月","日","周","时","分","秒")
#     print(y)
#     time.sleep(1)
#     os.system("cls")
# dictA={1:12,2:23,4:11,9:"l","a":23,"p":5}
# dictA[15]=99
# # a=dictA.popitem()
# a=dictA.pop(1)
# print(dictA,a)
#任务19，20
# def Minmax(ListA):
#     """求出一个可迭代对象（数字或字母的最大最小值）"""
#     temp1=0
#     temp2=0
#     for i in ListA:
#         if i>temp1:
#             temp1=i
#         if i<temp2:
#             temp2= i
#     return{"min":temp1,"max":temp2}
# list1=[1,3,6,0,12,67,-9,3.5]
# a=Minmax(list1)
# print(a)
#任务21
# def Addlist(I,Ai,ListA):
#     """将Ai插入到列表ListA的第I位置"""
#     temp=0
#     for i in range(I,len(ListA)):
#         temp=ListA[i]
#         ListA[i]=Ai
#         Ai=temp
#     ListA+=[Ai]
#     return ListA
# list1=[2,5,7,9,0,"a","bn"]
# print(list1,id(list1))
# b=Addlist(3,"莉莉",list1)
# print(b,id(b),list1,id(list1))
# #扩展，+= 与=+的不同
# list1=[2,5,7,9,0,"a","bn"]
# print(list1,id(list1))
# list2+=[22]#list2=list2+[22]
# # list1.pop(2)
# print(list1,id(list1))
# # print(list1,id(list1),list2,id(list2))

#任务22
# def Dellist(I,ListA):
#     """删除第I位置列表ListA的元素"""
#     temp=0
#     for i in range(I,len(ListA)-1):
#         temp=ListA[i]
#         ListA[i]=ListA[i+1]
#         ListA[i+1]=temp
#     ListA.pop()
#     return ListA
# list1=[2,5,7,9,0,"a","bn"]
# print(list1,id(list1))
# b=Dellist(3,list1)
# print(b,id(b),list1,id(list1))

#任务23
def Rannum(down=1,up=10):
    import random
    t=random.randint(down,up)
    return t
def Inputnum(down=1,up=10):
    t=input("请输入一个数字(1-10)：")
    while t.isdigit()==False or (0>int(t) or int(t)>10):
        t =input("输入错误，请重新输入一个数字(1-10)：")
    return int(t)
r=Rannum(1,10)
d=0
for s in range(5):
    a=Inputnum()
    print(r)
    if a>r:
        print("偏大")
    elif a<r:
        print("偏小")
    else:
        d=1
        if s==0:
            print("真厉害，第一次就猜对了")
        elif s==4:
            print("猜对了,这个游戏不适合你")
        else:
            print("猜对了")
        break
    s+=1
if d==0:
    print("垃圾了,这个游戏不适合你")