import matplotlib.pyplot as plt

try:
    import matplotlib.pyplot as plt
except ImportError:
    raise ImportError("Matplotlib is not installed. Please install matplotlib using 'pip install matplotlib'.")

import simple_package as sp

def plot_histogram(data):
    # Ensure the input is a numpy array or convert it to one if it is a list
    try:
        data = sp.check_input(data)

        # Calculate mean and median for marking on the plot
        mean_value = sp.mean(data)
        median_value = sp.median(data)

        # Plotting the histogram
        plt.hist(data, bins=10, alpha=0.7, color='pink', edgecolor='hotpink')
        plt.axvline(mean_value, color='olivedrab', linestyle='dashed', linewidth=2, label=f'Mean: {mean_value:.2f}')
        plt.axvline(median_value, color='steelblue', linestyle='dashed', linewidth=2, label=f'Median: {median_value:.2f}')

        # Adding labels, title, and legend
        plt.xlabel('Value')
        plt.ylabel('Frequency')
        plt.title('Histogram of Data with Mean and Median')
        plt.legend()

        # Show the plot
        plt.show()

    except TypeError as e:
        print(f"Error: {e}")
