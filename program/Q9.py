'''
Question 9
Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT
'''
def getInput():
    input_lines = []
    while True:
        raw_data = input('Please input multiple lines of words:')
        input_lines.append(raw_data)
        choice = input('More lines? Input Y to input one more line.')
        if choice == 'Y':
            continue
        else:
            break
    return '\n'.join(input_lines)
input_words = getInput()
print(input_words.upper())

'''
Solution:
lines = []
while True:
    s = raw_input()
    if s:
        lines.append(s.upper())
    else:
        break;

for sentence in lines:
    print sentence
'''