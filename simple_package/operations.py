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

def calculator():
    while True:
        try:
            # Get user's input for the operation
            user_input = input("\nEnter operation (add, subtract, multiply, divide, exit): ").lower() # .lower() to make the input case-insensitive
            
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
            else:
                # Inform the user if the operation is invalid
                print("Invalid operation. Try again.")

        except ValueError as e:
            # Handle specific "Cannot divide by zero" error
            if str(e) == "Cannot divide by zero.":
                print("Error: Cannot divide by zero.")
            else:
                # Handle other invalid numeric input errors
                print("Invalid input. Please enter numeric values.")

