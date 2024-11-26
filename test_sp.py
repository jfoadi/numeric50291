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
    print(f"The product of {a} and {b} is {sp.add(a,b)}")


print(sp.mean([1,2,3,4,5]))
print(sp.median([1,2,3,4,5]))
print(sp.std_dev([1,2,3,4,5]))


#sp.plot_histogram([ f for f in range(100)])
sp.interface_funciton()