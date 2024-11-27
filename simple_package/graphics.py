import matplotlib.pyplot as plt

def plot_histogram(data, mean, median):
    plt.hist(data, bins=50, alpha=1, label='Data')
    plt.axvline(mean, color='r', label='Mean')
    plt.axvline(median, color='g', label='Median')
    plt.legend()
    plt.show()