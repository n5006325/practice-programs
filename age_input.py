# Filename : age_input.py

# create a program that asks the user to enter their name and their age.
# print out message addressed to them that tells them the year that they will
# turn 100 years old.
# Extra - enter another number and print out that many copies of the message
# print out that many copies of the previous message on seperate lines.


name = input("What is your name: ")
age = input("How old are you? ")
year = 2017

number = input("Enter number:")

oneHundred = (100 - int(age)) + 2017

x = 1
for x in range(int(number)):
    print("Hi {0} you will be 100 years old in the year {1}".format(name, oneHundred))
    x += 1
    if x == int(number):
        break
