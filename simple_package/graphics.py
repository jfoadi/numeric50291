import matplotlib.pyplot as plt

def plots(data, data_mean, data_median): 
    try: 
        plt.figure(figsize=(10, 6))
        plt.hist(data, bins=10, alpha=0.7, color='blue', edgecolor='black')
        plt.axvline(data_mean, color='red', linestyle='dashed', linewidth=1.5, label=f'Mean: {data_mean:.2f}')
        plt.axvline(data_median, color='green', linestyle='dashed', linewidth=1.5, label=f'Median: {data_median:.2f}')
        plt.title("Histogram of Data with Mean and Median")
        plt.xlabel("Values")
        plt.ylabel("Frequency")
        plt.legend()
        plt.show()
    except Exception as e: 
        print("Something is wrong")



