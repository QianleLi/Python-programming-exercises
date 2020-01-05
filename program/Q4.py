'''
Question:
Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')
'''
numbers = input('please input a sequence of comma-separated numbers: ')
comma = ','
nlist = numbers.split(comma)
ntuple = ()
for i in range(len(nlist)):
    ntuple = ntuple+(nlist[i],)
print(nlist)
print(ntuple)
'''
tuple() method can convert list to tuple

Solution:
values=raw_input()
l=values.split(",")
t=tuple(l)
print l
print t
'''