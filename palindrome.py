# Filename : palindrome.py

# ask user for a string and check if string is a palindrome

a = input("Enter word: ")

new_list = a[::-1]

if new_list == a:
    print('Your word is a palindrome!')
else:
    print("your word is not a palindrome!")

    
