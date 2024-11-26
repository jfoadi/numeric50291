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

def power(a, b):
    return a ** b

def log(a, b):
    return math.log(a, b)

def sin(a):
    return math.sin(a)

def cos(a):
    return math.cos(a)

def tan(a):
    return math.tan(a)


def interface():
    operations = ['add', 'subtract', 'multiply', 'divide', 'power', 'log']
    trig_operations = ['sin', 'cos', 'tan']
    print("Choose operation: add, subtract, multiply, divide, power, log or exit")
    print("Or choose trigonometric functions: sin, cos, tan")
    while True:
        choice = input("Enter operation: ")
        if choice == 'exit':
            print("Bye!")
            break
        if (choice not in operations) and (choice not in trig_operations):
            print("Please enter a valid operation!")
            continue
        try:
            if choice in operations:
                number1 = float(input("Enter first number: "))
                number2 = float(input("Enter second number: "))
                print(f"The {choice} of {number1} and {number2} is {globals()[choice](number1, number2)}")
            elif choice in trig_operations:
                number = float(input("Enter number: "))
                print(f"The {choice} of {number} is {globals()[choice](number)}")
        except ValueError:
            print("Please enter a valid number!")
            continue
        except ZeroDivisionError:
            print("Cannot divide by zero!")
            continue
        
            
        


        

