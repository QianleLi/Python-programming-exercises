'''
Question:
Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
Suppose the following input is supplied to the program:
1,2,3,4,5,6,7,8,9
Then, the output should be:
1,3,5,7,9
'''
numbers = input('Please input a sequence of comma-separated numbers:')
num_list = numbers.split(',')
odd_list = []
print(num_list)
for num in num_list:
    if int(num) % 2 == 1:
        odd_list.append(num)
    else:
        continue
print(','.join(odd_list))

'''
Solution:
values = raw_input()
numbers = [x for x in values.split(",") if int(x)%2!=0]
print ",".join(numbers)
'''