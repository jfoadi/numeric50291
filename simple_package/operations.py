###
## Basic online calculator
###


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
        raise ValueError("Please do not enter 0 for second number")
    return a / b

def sin(a): 
    return np.sin(a)

def cos(a): 
    return np.cos(a)

def logarithmic(a): 
    return np.log(a)


def user_interface(): 
    while True: 
        user_input = input("Please select an option: ")

        if user_input == "exit": 
            print("Goodbye")
            break
        if user_input in ["add", "subtract", "multiply", "divide"]: 
            while True: 

                try: 
                    a = float(input(("First number: ")))
                    b = float(input(("Second number: ")))
                    if user_input == "add":
                        print(add(a, b))
                        break

                    elif user_input == 'subtract':
                        print(subtract(a, b))
                        break


                    elif user_input == 'multiply':
                        print(multiply(a, b))
                        break

                    elif user_input == 'divide':
                        try: 
                            result = divide(a, b)
                            print(result)
                            break
                        except ValueError as e: 
                            print(e)

                except ValueError as e: 
                    print("Please enter a correct value")
                
                except Exception as e: 
                    print("An error occurred!")


        
        elif user_input in ["sin", "cosine", "tangent"]: 
            while True:
                try: 
                    angle = float(input("Please enter the radians: "))

                    if user_input == "sin": 
                        print(sin(angle))
                        break
                    elif user_input == "cosine": 
                        print(cos(angle))  
                        break          
                except ValueError as e: 
                    print(e)                  
                except Exception as e: 
                    print(e)
        elif user_input == "log": 
            while True: 
                try: 
                    number = float(input("Please enter a number: "))
                    print(logarithmic(number))
                    break
                except ValueError as e: 
                    print(e)

        else: 
            print("Please select a valid option")
 



        



