from statistics import *
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

try:
    import matplotlib.pyplot as plt
except ImportError:
    raise ImportError("Matplotlib is not installed. Please install matplotlib to use this package.")

def check_numpy_array(data):
    if not isinstance(data, np.ndarray):
        data = np.array(data)
    return data

def plot_histogram(data):
    """Plot a histogram of the data, with the mean and median marked on the plot."""
    data=check_numpy_array(data)
    mean_val = mean(data)
    median_val = median(data)
    
    plt.hist(data, bins=10)
    plt.axvline(mean_val, color='r', linestyle='dashed', linewidth=1)
    plt.axvline(median_val, color='g', linestyle='dashed', linewidth=1)
    plt.show()
    
    return mean_val, median_val