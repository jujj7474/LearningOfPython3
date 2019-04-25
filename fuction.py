#函数 def 标识符+() 调用函数名() 
def addnum(a,b):
	print(a+b)

addnum(1,2)

#参数 定义函数时让函数接受数据 形参 定义时()  实参 调用时()
#函数类型：  有无参数+有无返回值 4种

#无参有返回值
def getTemperature():
	return 25

T = getTemperature()
print('当前的温度为：%d度'%T)

#有参有返回值
def calculateNum(num):
	result = 0
	i = 1
	while i<= num:
		result += i
		i += 1
	return result  #只有return才能返回值

result = calculateNum(100)
print('1-100的累加和为:%d'%result)