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

import numpy as np # type: ignore

def add(a, b): # Addition function
    return a + b

def subtract(a, b): # Subtraction function
    return a - b

def multiply(a, b): # Multiplication function
    return a * b

def divide(a, b): # Division function
    return a / b

def powerof(a, b):
    return a ** b