# Filename : divisor.py

# ask user for a number and then print out a list of all divisors of that number.

num = int(input('Enter in a number: '))
my_list = list(range(1, num + 1))

print(my_list)

divisorList = []

for number in my_list:
    if num % number ==0:
        divisorList.append(number)

print(divisorList)
