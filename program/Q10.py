'''
Question:
Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world
'''
words = input('Please input a sequence of whitespace separated words(include some duplicated words):')
word_list = words.split(' ')
copy_list = words.split(' ')
word_remain = []
for word in word_list:
    if word in copy_list:
        word_remain.append(word)
        copy_list.remove(word)
        while True:
            if word in copy_list:
                copy_list.remove(word)
            else:
                break
word_remain.sort()
print(' '.join(word_remain))
'''
Solution:
s = raw_input()
words = [word for word in s.split(" ")]
print " ".join(sorted(list(set(words))))
'''