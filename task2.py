#!python3

# Reciprocal
# have the program iterate through the list and determine the
# reciprocal of each number as a decimal and print it.
# use the try/except to find any invalid values and display
# the error message

#sample output:
"""
The reciprocal of 0 does not exist
The reciprocal of 1 is 1.0
The reciprocal of 2 is 0.5
The reciprocal of 3 is 0.3333333333333333
The reciprocal of 4 is 0.25


1/list
"""
numbers = [0,1,2,3,4]
for i  in numbers:
    try:
        k = 1/i
        print(f"reciprocal of {i} is {k}")
    except Exception as err:
        print(f"The reciprocal of {i} does not exist")


