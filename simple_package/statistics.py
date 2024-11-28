###
## Module for basic statistics
###

## Here I need functions to take in data
## and do the following:
##
## 1. Calculate mean. Calculate median. Calculate 
##    standard deviation.
import numpy as np
from simple_package.graphics import plots
try: 
    import numpy as np
    import matplotlib.pyplot as plt
except ImportError: 
    print("Numpy and/or matplotlib is not installed")
    exit(1)


def mean(data): 
    return np.mean(data)

def median(data): 
    return np.median(data)

def sd(data): 
    return np.std(data)

    
def data_input(): 
    while True: 
        user_input = input("Please enter a list or a array: ") 
        if user_input == "exit": 
            print("Goodbye")
            break
        
        try: 
            data = [float(x.strip()) for x in user_input.split(',')]
            data = np.array(data)
        
            
            data_mean = mean(data) 
            data_median = median(data)
            data_sd = sd(data)

            print(f'The mean is {data_mean}, the median is {data_median}, and the standard deviation is {data_sd}')


            plots(data, data_mean, data_median)

            

        except ValueError: 
            print("Error: Please enter valid numbers in inoput")
        except Exception as e: 
            print("Something went wrong")




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
