###
## test package
###

import simple_package as sp

if __name__ == '__main__':
    ## Define two numbers
    a = 1;
    b = 2;
    
    ## Print their sum with a nice message.
    print(f"The sum of {a} and {b} is {a + b}")

    ## Now do the same for the function in sp
    print(f"The sum of {a} and {b} is {sp.add(a,b)}")

sp.calculator()

data = [1, 12, 3, 4, 5, 6, 7, 7,7, 18, 9,9, 10]
sp.plot_histogram(data)