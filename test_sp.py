###
## test package
###

import simple_package as sp
import numpy as np

if __name__ == '__main__':
    ## Define two numbers
    a = 1
    b = 2
    
    ## Print their sum with a nice message.
    print(f"The sum of {a} and {b} is {a + b}")

    ## Now do the same for the function in sp
    print(f"The product of {a} and {b} is {sp.multiply(a,b)}")

    # test interface from operations
    sp.interface()

    # test statistics
    data = np.random.normal(0, 1, 1000)
    mean, median, std = sp.calculate_stats(data)
    sp.display_stats(mean, median, std)
    sp.plot_histogram(data, mean, median)