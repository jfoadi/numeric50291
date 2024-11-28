###
## test package
###

from simple_package.operations import user_interface
from simple_package.statistics import data_input
from simple_package.graphics import plots

try: 
    import numpy as np
    import matplotlib.pyplot as plt

except ImportError: 
    print("Numpy and/or matplotlib is not installed")
    raise SystemExit

if __name__ == "__main__":
    user_interface()
    data_input()