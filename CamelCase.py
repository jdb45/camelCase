'''Program: CamelCase
Author: Jeremy Belisle
Last Date Modified: 1/10/17
This program will let the user input a sentence and will convert it to camel case'''

print("CamelCase Converter", "\n")



def display_banner():
    '''Display program name in a banner'''
    msg = 'AWESOME camelCaseGenerator PROGRAM'
    stars = '*' * len(msg)
    print('\n', stars, '\n', msg, '\n', stars, '\n')

check = True

display_banner()

while check:

    userInput = input("Enter your sentence here: ")  # getting the user input

    if userInput[0].isdigit():  # using the isdigit to check and see if the first letter is a number
        print("Sentence can't start with a number")

    elif userInput[0] != int:  # just checking a few invalid characters
        if "#" in userInput:
            print("Sentence can't contain invalid characters #, \", +")
        elif "\"" in userInput:
            print("Sentence can't contain invalid characters #, \", +")
        elif "+" in userInput:
            print("Sentence can't contain invalid characters #, \", +")
        else:
            userInput = userInput.title()  # using title to convert every word to start with upper case and the rest to be lower case
            userInput = userInput.replace(" ", "")  # getting rid of the spaces
            check = False
            print(userInput[0].lower() + userInput[1:])  # Printing the output with the first letter in lower case
