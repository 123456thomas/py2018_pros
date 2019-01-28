# 1.两个列表进行合并操作 2.使用列表判断一个列表是否在另外一个列表中 3.列表的反转
# 4.列表的排序14/48
# 5.实现对列表的增删改查功能
# 6.如何将0-10随机存入列表中
# 7.求出元组(90,34,-23,18,12)中的最大值和最小值
# 8. 针对列表[90,34,-23,18,12]
# 从小到大进行排序，然后 输出排序后结果

#任务1
# list1=[1,4,6,0,'as']
# list2=[12,46,'0a','as']
# list1.extend(list2)
# print(list1)

#任务2
# list1=[1,4,6,0,"as"]
# list2=[3,6,7,8,0,1,'as','h',4]
# s=0
# for i in list1:
#     if i in list2:
#         s+=1
# if s==len(list1):
#     print("%s在%s中"%(list1,list2))

#任务3
# list2=[3,6,7,8,0,1,'as','h',4]
# list2.reverse()
# print(list2)
# #print(list2[::-1])

#任务4
# listA=[1,4,56,-9,'a','g','A']
# for i in range(len(listA)):
#     if type(listA[i])!=int:
#         m=listA[i]
#         listA[i] =ord(m)
# listA.sort()
# print(listA)
#任务5
# list2=[3,6,7,'as',8,0,1,'as','h',4]
# list1=list2[:]
# list3=list2[:]
# list4=list2[:]
# list2.append("Guten Morgen")
# list1.insert(2,"me")
# list3.pop()
# list4[4]='you'
# print(list2,list1,list3,list4)
# for i in range(len(list2)):
#     if "as"==list2[i]:
#         print("as在list2位置是：",i,end=",")

#任务6
# import random
# listA=[]
# while True:
#     t=random.randint(0,10)
#     if t not in listA:
#         listA+=[t]
#     if len(listA)==10:
#         print(listA)
#         break

#任务7
# tupleA=(90,34,-23,18,12)
# print("元组的最大值是%s,最小值是%s"%(max(tupleA),min(tupleA)))

#任务8
# strA=[90,34,-23,18,12]
# strA.sort()
# print(strA)

#随即点名
listku=["李梦醒","杜月飞","Tim","Bastian","Sakura","Thomas","Rita"]
import random
while True:
    t=random.randint(0,len(listku)-1)
    print(listku[t])
    if input()!="":
        break