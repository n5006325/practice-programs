# Filename : odd_even.py

# ask for a number, depending on odd or even print message.

numberOne = input('Enter first number:')
numberTwo = input('Enter second number:')

if (int(numberOne) % 4 == 0):
    print(numberOne, "is divisible by 4")
elif (int(numberOne) % 2) == 0:
    print(numberOne, 'is even')
else:
    print(numberOne, 'is odd')



if (int(numberTwo) % 4 == 0):
    print(numberTwo, 'is divisible by 4')
elif (int(numberTwo) % 2) == 0:
    print(numberTwo, 'is even')
else:
    print(numberTwo, "is odd")

if int(numberOne) % int(numberTwo) == 0:
    print (numberOne, "divides evenly by ", numberTwo)
else:
    print(numberOne, "does not divide evenly by", numberTwo)
