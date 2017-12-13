# Filename : only_even.py

# copy only even numbers into a new list.

a = [1, 2, 9, 16, 25, 36, 49, 64, 81, 100]
new_list = [x for x in a if x % 2 == 0]



# for x in a:       # old code multi line
#    if x % 2 == 0:
#        new_list.append(x)

print(new_list)
