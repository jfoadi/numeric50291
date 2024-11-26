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


try:
    import numpy as np
except ImportError:
    raise ImportError("Numpy is not installed. Please install numpy to use this package.")



def check_numpy_array(data):
    if not isinstance(data, np.ndarray):
        data = np.array(data)
    return data

def mean(data):
    """Calculate the mean of the data."""
    data=check_numpy_array(data)
    return np.mean(data)

def median(data):
    """Calculate the median of the data."""
    data=check_numpy_array(data)
    return np.median(data)

def std_dev(data):
    """Calculate the standard deviation of the data."""
    data=check_numpy_array(data)
    return np.std(data)

def display_stats(data):
    """Display the mean, median, and standard deviation of the data."""
    data=check_numpy_array(data)
    print(f"The mean of the data is {mean(data)}")
    print(f"The median of the data is {median(data)}")
    print(f"The standard deviation of the data is {std_dev(data)}")
    
    return mean(data), median(data), std_dev(data)
