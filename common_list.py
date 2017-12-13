# Filename : common_list.py

# return a list that contains only elements that are common between then
# lists without duplicates. make sure program works on lists of two different sizes.
# extra - randomly generate two lists.



# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

import random

a = random.sample(range(99), 20)
b = random.sample(range(99), 20)

print(a)
print(b)

new_list = []

new_list = set(a).intersection(set(b))

print(new_list)
