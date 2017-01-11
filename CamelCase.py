'''Program: CamelCase 
Author: Jeremy Belisle
Last Date Modified: 1/10/17
This program will let the user input a sentence and will convert it to camel case'''

print("Camel Case Converter", "\n")

userInput = input("Enter your sentence here: ")  # getting the user input
userInput = userInput.title()  # using title to convert every word to start with upper case and the rest to be lower case
userInput = userInput.replace(" ", "")  # getting rid of the spaces

print(userInput[0].lower() + userInput[1:])  # Printing the output with the first letter in lower case

