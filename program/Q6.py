'''
Question:
Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
Example
Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24
'''
import math
C = 50
H = 30
comma = ','
def getD():
    S = input('Please input a comma separated input sequence of D:')
    result = S.split(comma)
    return(result)
def formula(D):
    Q = []
    for i in range(len(D)):
        result = round(math.sqrt((2 * C * int(D[i])) / H))
        Q.append(str(result))
    return Q
D = getD()
Q = formula(D)
print(comma.join(Q))

'''
Solution:
#!/usr/bin/env python
import math
c=50
h=30
value = []
items=[x for x in raw_input().split(',')]
for d in items:
    value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))

print ','.join(value)
'''