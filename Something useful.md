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
## The re module

```
re.search([keyword], [object string])
e.g.: 
>>> re.search("com","www.baidu.com")

<_sre.SRE_Match object; span=(10, 13), match='com'>

>>> re.search("com","www.baidu.com.com.com")

<_sre.SRE_Match object; span=(10, 13), match='com'> # only return the first matched position
```
