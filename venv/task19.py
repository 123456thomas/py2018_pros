# 9. 编程输出所有的三位水仙花数 水仙花数:各位数字的立 方数相加等于该数本身  例如 153  1*1*1+5*5*5 +3*3*3=153  153就是一个三位水仙花数
# 10.为哈希表追加不重复的100个值，且每个值都是1-100 之间的随机数，问哪个数字重复的次数最多，重复了多少 次？
# 11.假定书籍的种类有5种，设计何种的数据结构可以达到 快速查询某类所有书籍的功能（提示：用 Dictionary<K,V>）
#任务9
# listA=[]
# for i in range(100,1000):
#     if (i//100)**3+(i%10)**3+(i//10%10)**3==i:
#         listA.append(i)
# print(listA)

#任务10
# import random
# listA=list("asdfghjklb")
# listB=[]
# for i in range(len(listA)):
#     temp =[]
#     listB.append(temp)
#     for j in range(1,21):
#         listB[i].append(random.randint(1,20))
# dictA=dict(zip(listA,listB))
# print(dictA)
# listZ=[]
# for i in range(len(listB)):
#     listZ+=listB[i]
# max_={"shuzi":0,"cishu":0}
# for i in range(1,21):
#     if listZ.count(i)>max_["cishu"]:
#         max_["shuzi"]=i
#         max_["cishu"] =listZ.count(i)
#     print(i,":",listZ.count(i),end=",")
# print(max_)




# #任务11
# dictB={"文学类":{"现代文学类":["教父|作者1","吸血鬼日记|作者1"],"科幻类":["三体|作者1","银河帝国|作者1"]},\
#        "工程技术类":{"化工类":["化工原理|","流体力学"],"材料":["纳米材料|","高分子材料|"]},\
#        "艺术类":{"音乐":["钢琴","小提琴","口风琴"],"线谱":["五线谱","六线谱"],"戏剧":["豫剧","京剧"]},\
#        "历史":{"外国历史":["德国历史","俄罗斯历史","东南亚历史"],"中国历史":["先秦史","近代史"],"四大发明":["指南针","纸币"]},\
#        "世界战争":{"一战":["一战背景","一战态势","一战影响"],"二战英雄":["斯大林","希特勒"],"二战":["二战背景","二战态势","二战影响"]}}
# print(dictB)
# #快速查找
# x=input("请选择书的类别文学类（工程技术类，艺术类，历史世界战争）：")
# x1=input("请选择书的%s:"%dictB[x])
# print(dictB[x][x1])
# for i in dictB:
#     print(i)
# # for i in dictB[x].get(x1):
# print(dictB[x].get(x1))
# # print(dictB[x][x1])



# a=b=12
# print(id(a),id(b),id(12))
# a=4
# print(id(a),id(b))
# print(a,b)

# a=b="asdfg"
# print(id(a),id(b),id("asdfg"))
# a="sdfg"
# print(id(a),id(b))
# print(a,b)
# listA=[1,3,5,6]
# listB=listA
# print(id(listA),id(listB))
# print(id(listA),id([1,3,5,6]))
# listA[0]='a'
# print(id(listA),id(listB))

# setA={1,3,5,6}
# setB=setA
# print(id(setA),id(setB))
# print(id(setA),id({1,3,5,6}))
# setA.add("a")
# print(setA,setB)
# print(id(setA),id(setB))

# tupleA=(1,2,3,4,5,6)
# tupleB=tupleA
# print(id(tupleA),id(tupleB))
# print(id(tupleA),id((1,2,3,4,5,6)))
# listA=list(tupleA)
# listA[1]=12
# tupleA=tuple(listA)
# print(id(tupleA),id(tupleB))
# print(tupleA,tupleB)