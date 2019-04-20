#切片  [起始：结束：步长] 左闭右开
city = 'beijing'
print(city[0:3:2])
#bi  每两个取1个

newCity = city.split('i')
print(newCity)
print(type(newCity))
# ['be','j','ng']   <class 'list'>

newCity2 = city.replace('i','a')
print(newCity2)
#beajang

city2 = '  beijing  '
print(city2.stirp())
#beijing

newCity3 = city.upper()
print(newCity3)
print(newCity3.lower())
#BEIJING  beijing

print(len(city))
#7

#布尔型
#'true'  'false'

#列表  ['a',5,25.5]  数据可具备不同数据类型  增删改查
studentList = ['aa','bb','cc']
studentList.append('dd')
studentList.extend(['ee'])
studentList.insert(2,'qq')
print(studentList)
#['aa','bb','cc','dd']  ['aa','bb','cc','ee'] ['aa','bb','qq','cc']

studentList.pop()
del(studentList[0])
studentList.remove('bb')
#['aa','bb'] ['bb','cc'] ['aa','cc']

studentList[0] = 'qq'
#['qq','bb','cc']

#in(存在)  true/false
#not in(不存在) 

#python列表表达式
'''
从一个数据序列构建一个新的数据序列的方式
推导式(comprehensions)是python的一种独有特性
基本语法：[表达式for变量in列表if条件]
'''
#筛选长度大于3的字符串列表
names = ['Jerry','Bob','Tom','Smith']
select_name = [names.upper() for name in names if len(name)>3]
print(select_name)
#['JERRY','SMITH']