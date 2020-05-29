# print("hello world!")
# print("I am Yaogang Chen")
# name = "Yaogang"
# _age = "24"
# age = 24
# print("my name is:" + name)
# print("my age is:" + _age)
# print(name+ " " +_age)
# print(name[-1:])
# print("my name is %s, my age is %s" %(name,str(age)))
# print("my name is {0}, my age is {1}". format(name,age).capitalize())
# print(name.encode(encoding="UTF-8"))
# print(name.startswith("Y"))
# print(name.find("Y"))  #0代表成功查到，-1代表没有查到

# a = 1256
# print(a)
# a = True
# b = False
# c=1
# print(int(a)) 
# print(type(a))
# print(type(c))
# d=int(a)+c
# print(d)


# texthosts = ["aa","bb","cc"]  #list
# anothertexthosts =["11","22"]
# print(texthosts[2])  #获取元素，注意是第三个元素cc
# print(len(texthosts))  #显示长度 3
# texthosts.append("dd") #末尾追加
# print(texthosts)
# texthosts.extend(anothertexthosts) #扩展
# print(texthosts)
# print(texthosts.index("bb")) #显示索引 1
# texthosts.insert(3,"ee") #第4个元素插入ee
# print(texthosts)
# texthosts.remove("11") #删除元素
# print(texthosts)
# texthosts.reverse() #反向列表
# print(texthosts)

# myinfo = {"name":"Yaogang Chen","age":24}
# print(myinfo)
# print(myinfo["name"])

# #print(myinfo.clear()) #清空字典
# data1 = myinfo.copy() #复制独立的副本
# print(data1)
# print(myinfo.get("age")) #获取key的值
# print(myinfo.items()) #将key和value的组合放到列表中
# #输出为 dict_items([('name', 'Yaogang Chen'), ('age', 24)])
# print(myinfo.keys())
# print(myinfo.values())  #别忘了加s
# myinfo.pop("name") #删除
# print(myinfo)

# import json

# info = {"name":"Kobe","age":24}
# jsonInfo = json.dumps(info) #dict -> json
# print(jsonInfo)
# print(type(jsonInfo))

# dictInfo = json.loads(jsonInfo) #json -> dict
# print(dictInfo)
# print(type(dictInfo))

# numberOne = 10
# numberTwo = 2
# print("numberOne ** numberTwo = %d" %(numberOne ** numberTwo))
# print("numberOne % numberTwo = {0}".format(numberOne % numberTwo))

# A = True
# B = False
# print("A and B ---> {0}".format(A and B))

# score = 60
# students = {"王世杰":40,"韦涛":60,"王家能":80,"陈垚钢":100}
# stu = students["王世杰"]
# print(stu)
# print(type(stu))

# if stu >= 80:
#     print("优秀")
# elif stu >= 60:
#     print("及格")
# else:
#     print("不及格")


# for 循环

# from numpy import *
# import numpy as np
# sum = 0
# x = np.array([1,-1])
# x1 = x.reshape(-1,1)
# P = np.matrix([[1,0],[0,0.5]])
# A = np.matrix([[0.5,0.5],[0,0.8]])
# At = A.T



# for i in range(1,100):
#      sum += (x*P*x1)
#      x2 = A*x1
#      x1 = x2
#      x = x2.T
# print(sum)

from collections import Iterable

num = list(range(1,10))
print(isinstance(num,Iterable))


names = ['a','b','c']

for i,value in enumerate(names):
    print(i,value)

numlist = []
for x in range(5):
    numlist.append(x)
print(numlist)

print([x for x in range(5)])





