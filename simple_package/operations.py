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
    """Divide one number by another."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
def sin(a):
    """Calculate sine of an angle in degrees."""
    return np.sin(np.radians(a))

def cos(a):
    """Calculate cosine of an angle in degrees."""
    return np.cos(np.radians(a))

def tan(a):
    """Calculate tangent of an angle in degrees."""
    return np.tan(np.radians(a))

def logarithm(a, base=10):
    """Calculate logarithm of a number with a specified base (default is 10)."""
    if a <= 0:
        raise ValueError("Logarithm is only defined for positive numbers.")
    if base <= 0 or base == 1:
        raise ValueError("Logarithm base must be greater than 0 and not equal to 1.")
    return np.log10(a) if base == 10 else np.log(a)/np.log(base)

def calculator():
    while True:
        try:
            # Get user's input for the operation
            user_input = input("\nEnter operation (add, subtract, multiply, divide, sin, cos, tan, log, exit): ").lower() # .lower() to make the input case-insensitive
            
            # Exit function if user enters 'exit'
            if user_input == 'exit':
                print("Exiting...")
                break

            # Check if the input is a valid operation
            if user_input in ('add', 'subtract', 'multiply', 'divide'):
                # Get the two numbers from the user
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))

                # Perform the operation based on user input
                if user_input == 'add':
                    result = add(a, b)
                elif user_input == 'subtract':
                    result = subtract(a, b)
                elif user_input == 'multiply':
                    result = multiply(a, b)
                elif user_input == 'divide':
                    result = divide(a, b)

                # Print the result
                print(f"Result: {result}")

            # Operations that take a single argument (trigonometric, logarithm)
            elif user_input in ('sin', 'cos', 'tan'):
                a = float(input("Enter the angle in degrees: "))

                if user_input == 'sin':
                    result = sin(a)
                elif user_input == 'cos':
                    result = cos(a)
                elif user_input == 'tan':
                    result = tan(a)

                # Print the result
                print(f"Result: {result}")

            elif user_input == 'log':
                a = float(input("Enter the number: "))
                base = input("Enter the base for logarithm (press Enter for base 10): ")
                base = int(base) if base else 10  # Default to base 10 if no input is given
                result = logarithm(a, base)

                # Print the result
                print(f"Result: {result}")
            else:
                # Inform the user if the operation is invalid
                print("Invalid operation. Try again.")

        except ValueError as e:
            print(f"Error: {e}")