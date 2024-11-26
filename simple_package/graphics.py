# graphics.py
import numpy as np
import matplotlib.pyplot as plt


def display(mean_val, median_val, std_dev_val):
    """Display the mean, median, and standard deviation of the data."""
    print(f"The mean of the data is: {mean_val}")
    print(f"The median of the data is: {median_val}")
    print(f"The standard deviation of the data is: {std_dev_val}")

def histogram(data, mean, median):
    """Plot a histogram of the data with the mean and median marked."""
    plt.hist(data, bins=10)
    plt.axvline(mean, color='r', linestyle='dashed', linewidth=1)
    plt.axvline(median, color='g', linestyle='dashed', linewidth=1)
    plt.show()

