###
## test package
###

import simple_package.operations as op
from simple_package.statistics import calculate_statistics

if __name__ == '__main__':
    ## Define two numbers
    a = 1;
    b = 2;
    
    ## Print their sum with a nice message.
    print(f"The sum of {a} and {b} is {a + b}")

    ## Now do the same for the function in sp
    print(f"The product of {a} and {b} is {op.add(a,b)}")

    op.calculator_interface()
    




