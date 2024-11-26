###
## Basic online calculator
###

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

import math
import numpy as np


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
    if b == 0:
        raise ValueError("Cannot divide by zero.")
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

def power(a, b):
    """Raise a to the power of b."""
    return np.power(a, b)

def factorial(a):
    """Calculate the factorial of a number."""
    return np.math.factorial(a)

def log(a):
    """Calculate the natural logarithm of a number."""
    return np.log(a)

def log10(a):
    """Calculate the base-10 logarithm of a number."""
    return np.log10(a)

def exp(a):
    """Calculate the exponential of a number."""
    return np.exp(a)

def sqrt(a):
    """Calculate the square root of a number."""
    return np.sqrt(a)

def interface():
    operations = {'add': add, 'subtract': subtract, 'multiply': multiply, 'divide': divide, 'sine': sine, 'cosine': cosine, 'tangent': tangent, 'power': power, 'factorial': factorial, 'log': log, 'log10': log10, 'exp': exp, 'sqrt': sqrt}
    
    print("Welcome to the online calculator!")
    print("You can perform the following operations:")

    print(list(operations.keys()))
        
    print("Type 'exit' to quit the calculator.")
    
    while True:
        user_input = input("Enter an operation from the list: ").lower()
        if user_input == 'exit':
            print("Exiting the calculator. Goodbye!")
            break
        elif user_input in operations:
            try:
                if user_input in ['add', 'subtract', 'multiply', 'divide', 'power']:
                    a = float(input("Enter the first number: "))
                    b = float(input("Enter the second number: "))
                    result = operations[user_input](a, b)
                elif user_input in ['sine', 'cosine', 'tangent', 'log', 'log10', 'exp', 'sqrt']:
                    a = float(input("Enter the number: "))
                    result = operations[user_input](a)
                elif user_input == 'factorial':
                    a = int(input("Enter an integer: "))
                    result = operations[user_input](a)
                print(f"The result of {user_input} operation is: {result}")
            except Exception as e:
                print(f"An error occurred: {e}")
        else:
            print("Invalid operation. Please try again.")

