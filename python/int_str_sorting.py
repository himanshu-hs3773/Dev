from random import shuffle

l1 = ['whose', 'code', 'is', 'this']

shuffle(l1)                   # randomizing items of a list in place
print(l1)                     # returns a randomly shuffled items

# sorting an integer string
l2 = ['2', '5', '9', '11', '1', '16', '55', '-10', '-3', '0']

l1.sort()                     # sorted by ASCII value of 1st character of each element of te list
l2.sort()                     # sorted by ASCII value of 1st character of each element of te list
print(l1)                     # returns ['code', 'is', 'this', 'whose']
print(l2)                     # returns ['-10', '-3', '0', '1', '11', '16', '2', '5', '55', '9']


# convert str to int using list Comprehension
shuffle(l2)
l2 = [int(i) for i in l2]
l2.sort()
print(l2)                     # returns [-10, -3, 0, 1, 2, 5, 9, 11, 16, 55]
l2 = [str(i) for i in l2]     # converting integers back to string
print(l2)                     # returns ['-10', '-3', '0', '1', '2', '5', '9', '11', '16', '55']

# convert str to int using map
shuffle(l2)
l2 = list(map(int, l2))       # mapped list items to integers
l2.sort()
print(l2)                     # returns [-10, -3, 0, 1, 2, 5, 9, 11, 16, 55]
l2 = list(map(str, l2))       # mapped list items to string
print(l2)                     # returns ['-10', '-3', '0', '1', '2', '5', '9', '11', '16', '55']
