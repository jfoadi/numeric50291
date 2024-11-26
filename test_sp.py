###
## test package
###


from simple_package.operations import interface
from simple_package.statistics import interface_statistics

try:
    import numpy as np
    import matplotlib.pyplot as plt
except ImportError as e:
    print(f"Error importing libraries: {e}")
    print("Make sure numpy and matplotlib are installed.")
    raise SystemExit


if __name__ == '__main__':

    interface()

    interface_statistics()