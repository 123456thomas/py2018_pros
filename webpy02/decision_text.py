# 决策树实例，用juepyter运行

# 1.读取数据鸢尾花的数据
from sklearn.datasets import load_iris
iris = load_iris()

# 查看数据
print(iris.DESC)

# 2.建立模型
from sklearn import tree

