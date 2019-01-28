#点名程序
# nameku=input("请输入名字，以‘，’隔开：")
# lista=nameku.split("，")
# import random
# listA=[]
# for i in lista:
#     temp=[]
#     temp.append(i)
#     temp.append(0)
#     listA.append(temp)
# print(listA)
# while True:
#     t = random.randint(0,len(listA) - 1)
#     listA[t][1]+=1
#     print(listA)
#     if input()=="q":
#         break
#     input()
# for i in range(len(listA)):
#     for j in range(len(listA)-i-1):
#         if listA[j][1]<listA[j+1][1]:
#             temp=listA[j][1]
#             listA[j][1]=listA[j+1][1]
#             listA[j+1][1]=temp
# print(listA)



# 数字从小到大排序（选择排序）选择排序（先确定最小的（前面的，在确定其次小的））
# listA=[1,5,7,9,23,6,0]
# for i in range(len(listA)-1):
#     for j in range(i+1,len(listA)):
#         if listA[j]<listA[i]:
#             temp=listA[j]
#             listA[j]=listA[i]
#             listA[i]=temp
# print(listA)
#数字从小到大排序（冒泡排序先确定最最大的（后面的，在确定其次大的）
# listA=[1,5,7,9,23,6,0]
# for i in range(len(listA)-1):
#     for j in range(0,len(listA)-1-i):
#         if listA[j+1]<listA[j]:
#             temp = listA[j]
#             listA[j] = listA[j+1]
#             listA[j+1] = temp
# print(listA)
#纯字母排序不区分大小写
# listA=['a','z','S','t','b','p','e','s']
# for i in range(len(listA)-1):
#     for j in range(i+1,len(listA)):
#         if ord(listA[j].upper())<ord(listA[i].upper()):
#             temp=listA[j]
#             listA[j]=listA[i]
#             listA[i]=temp
# print(listA)

#纯数字字母排序不区分大小写(制表符不能判断，空格可以)
# listA=['a',3,'z','S',12,'t',0,'b',9,'p',' ','e',84,'s']
# for i in range(len(listA)-1):
#     for j in range(i+1,len(listA)):
#         if type(listA[j])==str and type(listA[i])==str:
#             if ord(listA[j].upper())<ord(listA[i].upper()):
#                 temp=listA[j]
#                 listA[j]=listA[i]
#                 listA[i]=temp
#         elif type(listA[j])==str:
#             if ord(listA[j].upper())<listA[i]:
#                 temp=listA[j]
#                 listA[j]=listA[i]
#                 listA[i]=temp
#         elif type(listA[i])==str:
#             if ord(listA[i].upper())>listA[j]:
#                 temp=listA[j]
#                 listA[j]=listA[i]
#                 listA[i]=temp
#         else:
#             if listA[j]<listA[i]:
#                 temp=listA[j]
#                 listA[j]=listA[i]
#                 listA[i]=temp
# print(listA)
# print(listA)
# print(type("a")==str)
# print(type("a"))
# print("str" in str(type("a")))


# listA=[1,1,2,4,5,6,23,51,0]
# listA.pop(3)
# listA.remove(51)
# listA.insert(2,"a")
# listA.append("x")
# listA.extend([11,22,33])
# print(listA)

setA={1,3,"d",'j',200,"t"}
setB={1,200,"d","j",3,20,"p"}
print(setB.difference(setA))

,"工程技术类":{{"化工类":["化工原理|","流体力学"]},{"材料":["纳米材料|","高分子材料|"]}},
       "艺术类":{{"音乐":["钢琴","小提琴","口风琴"],"线谱":["五线谱","六线谱"]},{"戏剧":["豫剧","京剧"]}},"历史":{{"外国历史":["德国历史","俄罗斯历史","东南亚历史"],"中国历史":["先秦史","近代史"]},{"四大发明":["指南针","纸币"]}},
       "世界战争":{{"一战":["一战背景","一战态势","一战影响"],"二战英雄":["斯大林","希特勒"]},{"二战":["二战背景","二战态势","二战影响"]}}