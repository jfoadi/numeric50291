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
def interface_funciton():
    while True:
        try:
            operation = input("Enter the operation you want to perform from 'add', 'subtract','multiply','divide': ")
            if operation == "exit":
                break
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            if operation == "add":
                print(f"The sum of {a} and {b} is {add(a,b)}")
            elif operation == "subtract":
                print(f"The difference of {a} and {b} is {subtract(a,b)}")
            elif operation == "multiply":
                print(f"The product of {a} and {b} is {multiply(a,b)}")
            elif operation == "divide":
                print(f"The division of {a} and {b} is {divide(a,b)}")
            else:
                print("Invalid operation")
        except Exception as e:
            print(f"An error occurred: {e}")


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

def log(a, b):
    """Return the logarithm of a with base b."""
    return math.log(a, b)

def power(a, b):
    """Return a raised to the power of b."""
    return a ** b

def sin(a):
    """Return the sine of a."""
    return math.sin(a)

def cos(a):
    """Return the cosine of a."""
    return math.cos(a)

def tan(a):
    """Return the tangent of a."""
    return math.tan(a)
