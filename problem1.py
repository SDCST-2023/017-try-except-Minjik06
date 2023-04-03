#python3
# Quadratic Equation
# Have the user enter in the coefficients of a quadratic equation in the
# format: ax^2 + bx + c = 0 and calculate the solutions of the equation
# rounded to 2 decimal places. Use a try...except block to catch if there
# is no solution
# incorporate a while loop to keep having the user enter in values for a,b,c
# until they are valid
# incorporate a second while loop to keep repeating the program without
# having to rerun it.

""" Sample output:
Enter in the coefficients for a quadratic equation in the format:
  ax^2 + bx + c = 0
a:3
b:d
c:1
Those are not valid values for a, b or c
a:3
b:2
c:1
There are no real roots to the equation
a:2
b:-3
c:-6
The roots are 2.64 and -1.14
a:1
b:8
c:16
The roots are -4.0 and -4.0
"""
import os
os.system('cls')


print("Enter in the coefficients for a quadratic equation in the format:")
print("  ax^2 + bx + c = 0")


import math
while True:
    try:
        a=input("Enter in a number a: ")
        b=input("Enter in a number b: ")
        c=input("Enter in a number c: ")
        print(f"  {a}x^2 + {b}x + {c} = 0")
        a=int(a)
        b=int(b)
        c=int(c)
        d=((-1*b)+math.sqrt(math.pow(b,2)-(4*(a)*(c))))/(2*a)
        e=((-1*b)-math.sqrt(math.pow(b,2)-(4*(a)*(c))))/(2*a)
        print(f"The roots are {d} is {e}")
        break
    except Exception as err:
        if a==str(a) or b==str(b) or c==str(c):
            print(f"Those are not valid values for {a},{b} or {c}")
        else:
            print("There are no real roots to the equation")