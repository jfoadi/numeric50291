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
import operator
import inspect


def log(a, b):
    """Return the logarithm of a with base b."""
    return math.log(a, b)


'''
for some reason log doesnt work in the below seanrio so i had to hardcode it idk why

'''
EXPOSED_FUNCTIONS_MATH = [
    'sin', 'cos', 'tan',
    'fabs', 'sqrt',
    'exp', 'ceil', 'floor'
]
EXPOSED_FUNCTIONS_OPERATOR = [
    'add', 'sub', 'mul',
    'truediv', 'mod', 'pow',
    'neg', 'pos', 'abs'
]

# Dynamically expose functions
def create_wrappers():
    namespace = {}
    for func_name in EXPOSED_FUNCTIONS_MATH:
        func = getattr(math, func_name)
        namespace[func_name] = func

    for func_name in EXPOSED_FUNCTIONS_OPERATOR:
        func = getattr(operator, func_name)
        namespace[func_name] = func
    return namespace

wrapped_functions = create_wrappers()

def get_num_args(func):
    """
    Returns the number of positional arguments a function takes.

    Args:
        func: The callable to inspect.

    Returns:
        int: Number of positional arguments.
    """
    signature = inspect.signature(func)
    return sum(
        1 for param in signature.parameters.values()
        if param.default == inspect.Parameter.empty and
           param.kind in (inspect.Parameter.POSITIONAL_ONLY, inspect.Parameter.POSITIONAL_OR_KEYWORD)
    )




def interface_funciton():
    Stop= False
    while not Stop:
        try:
            print(f"The available functions are: {EXPOSED_FUNCTIONS_MATH + EXPOSED_FUNCTIONS_OPERATOR} and 'log' or 'exit' to exit")
            operation = input("Enter the operation you would like to perform: ")
            if operation == 'exit':
                Stop=True
                break
            elif operation not in EXPOSED_FUNCTIONS_MATH + EXPOSED_FUNCTIONS_OPERATOR:
                print("Invalid operation.")
                
            elif operation == 'log':
                a = float(input("Enter the number you would like to take the logarithm of: "))
                b = float(input("Enter the base of the logarithm: "))
                result = log(a, b)
                print(f"The result of the operation {operation} on {a} and {b} is: {result}\n")
                
            func = wrapped_functions[operation]
            num_args = get_num_args(func)
            args = []
            for i in range(num_args):
                args.append(float(input(f"Enter argument {i+1}: ")))

            #check all args are numbers
            for arg in args:
                if not isinstance(arg, (int, float)):
                    raise ValueError("All arguments must be numbers.")

            result = func(*args)
            print(f"The result of the operation {operation} on {args} is: {result}\n")
            


        except Exception as e:
            print(f"Error: {e}")
            continue
