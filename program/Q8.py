'''
Question:
Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world
'''
words = input('please innput a comma seperated sequence of words:')
word_list = words.split(',')
word_list.sort()
result = ','.join(word_list)
print(result)

'''
items=[x for x in raw_input().split(',')]
items.sort()
print ','.join(items)
'''