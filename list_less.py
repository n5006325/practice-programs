# Filename: list_less.py

# write a program that prints out all the elements of the list that are less than 5
# make a new lis that has all th eelemnets less than 5 from this list in it.
# print out new list.
# ask user for a number and return a list that contains only elemnts from original
# list that are smaller than that number given by the user.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new_list = []
number = int(input('Enter in a number:'))

for i in a:
    if i < number:
        new_list.append(i)

        # print("Numbers below 5 are", i) # old code for problem 1

print(new_list)
