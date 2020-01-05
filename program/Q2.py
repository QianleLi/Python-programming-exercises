'''
Question:
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320
'''
number = int(input('Please input an positive integer:'))
result = 1
for i in range(2,number+1):
    result = result * i
print(result)