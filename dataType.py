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