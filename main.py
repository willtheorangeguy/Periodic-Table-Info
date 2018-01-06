"""
Copyright (C) 2016 - 2018 Dog Face Development Company
This is the main program file for Periodic Table Info.
Run this file to run the app.
"""

# Imports all other files.
from elements import element_print_out

# Print all elements and input field
print(element_print_out())

input_from_user = input ("Please enter the element you would like to learn more about: ")


# Prints the information the user want based on what input they have selected.
if input_from_user.lower() == "" :
    print("")

else :
    print("Sorry, that is not an element of the current Periodic Table!")
    print("Remember to type it like this: 'Sodium' or 'sodium'. Capatlization dosen't matter. No punctuation, please!")
