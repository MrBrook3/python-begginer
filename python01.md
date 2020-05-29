### Hello world部分
```python
print("hello world!")
print("I am Yaogang Chen")
name = "Yaogang"
_age = "24"
age = 24
print("my name is:" + name)
print("my age is:" + _age)
print(name+ " " +_age)
print(name[-1:])
print("my name is %s, my age is %s" %(name,str(age)))
print("my name is {0}, my age is {1}". format(name,age).capitalize())
print(name.encode(encoding="UTF-8"))
print(name.startswith("Y"))
print(name.find("Y"))  #0代表成功查到，-1代表没有查到

a = 1256
print(a)
a = True
b = False
c=1
print(int(a)) 
print(type(a))
print(type(c))
d=int(a)+c
print(d)
```
注：
- python第一个元素是第0；
- [1:5]表示第二2个到第5个元素，取不到第6个；
- print不能直接运算数据类型:
```python
texthosts = ["aa","bb","cc"]
k = 1
p = 2
print("k+P="+k+p)
会报错
但
print(k+p)是可以的
```
### list列表 及 内置函数
列表是方括号[]
```python
texthosts = ["aa","bb","cc"]  #list
anothertexthosts =["11","22"]
print(texthosts[2])  #获取元素，注意是第三个元素cc
print(len(texthosts))  #显示长度 3
texthosts.append("dd") #末尾追加
print(texthosts)
texthosts.extend(anothertexthosts) #扩展
print(texthosts)
print(texthosts.index("bb")) #显示索引 1
texthosts.insert(3,"ee") #第4个元素插入ee
print(texthosts)
texthosts.remove("11") #删除元素
print(texthosts)
texthosts.reverse() #反向列表
print(texthosts)
```
### 元组类型
- 元组用圆括号()
- 元组中的元素是不可修改的
### 字典类型
- 字典用大括号 {}，字典是key和value的组会
  ```python
  myinfo = {"name":"Yaogang Chen","age":24}
  #前面name、age称为key（键），不可改变；后面Yaogang Chen和24称为value（值），可以改变；
  print(myinfo)
  print(myinfo["name"])

  ```

- 内置函数
  ``` python
  #print(myinfo.clear()) #清空字典
   data1 = myinfo.copy() #复制独立的副本
   print(data1)
   print(myinfo.get("age")) #获取key的值
   print(myinfo.items()) #将key和value的组合放到列表中
   #输出为 dict_items([('name', 'Yaogang Chen'), ('age', 24)])
   print(myinfo.keys())
   print(myinfo.values())  #别忘了加s
   myinfo.pop("name") #删除
   print(myinfo)
   ```

   实战：dict格式和json格式相互转化
   ```python
    import json

   info = {"name":"Kobe","age":24}
   jsonInfo = json.dumps(info) #dict -> json
   print(jsonInfo)
   print(type(jsonInfo))
 
   dictInfo = json.loads(jsonInfo) #json -> dict
   print(dictInfo)
   print(type(dictInfo))
   ```

### python 运算符
####算数运算符
  - 加减乘除
  - 模运算 a % b
  - 幂运算 a ** b
  - 整除运算 a // b
  - 两种方法
```python
numberOne = 10
numberTwo = 2
print("numberOne ** numberTwo = %d" %(numberOne ** numberTwo))
print("numberOne % numberTwo = {0}".format(numberOne % numberTwo))
# %d没有. 且需要区分变量类型；format要加.
```
- 等于 ==
- 不等于 !=
- += *= /= %= **= //=
 
 #### 逻辑运算符
 and or not
 ```python
 A = True
B = False
print("A and B ---> {0}".format(A and B))

 ```
  
#### if条件语句
```python
score = 60
students = {"王世杰":40,"韦涛":60,"王家能":80,"陈垚钢":100}
stu = students["王世杰"]
print(stu)
print(type(stu))

if stu >= 80:  #在判断条件之后要加：
    print("优秀")  #注意缩进、可以嵌套
elif stu >= 60:
    print("及格")
else:
    print("不及格")

```

