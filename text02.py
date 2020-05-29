# #函数

# def print_msg(x:"first number"=0,y:"second number"=0):
#     """
#     This is a function!
#     print hello world!
#     """

#     print("Helle world!")
#     print("x + y = {0}".format(x+y))
# print_msg(1,5)
# print(print_msg.__annotations__) #显示变量的注解
# print(print_msg.__class__)
# print(print_msg.__doc__)


# #关键字参数

# def print_mes(*name,**num):
#     print(name)
#     print(num)

# print_mes("Kobe","Lebron","Stephen",numKobe1=8,numKobe2=24,numLebron=23,numStephen=30)


#小实践：成绩查询

# scores = {"xiaoming":68,"xiaohong":92,"lanlan":85,"aqiang":45}

# def select(name):
#     if name in scores.keys():
#         print("您的成绩正在查询--->{0}".format(name))
#         print("{0}的成绩为--->{1}".format(name,scores[name]))
#         if scores[name] >=80:
#             print("成绩等级：优秀")
#         elif scores[name] >= 60:
#             print("成绩等级：及格")
#         else: 
#             print("成绩等级：不及格")
#     else:
#         print("未查询到您的成绩")

# select("aqiang") 


try:
    int("x25")
except ValueError:
    print("语法错误")
print("hello")


a = "1"
b = "2"

if a < b:
    raise Exception("error")







