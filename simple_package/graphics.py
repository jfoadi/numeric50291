import matplotlib.pyplot as plt

def plot_histogram(data, mean, median):
        plt.hist(data)
        plt.axvline(mean, color='r', linestyle='dashed', linewidth=1)
        plt.axvline(median, color='b', linestyle='dashed', linewidth=1)
        plt.savefig('histogram.png')
        plt.show()