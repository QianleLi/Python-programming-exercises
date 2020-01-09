'''
Question:
Write a program, which will find all such numbers between 1000 and 3000 (both included) such
 that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.
'''
even_list = []
for num in range(1000,3001):
    i = 0
    num = str(num)
    for digit in num:
        if int(digit) % 2 == 0:
            i += 1
            if i == 4:
                even_list.append(num)
            continue
        else: 
            break
print(','.join(even_list))

'''
Solution:
values = []
for i in range(1000, 3001):
    s = str(i)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
        values.append(s)
print ",".join(values)
'''