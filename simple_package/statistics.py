###
## Module for basic statistics
###

import numpy as np
import matplotlib.pyplot as plt
from simple_package.graphics import (
    histogram,
    display
)

## Here I need functions to take in data
## and do the following:
##
## 1. Calculate mean. Calculate median. Calculate 
##    standard deviation.
##
## 2. Display the result with a nice print statement.
##
## 3. Plot a histogram of the data, with the mean and median 
##    marked on the plot. This should be part of a new Python
##    file in the package, called graphics.py.
##
## 4. Remember to provide a mechanism for checking that the input
##    is a numpy array or a list (if a list, you must convert it
##    to a numpy array).
##
## 5. Also, do something and/or throw an exception/message if the
##    numpy and matplotlib packages are not installed.


def interface_statistics():
    """Interface for the statistics module."""
    ## Get the data
    data = get_data()
    
    ## Calculate the statistics
    mean_val = mean(data)
    median_val = median(data)
    std_dev_val = std_dev(data)
    
    ## Display the statistics
    display(mean_val, median_val, std_dev_val)
    
    ## Plot the histogram
    histogram(data, mean_val, median_val)


def get_data():
    """Get the data from the user."""
    data = input("Enter a list of numbers separated by commas: ")
    if data == "":
        raise ValueError("You must enter a list of numbers.")
    elif data == "exit":
        raise SystemExit
    else:
        data = [float(x) for x in data.split(",")]
    return np.array(data)


def mean(data):
    """Calculate the mean of the data."""
    return np.mean(data)

def median(data):
    """Calculate the median of the data."""
    return np.median(data)

def std_dev(data):
    """Calculate the standard deviation of the data."""
    return np.std(data)



