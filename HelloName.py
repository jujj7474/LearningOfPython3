#Hello world
name = input('please input your name:')
print('Hello,',name)

#变量
myAge = 20  # 变量 赋值符 值

#关键字
'''
import keyword
keyword.kwlist
'''

#数据类型    充分利用内存
age = 20
booler = "False"
print(type(age))
print(type(booler))

#字符串输入输出
username = input('请输入用户名：')
password = input('请输入密码：')
print('用户名：',username)
print('密码:',password)

#print absolute value of an integer:   注释(解释器会忽略)
a = 100
if a >= 0:       # ‘:’形成代码块，默认4空格缩进
  print(a)       # 缩进：复制粘贴功能失效
else:            # python大小写敏感
  print(-a)
