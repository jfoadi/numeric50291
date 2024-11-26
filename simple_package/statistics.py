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
    import matplotlib.pyplot as plt

    def calculate_stats(data):
        if type(data) == list:
            data = np.array(data)
        elif type(data) != np.ndarray:
            raise TypeError("Data must be a list or numpy array.")
            
        mean = np.mean(data)
        median = np.median(data)
        std = np.std(data)
        return mean, median, std

    def display_stats(mean, median, std):
        print(f"The mean is {mean}")
        print(f"The median is {median}")
        print(f"The standard deviation is {std}")

except ImportError:
    print("You need to install numpy and matplotlib to use this package.")



