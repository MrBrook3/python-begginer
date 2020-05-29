#面向对象编程

# class car:
#     brand = "BWM"
#     color = "black"

#     def run(self,s):
#         print("当前车速为:",s,"km/h")
    
# test = car()

# print(test.brand)
# test.color = "blue"  #修改class
# print(test.color)

# test.run(60)



# requests库
import requests
url = "http://www.baidu.com"
response = requests.get(url)   #请求方法：get,head,put,post
print(response)  
print(response.status_code)
print(response.encoding)
print(response.text)
print(response.headers)














