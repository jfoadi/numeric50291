###
## Module for basic statistics
###

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

import numpy as np

try:
    import numpy as np
except ImportError:
    raise ImportError("Numpy is not installed. Please install numpy using 'pip install numpy'.")

def check_input(data):
    if not isinstance(data, (np.ndarray, list)):
        raise TypeError("Input data must be a numpy array or a list.")
    if isinstance(data, list):  # If data is a list, convert it to a NumPy array
        data = np.array(data)
    return data

def mean(data):
    return np.mean(data)

def median(data):
    return np.median(data)

def std_dev(data):
    return np.std(data)

def display_statistics(data):
    try:
        data = check_input(data)

        mean_value = mean(data)
        median_value = median(data)
        std_dev_value = std_dev(data)

        print(f"Statistics for the given data:")
        print(f"Mean: {mean_value}")
        print(f"Median: {median_value}")
        print(f"Standard Deviation: {std_dev_value}")
    except TypeError as e:
        print(f"Error: {e}")
