'''
Question:
Write a program which accepts a sequence of comma separated 4 digit binary numbers as 
its input and then check whether they are divisible by 5 or not. The numbers that are 
divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010
Notes: Assume the data is input by console.
'''
bi_nums = input('Please input a sequence of comma separated 4 digit binary numbers:')
bi_list = bi_nums.split(',')
int_list = []
remain_list = []
for num in bi_list:
    int_num = int(num,2)
    if int_num % 5 == 0:
        int_list.append(int_num)
    print(int_num)
for num in int_list:
    bi_num = bin(num)[2:]
    remain_list.append(bi_num)
print(','.join(remain_list))
'''
Solution:
value = []
items=[x for x in raw_input().split(',')]
for p in items:
    intp = int(p, 2)
    if not intp%5:
        value.append(p)

print ','.join(value)
'''