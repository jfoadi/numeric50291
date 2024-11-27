<<<<<<< HEAD
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

def calculate_statistics(data):
    if not isinstance(data, (np.ndarray, list)):
        raise ValueError("Input must be a numpy array or a list")
    if isinstance(data, list):
        data = data
    
    mean = np.mean(data)
    median = np.median(data)
    std_dev = np.std(data)
    
    return mean, median, std_dev

def display_statistics(mean, median, std_dev):
    print(f"Mean: {mean}")
    print(f"Median: {median}")
    print(f"Standard Deviation: {std_dev}")
=======
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

def calculate_statistics(data):
    if not isinstance(data, (np.ndarray, list)):
        raise ValueError("Input must be a numpy array or a list")
    if isinstance(data, list):
        data = np.arrry(data)
    
    mean = np.mean(data)
    median = np.median(data)
    std_dev = np.std(data)
    
    return mean, median, std_dev

def display_statistics(mean, median, std_dev):
    print(f"Mean: {mean}")
    print(f"Median: {median}")
<<<<<<< HEAD
    print(f"Standard Deviation: {std_dev}")
=======
    print(f"Standard Deviation: {std_dev}")

def plot_histogram(data, mean, median):
    plt.hist(data, bins=50, alpha=1, label='Data')
    plt.axvline(mean, color='r', label='Mean')
    plt.axvline(median, color='g', label='Median')
    plt.legend()
    plt.show()

''' added a test to make sure code works as desired '''
def main():
    try:
        import numpy as np
        import matplotlib.pyplot as plt
    except ImportError:
        raise ImportError("numpy and/or matplotlib packages are not installed")
    
    data = np.array([1, 2, 3, 4, 5, 5, 3, 1, 4, 6, 8, 3, 10])  # example data
    mean, median, std_dev = calculate_statistics(data)
    display_statistics(mean, median, std_dev)
    plot_histogram(data, mean, median)

if __name__ == "__main__":
    main()
>>>>>>> f41cb7b3d740c9f646fc85d14b640613bb8ac0bc
>>>>>>> refs/remotes/origin/master
