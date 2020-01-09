'''
Question:
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106
'''
digit = input('Please input 1~9:')
d = int(digit)
dd = int(digit+digit)
ddd = int(digit+digit+digit)
dddd = int(digit+digit+digit+digit)
sum = d+dd+ddd+dddd
print(sum)

'''
Solution:
a = raw_input()
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
n4 = int( "%s%s%s%s" % (a,a,a,a) )
print n1+n2+n3+n4
'''