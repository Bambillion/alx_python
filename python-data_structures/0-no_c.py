#!/usr/bin/env python3
def no_c(my_string):
    # Initialize an empty string to store the new string without 'c'  or 'C'
    new_string = ""
    # Iterate through each character in the input string
    for char in my_string:
    # check if the character is 'c' or 'C'
        if char != 'c' and char != 'C':
        # If it is not 'c' or 'C' append it 
            new_string += char 
    # Return the new_string without 'c' or 'C'
    return new_string 
