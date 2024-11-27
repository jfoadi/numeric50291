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

import numpy as np  # type: ignore
import matplotlib.pyplot as plt # type: ignore

def calculate_mean(data): # Function to calculate mean
    return np.mean(data)

def calculate_median(data): # Function to calculate median
    return np.median(data)

def calculate_std(data): # Function to calculate standard deviation
    return np.std(data)

def plot_histogram(data):  # Function to plot histogram
    DataMean = calculate_mean(data)
    DataMedian = calculate_median(data)

    plt.hist(data)  # Plot histogram

    # Adding mean and median to the plot
    plt.axvline(DataMean, color='red', linestyle='dashed', linewidth=2, label=f'Mean: {DataMean:.2f}')
    plt.axvline(DataMedian, color='purple', linestyle='dashed', linewidth=2, label=f'Median: {DataMedian:.2f}')

    plt.legend()
    plt.savefig('graphics.png')  # Save plot to file
    plt.close()


