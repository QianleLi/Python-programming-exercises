'''
Question:
Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
D 100
W 200

D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500
'''
balance = 0
trigger = True
def check_point():
    choice = input('One more transaction log? Y/N')
    if choice == 'Y':
        trigger = True
    elif choice == 'N':
        trigger = False
    else:
        trigger = False
    return trigger

while trigger:
    line = input('Please input a transaction log:')
    number = line[2:]
    if line[0] == 'D':
        balance += int(number)
        print('+'+number)
        trigger = check_point()
    elif line[0] == 'W':
        balance -= int(number)
        print('-'+number)
        trigger = check_point()
    else:
        print('Please input a transaction log!!!')
print(balance)
    
'''
Solution:
netAmount = 0
while True:
    s = raw_input()
    if not s:
        break
    values = s.split(" ")
    operation = values[0]
    amount = int(values[1])
    if operation=="D":
        netAmount+=amount
    elif operation=="W":
        netAmount-=amount
    else:
        pass
print netAmount
'''