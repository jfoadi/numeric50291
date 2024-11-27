##### This is the python file that contains the function to plot the histogram

import numpy as np # type: ignore
import matplotlib.pyplot as plt # type: ignore


def plot_histogram(data):  # Function to plot histogram
    DataMean = np.mean(data)
    DataMedian = np.median(data)

    plt.hist(data)  # Plot histogram

    # Adding mean and median to the plot
    plt.axvline(DataMean, color='red', linestyle='dashed', linewidth=2, label=f'Mean: {DataMean:.2f}')
    plt.axvline(DataMedian, color='purple', linestyle='dashed', linewidth=2, label=f'Median: {DataMedian:.2f}')

    plt.legend()
    plt.savefig('graphics.png')  # Save plot to file
    plt.close()