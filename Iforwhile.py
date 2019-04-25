#控制流 判断if 循环for、while  
if 10>5:
print('10>5)'

lang = input('请选择你所输入的语言，es、cn或其他：')
if lang == 'es':
	print('Hi')
elif lang == 'cn':
	print('您好')
else:
	print('Hello')

#for变量in列表或者字符串等，满足则执行
city = 'beijing'
for i in city:
	print(i)

#while条件满足：执行代码
num = 0
while num<5:
	print('num<5')
	num = num +5

#break结束循环 continue结束本次，开始下一循环
list1 = [1,2,3,4]
for i in list1:
	if i == 3:
		break
	print(i)

i=0
while i<5:
	i = i+1
	print('---')
	if i==3:
		continue
	print(i)

#运算符  比较 赋值  逻辑 成员 身份 