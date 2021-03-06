'''
Question:
A website requires the users to input username and password to register. 
Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1
'''
good_one = []
character = ['$','#','@']
raw_data = input('Please input passwords with comma seperated:')
passwords = raw_data.split(',')
def count_num(password,character):
    print(password)
    letter_upper = 0
    letter_lower = 0
    num = 0
    char_num = 0
    for letter in password:
        if letter.isalpha():
            if letter.isupper():
                letter_upper += 1
            else:
                letter_lower += 1
        elif letter.isdigit():
            num += 1
        elif letter in character:
            char_num += 1
    return letter_upper,letter_lower,num,char_num
for password in passwords:
    pwd_len = len(password)
    letter_upper,letter_lower,num,char_num = count_num(password,character)
    print(letter_upper,letter_lower,num,char_num)
    if 6 <= len(password) <= 12:
        if letter_upper < 1 or letter_lower < 1 or num < 1 or char_num < 1:
            print('The password has to have one upper letter, one lower letter, one digit and one character from \'$#@\'!')
        else:
            good_one.append(password)
    else:
       print('The length of password should between 6 and 12.')
print(','.join(good_one))
'''
Solutions:
import re
value = []
items=[x for x in raw_input().split(',')]
for p in items:
    if len(p)<6 or len(p)>12:
        continue
    else:
        pass
    if not re.search("[a-z]",p):
        continue
    elif not re.search("[0-9]",p):
        continue
    elif not re.search("[A-Z]",p):
        continue
    elif not re.search("[$#@]",p):
        continue
    elif re.search("\s",p):
        continue
    else:
        pass
    value.append(p)
print ",".join(value)
'''