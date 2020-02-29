from operator import attrgetter, itemgetter
class Teacher():    
	def __init__(self, name, salary, age):        
		self.name = name        
		self.age  = age        
		self.salary = salary    
	def __repr__(self):        
		return  repr((self.name,self.age,self.salary))

teachers = [Teacher("A",1200,30),Teacher("B",1200,31),Teacher("C",1300,30)]
print(sorted(teachers,key=attrgetter("age")))  # 根据age排序
print(sorted(teachers,key=attrgetter("salary","age"))) # 根据salary和age排序
print('**********************')

data = [('老王', 18, 175, 75), ('阿汤哥', 15, 165, 70), ('罗宾森', 23, 180, 100), ('小风', 10, 171, 60), ('黄佬', 20, 175, 65)] 
"""
itemgetter，它构建的函数会返回提取的值构成的元组
"""
get_c_d = itemgetter(2, 3)
for value in data:
	print(get_c_d(value))
	print("-------------------------------------")
	# 表示根据 C,D 来进行排序
for value in sorted(data, key=itemgetter(2, 3)):
	print(value)
	print("-------------------------------------")