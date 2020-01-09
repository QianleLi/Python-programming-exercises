'''
Question:
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3
'''
digit_list = []
letter_list = []
sentence = input('Please input a sentence which contains letters and digits:')
for unit in sentence:
    if unit.isalnum():
        if unit.isalpha():
            letter_list.append(unit)
        else:
            digit_list.append(unit)
    else:
        continue
print('LETTER '+str(len(letter_list)))
print('DIGITS '+str(len(digit_list)))

'''
Solution:
s = raw_input()
d={"DIGITS":0, "LETTERS":0}
for c in s:
    if c.isdigit():
        d["DIGITS"]+=1
    elif c.isalpha():
        d["LETTERS"]+=1
    else:
        pass
print "LETTERS", d["LETTERS"]
print "DIGITS", d["DIGITS"]
'''