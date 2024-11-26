###
## Basic online calculator
###

import numpy as np

## Here I have defined four functions for the four
## basic operations. 
##
## 1) You should provide an interface
## function that will prompt the user for input and
## call the appropriate function based on the user's
## input. The interface function should continue to
## prompt the user for input until the user enters
## 'exit'. 
##
## 2) The interface function should also handle
## any exceptions that might be thrown by the basic
## operations functions. If an exception is thrown,
## the interface function should print an error message
## and continue to prompt the user for input.
##
## 3) Add other "operations" to the calculator, that
## involve complicated operations (e.g., trigonometric
## functions, logarithms, etc.).

def interface():
    possible_operations = ['add', 'subtract', 'multiply', 'divide', 'sine',
                            'cosine', 'tangent', 'log', 'log10', 'log2',
                              'exp', 'sqrt', 'cbrt', 'power', 'factorial', 'exit']
    print("Welcome to the online calculator!")
    print("You can perform the following operations:")
    print(possible_operations)
    user_input = input("Enter an operation from the list: ")

    while user_input != 'exit' or user_input != 'Exit':
        try:
            if user_input == 'add':
                a = float(input("Enter a number: "))
                b = float(input("Enter another number: "))
                print(f"The sum of {a} and {b} is {add(a, b)}")
            elif user_input == 'subtract':
                a = float(input("Enter a number: "))
                b = float(input("Enter another number: "))
                print(f"The difference of {a} and {b} is {subtract(a, b)}")
            elif user_input == 'multiply':
                a = float(input("Enter a number: "))
                b = float(input("Enter another number: "))
                print(f"The product of {a} and {b} is {multiply(a, b)}")
            elif user_input == 'divide':
                a = float(input("Enter a number: "))
                b = float(input("Enter another number: "))
                print(f"The quotient of {a} and {b} is {divide(a, b)}")
            elif user_input == 'sine':
                a = float(input("Enter a number: "))
                print(f"The sine of {a} is {sine(a)}")
            elif user_input == 'cosine':
                a = float(input("Enter a number: "))
                print(f"The cosine of {a} is {cosine(a)}")
            elif user_input == 'tangent':
                a = float(input("Enter a number: "))
                print(f"The tangent of {a} is {tangent(a)}")
            elif user_input == 'log':
                a = float(input("Enter a number: "))
                print(f"The natural logarithm of {a} is {log(a)}")
            elif user_input == 'log10':
                a = float(input("Enter a number: "))
                print(f"The base-10 logarithm of {a} is {log10(a)}")
            elif user_input == 'log2':
                a = float(input("Enter a number: "))
                print(f"The base-2 logarithm of {a} is {log2(a)}")
            elif user_input == 'exp':
                a = float(input("Enter a number: "))
                print(f"The exponential of {a} is {exp(a)}")
            elif user_input == 'sqrt':
                a = float(input("Enter a number: "))
                print(f"The square root of {a} is {sqrt(a)}")
            elif user_input == 'cbrt':
                a = float(input("Enter a number: "))
                print(f"The cube root of {a} is {cbrt(a)}")
            elif user_input == 'power':
                a = float(input("Enter a number: "))
                b = float(input("Enter the power: "))
                print(f"{a} raised to the power of {b} is {power(a, b)}")
            elif user_input == 'factorial':
                a = int(input("Enter a number: "))
                print(f"The factorial of {a} is {factorial(a)}")                                    
            elif user_input == 'exit' or user_input == 'Exit':
                break
            else:
                print("Invalid operation. Please try again.")
        except Exception as e:
            print(f"An error occurred: {e}")
        user_input = input("Enter an operation: ")

def add(a, b):
    """Add two numbers."""
    return a + b

def subtract(a, b):
    """Subtract one number from another."""
    return a - b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def divide(a, b):
    """Divide one number by another."""
    return a / b

def sine(a):
    """Calculate the sine of a number."""
    return np.sin(a)

def cosine(a):
    """Calculate the cosine of a number."""
    return np.cos(a)

def tangent(a):
    """Calculate the tangent of a number."""
    return np.tan(a)

def log(a):
    """Calculate the natural logarithm of a number."""
    return np.log(a)

def log10(a):
    """Calculate the base-10 logarithm of a number."""
    return np.log10(a)

def log2(a):
    """Calculate the base-2 logarithm of a number."""
    return np.log2(a)

def exp(a):
    """Calculate the exponential of a number."""
    return np.exp(a)

def sqrt(a):
    """Calculate the square root of a number."""
    return np.sqrt(a)

def cbrt(a):
    """Calculate the cube root of a number."""
    return np.cbrt(a)

def power(a, b):
    """Raise a to the power of b."""
    return np.power(a, b)

def factorial(a):
    """Calculate the factorial of a number."""
    return np.math.factorial(a)