#### 循环语句
- for循环
  ```
  for 变量名 in 序列
      todo
  ```
```python
#实现 系统x(k+1)=Ax(k)在二次型x'Px的100步求和

from numpy import *
import numpy as np
sum = 0
x = np.array([1,-1])
x1 = x.reshape(-1,1)
P = np.matrix([[1,0],[0,0.5]])
A = np.matrix([[0.5,0.5],[0,0.8]])
At = A.T

for i in range(1,100):
     sum += (x*P*x1)
     x2 = A*x1
     x1 = x2
     x = x2.T
print(sum)
```
while循环 continue、break语句
- continue:跳出当前循环，继续下次循环；
- break：跳出整个循环

#### 迭代器
- iterable
  ```python
  from collections import Iterable

  num = list(range(1,10))
  print(isinstance(num,Iterable))
  ```
- enumerate
  ```python
  names = ['a','b','c']

  for i,value in enumerate(names):
  print(i,value)
  ```
  ```python
  0 a
  1 b
  2 c
  ```
- 列表推导式
  两种写法
  ```python
  numlist = []
  for x in range(5):
      numlist.append(x)
   print(numlist)

   print([x for x in range(5)])

   [0, 1, 2, 3, 4]
   [0, 1, 2, 3, 4]
  ```

### 函数
#### 函数的定义与调用

```
def Print_msg():
print("Hello world!")
```
```python
def Print_msg():
    print("Helle world!")
Print_msg()
```



#### 函数编写规范
- 文档字符串
  ```python
  def print_msg():
    """
    This is a function!
    print hello world!
    """

    print("Helle world!")
    print_msg()
    ```
    获取文档字符串
    ```
    print(print_msg.__doc__)
    ```
  

- 函数注释

#### 函数参数
- 位置参数
- 默认参数 
- 关键字参数 
可以防止两个变量数量不一致的情况
```python
def print_mes(*name,**num):
    print(name)
    print(num)

print_mes("Kobe","Lebron","Stephen",numKobe1=8,numKobe2=24,numLebron=23,numStephen=30)
```
```
('Kobe', 'Lebron', 'Stephen')
{'numKobe1': 8, 'numKobe2': 24, 'numLebron': 23, 'numStephen': 30}
```

```python
#小实践：成绩查询

scores = {"xiaoming":68,"xiaohong":92,"lanlan":85,"aqiang":45}

def select(name):  #name本身就表示字符串
    if name in scores.keys():
        print("您的成绩正在查询--->{0}".format(name))
        print("{0}的成绩为--->{1}".format(name,scores[name]))
        if scores[name] >=80:
            print("成绩等级：优秀")
        elif scores[name] >= 60:
            print("成绩等级：及格")
        else: 
            print("成绩等级：不及格")
    else:
        print("未查询到您的成绩")

select("xiaohong")
```
```
您的成绩正在查询--->xiaohong
xiaohong的成绩为--->92
成绩等级：优秀
```

### 异常处理
- 异常处理
```python
try:
    int("x25")
except ValueError:
    print("语法错误")
print("hello")

```
- 抛出异常 raise
```python
a = "1"
b = "2"

if a < b:
    raise Exception("error")
```
- 自定义异常

### 面向对象编程

```python
class car:
    brand = "BWM"
    color = "black"

    def run(self,s):
        print("当前车速为:",s,"km/h")
    
test = car()

print(test.brand)
test.color = "blue"  #修改class
print(test.color)

test.run(60)
```

### requests库
- 安装：pip3 install requests
- method:必填 POST
- url：必填 服务器地址
params:可选 请求参数
data：可选，主体部分
json
cookies：可选
file：文件
auth：身份验证
timeout：超时时间

```python
# requests库
import requests
url = "http://www.baidu.com"
response = requests.get(url)   #请求方法：get,head,put,post
print(response)  
print(response.status_code)
print(response.encoding)
print(response.text)
print(response.headers)

```






