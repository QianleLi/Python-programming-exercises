'''
Question:
Define a class with a generator which can iterate the numbers, which are divisible by 7, 
between a given range 0 and n.
'''
class Num7():
    r = int(input('input the maximum range'))
    n = 0
    result = []
    while(r % 7 != 0):
        r = r - 1
    while(n <= r):
        if n % 7 == 0:
            result.append(n)
        n += 1

get_number = Num7()
print(get_number.result)

'''
Solution:
def putNumbers(n):
    i = 0
    while i<n:
        j=i
        i=i+1
        if j%7==0:
            yield j

for i in reverse(100):
    print i
'''