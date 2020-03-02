
'''
Question 22
Level 3

Question:
Write a program to compute the frequency of the words from the input. 
The output should output after sorting the key alphanumerically. 
Suppose the following input is supplied to the program:
New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
Then, the output should be:
2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1
'''

input_string = 'New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.'
input_words = input_string.split(' ')
dictionary = {}
for word in input_words:
    if word not in dictionary:
        dictionary[word] = 1
    else:
        dictionary[word] += 1
print(dictionary)
'''
#Solution:
freq = {}   # frequency of words in text
line = 'New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.'
for word in line.split():
    freq[word] = freq.get(word,0)+1
print(freq)

words = freq.keys()
sorted(words)
print(type(words))

for w in words:
    print('%s' %w)
'''