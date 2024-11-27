###
## test package
###

import simple_package as sp

if __name__ == '__main__':
    
    print('\nHi, welcome to the basic online calculator!')  # Welcome text
    quit = False   # Making a boolian variable which changes to True when the user wants to quit

    while quit == False:

        # Taking in the details needed for the wanted calculation 
        a = input("\n> Enter the first number 'a': ")
        b = input("> Enter the second number 'b': ")
        SelectedOpperation = input("> Enter the operation you want to perform (+, -, *, /): ")

        try:  # Checking if a,b are numbers, if not give an error message given in the except block

            # Changing strings to a numbers, if there is an error, then it will go to the exept block
            a = float(a)  
            b = float(b)

            if SelectedOpperation == '+':  # If they have asked for addition
                print(f"\nThe sum {a} + {b} is {sp.add(a,b)}")
            elif SelectedOpperation == '-':  # If they have asked for subtraction
                print(f"\nThe subtraction {a} - {b} is {sp.subtract(a,b)}")
            elif SelectedOpperation == '*':  # If they have asked for multiplication
                print(f"\nThe product {a} * {b} is {sp.multiply(a,b)}")
            elif SelectedOpperation == '/':  # If they have asked for division
                print(f"\nThe divition {a} / {b} is {sp.divide(a,b)}")
            else:  # If they have asked for something else
                print("\n** ERROR: You have entered an invalid operation. **")
            QuitOrNot = input('\n> Would you like to leave the calculator? (yes/no): ')
            if QuitOrNot == 'yes':
                quit = True
            elif QuitOrNot in ('no','NO','No'):
                print('\nSure! Please enter the new detials.')
            else:
                print('\nERROR: Invalid input, closing the calculator')
                quit = True

        except ValueError:
            print("\n** ERROR: Both inputs must be numbers. **")
            QuitOrNot = input('\n> Would you like to leave the calculator? (yes/no): ')
            if QuitOrNot == 'yes':
                quit = True
            elif QuitOrNot in ('no','NO','No'):
                print('\nSure! Please enter the new detials.')
            else:
                print('\n** ERROR: Invalid input, closing the calculator **')
                quit = True

    
    
    
    print('\nThank you for using the calcualtor, hope to see you again soon :)')
    print('')