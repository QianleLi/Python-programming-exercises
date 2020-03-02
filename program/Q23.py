'''
Question:
    Write a method which can calculate square value of number
'''
def square(l):
    s = l ** 2
    return s

num = int(input('Please input a number'))
print(square(num))