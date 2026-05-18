"""
Periodic Table Info - Print all the elements in the Periodic Table of the Elements.
Copyright (C) 2017-2026 willtheorangeguy
"""

# pylint: disable=import-error, invalid-name, duplicate-code

# This is the main program file for Periodic Table Info.
# Imports all other files.
from elements import element_print_out

# Print all elements and input field
print(element_print_out())

input_from_user = input("Please enter the element you would like to learn more about: ")

# Prints the information the user want based on what input they have selected.
if input_from_user.lower() == "":
    print("")

else:
    print("Sorry, that is not an element of the current Periodic Table!")
    print(
        "Remember to type it like this: 'Sodium' or 'sodium'. \
            Capitalization doesn't matter. No punctuation, please!"
    )
