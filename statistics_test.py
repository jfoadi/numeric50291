<<<<<<< HEAD

from simple_package import graphics
from simple_package import statistics

def main():
    try:
        import numpy as np
        import matplotlib.pyplot as plt
    except ImportError:
        raise ImportError("numpy and/or matplotlib packages are not installed")
    
    data = np.array([1, 2, 3, 4, 5, 5, 3, 1, 4, 6, 8, 3, 10])  # example data
    mean, median, std_dev = statistics.calculate_statistics(data)
    statistics.display_statistics(mean, median, std_dev)
    graphics.plot_histogram(data, mean, median)

if __name__ == "__main__":
=======

from simple_package import graphics
from simple_package import statistics

def main():
    try:
        import numpy as np
        import matplotlib.pyplot as plt
    except ImportError:
        raise ImportError("numpy and/or matplotlib packages are not installed")
    
    data = np.array([1, 2, 3, 4, 5, 5, 3, 1, 4, 6, 8, 3, 10])  # example data
    mean, median, std_dev = statistics.calculate_statistics(data)
    statistics.display_statistics(mean, median, std_dev)
    graphics.plot_histogram(data, mean, median)

if __name__ == "__main__":
>>>>>>> refs/remotes/origin/master
    main()