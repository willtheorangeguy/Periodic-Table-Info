"""
Periodic Table Info - Print all the elements in the Periodic Table of the Elements. 
Copyright (C) 2017-2022 Dog Face Development Co.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 3 of the License.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
# This is the main program file for Periodic Table Info.

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
    print("Remember to type it like this: 'Sodium' or 'sodium'. Capitalization doesn't matter. No punctuation, please!")
