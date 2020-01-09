'''
Question:
Write a program that accepts a sentence and calculate the number
 of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9
'''
U = 0
L = 0
sentence = input('Please enter a sentence:')
for digit in sentence:
    if digit.isupper():
        U += 1
    elif digit.islower():
        L += 1
    else:
        continue
print('UPPER CASE '+str(U))
print('LOWER CASE '+str(L))

'''
Solution:
s = raw_input()
d={"UPPER CASE":0, "LOWER CASE":0}
for c in s:
    if c.isupper():
        d["UPPER CASE"]+=1
    elif c.islower():
        d["LOWER CASE"]+=1
    else:
        pass
print "UPPER CASE", d["UPPER CASE"]
print "LOWER CASE", d["LOWER CASE"]
'''