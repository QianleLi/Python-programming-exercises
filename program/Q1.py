'''
Question:
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.
'''
numbers = []
for num in range(2000,3201):
    div7 = num % 7
    div5 = num % 5
    if div7 == 0 and div5 != 0:
        numbers.append(str(num))
comma = ','
print(comma.join(numbers))