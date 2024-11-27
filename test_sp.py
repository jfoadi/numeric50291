###
## test package
###

import simple_package as sp

if __name__ == '__main__':

    # Welcome text
    print('')
    print('Hi, welcome to the basic online calculator!')
    print('')

    # Taking in the details needed for the wanted calculation 
    a = input("> Enter the first number 'a': ")
    b = input("> Enter the second number 'b': ")
    SelectedOpperation = input("> Enter the operation you want to perform (+, -, *, /): ")
    
    quit = False  # Making a boolian variable which changes to True when the user wants to quit

    while quit == False:
        try:  # Checking if a,b are numbers, if not give an error message given in the except block

            a = float(a)
            b = float(b)
            if SelectedOpperation == '+': # If they have asked for addition
                print(f"The sum {a} + {b} is {sp.add(a,b)}")
            elif SelectedOpperation == '-': # If they have asked for subtraction
                print(f"The subtraction {a} - {b} is {sp.subtract(a,b)}")
            elif SelectedOpperation == '*': # If they have asked for multiplication
                print(f"The product {a} * {b} is {sp.multiply(a,b)}")
            elif SelectedOpperation == '/': # If they have asked for division
                print(f"The divition {a} / {b} is {sp.divide(a,b)}")
            else:
                print("Sorry, you have entered an invalid operation.")
                QuitOrNot = input('> Would you like to leave the program? (yes/no): ')
                if QuitOrNot == 'yes':
                    quit = True


        except ValueError:
            print("Both inputs must be numbers, please try again")
            QuitOrNot = input('> Would you like to leave the program? (yes/no): ')
            if QuitOrNot == 'yes':
                quit = True

    