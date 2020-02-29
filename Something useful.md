## Index

- [join function](Something useful.md#join-function)
- [split function](Something useful.md#split-function)
- [upper function](Something useful.md#upper-function)
- [get square roots](Something useful.md#get-square-roots)
- [get the integer](Something useful.md#get-the-integer)
- [delete dedicated elements](Something useful.md#delete-dedicated-elements)
- [sort() & sorted()](Something useful.md#sort()-&-sorted())
  - [sorted() with operator module](Something useful.md#sorted()-with-operator-module)
  - [attrgetter and itemgetter](Something useful.md#attrgetter-and-itemgetter)
- [Transfer among binary, decimal, octonary and hexadecimal](Something useful.md#Transfer-among-binary,-decimal,-octonary-and-hexadecimal)
- [Check if str is alphabet or digit (return T/F)](Something useful.md#Check-if-str-is-alphabet-or-digit-(return-T/F))
- [Check if str is upper, lower or title (return T/F)](Something useful.md#Check-if-str-is-upper,-lower-or-title-(return-T/F))

## join function
```
comma = ','
print(comma.join(numbers))
```
## split function
```
comma = ','
nlist = numbers.split(comma)
```
## upper function

`print(String.upper())`
## get square roots
```
import math
math.sqrt()
```
## get the integer
```
int() the smaller integer
round() the nearest integer

import math
math.ceil() the larger integer
```
## delete dedicated elements

`set()`
## sort() & sorted()

```
list.sort()   #sort() can only used on list
sorted(list)   #sorted can used on anything iterable
```
### sorted() with operator module

```
from operator import itemgetter
a = [[1, 2, 3], [3, 5, 6], [2, 4, 5]]
print("sort the list according to the first element:", end='')
print(sorted(a, key=itemgetter(0)))  
print("sort the list according to the second element:", end='')
print(sorted(a, key=itemgetter(1)))  
print("sort the list according to the third element:", end='')
print(sorted(a, key=itemgetter(2)))  
```
```
from operator import attrgetter
class Teacher():    
	def __init__(self, name, salary, age):        
		self.name = name        
		self.age  = age        
		self.salary = salary    
	def __repr__(self):        
		return  repr((self.name,self.age,self.salary))

teachers = [Teacher("A",1200,30),Teacher("B",1200,31),Teacher("C",1300,30)]
print(sorted(teachers,key=attrgetter("age")))  # sort according to age
print(sorted(teachers,key=attrgetter("salary","age"))) # sort according to salary and age
```
### attrgetter and itemgetter

#### attrgetter

```
from operator import attrgetter, itemgetter
class Teacher():    
	def __init__(self, name, salary, age):        
		self.name = name        
		self.age  = age        
		self.salary = salary    
	def __repr__(self):        
		return  repr((self.name,self.age,self.salary))

teachers = [Teacher("A",1200,30),Teacher("B",1200,31),Teacher("C",1300,30)]
print(sorted(teachers,key=attrgetter("age")))  # Sorted by acsending order by age
print(sorted(teachers,key=attrgetter("salary","age"))) # Sorted by acsending order first by salary, then by age.
```
#### itemgetter 

```
#itemgetter will return a tuple
from operator import itemgetter
data = [('老王', 18, 175, 75), ('阿汤哥', 15, 165, 70), ('罗宾森', 23, 180, 100), ('小风', 10, 171, 60), ('黄佬', 20, 175, 65)] 
get_c_d = itemgetter(2, 3)   #Get elements of tuples by index
for value in data:
	print(get_c_d(value))
	print("-------------------------------------")
for value in sorted(data, key=itemgetter(2, 3)):  #Sorted by acsending order by the value got by itemgetter
	print(value)
	print("-------------------------------------")
```
## Transfer among binary, decimal, octonary and hexadecimal

| :smile: | binary | octonary | decimal | hexadecimal |
|:---------:|:---------:|:----------:|:----------:|:------:|
|binary|-|bin(int(x,8))|bin(int(x,10))|bin(int(x,16))|
|octonary|oct(int(x,2))|-|oct(int(x,10))|oct(int(x,16))|
|decimal|int(x,2)|int(x,8)|-|int(x,16)|
|hexadecimal|hex(int(x,2))|hex(int(x,8))|hex(int(x,10))|-|

## Check if str is alphabet or digit (return T/F)
```
str.isdigit()
str.isalpha()
str.isalnum()  #combination of alpha &number
```
## Check if str is upper, lower or title (return T/F)
```
str.isupper()
str.islower()
str.istitle()  #check if the first letter is upper and the rest is lower
```
