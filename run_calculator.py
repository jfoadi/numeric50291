###
## test package
###

import simple_package as sp
import numpy as np

if __name__ == '__main__':
    
    quit = False   # Making a boolian variable which changes to True when the user wants to quit
    
    while quit == False:
        
        print('\nHi, welcome to this maths help package!')
        mode = input('> Would you like to use the calculator or the stats helper? (calc/stats)')

        if mode == 'calc':

            print('\nWelcome to the basic online calculator!')  # Welcome text

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
                    print("\n*** ERROR: You have entered an invalid operation. ***")
                
                QuitOrNot = input('\n> Would you like to leave the helper? (yes/no): ')  # Asking the user if they want to quit
                if QuitOrNot == 'yes':  # If they want to quit, then exit calculator
                    quit = True
                elif QuitOrNot in ('no','NO','No'):  # If they do not want to quit, then continue on the calculator
                    print('\nSure! Please enter the new detials.')
                else:  # If another responce, presume they would like to quit and exit helper
                    print('\n*** ERROR: Invalid input, closing the helper ***')
                    quit = True

            except ValueError:  # If a or b are not numbers, then give an error message
                print("\n*** ERROR: Both inputs must be numbers. ***")

                QuitOrNot = input('\n> Would you like to leave the helper? (yes/no): ')
                if QuitOrNot == 'yes':  # If they want to quit, then exit calculator
                    quit = True
                elif QuitOrNot in ('no','NO','No'):  # If they do not want to quit, then continue on the calculator
                    print('\nSure! Please enter the new detials.')
                else:  # If another responce, presume they would like to quit and exit helper
                    print('\n*** ERROR: Invalid input, closing the helper ***')
                    quit = True

        elif mode == 'stats':
            print('\nWelcome to the statistics calculator!')  # Welcome text
            statsdata = input('> Please enter the data you want to use (It must be a list or a 1D numpy array!)')

            try:
                statsdata = eval(statsdata)  # Cahnge from string to list 
                statsdata  = np.array(statsdata)
                print('This data is fine')
                print(statsdata)



                QuitOrNot = input('\n> Would you like to leave the helper? (yes/no): ')
                if QuitOrNot == 'yes':  # If they want to quit, then exit calculator
                    quit = True
                elif QuitOrNot in ('no','NO','No'):  # If they do not want to quit, then continue on the calculator
                    print('\nSure! Please enter the new detials.')
                else:  # If another responce, presume they would like to quit and exit helper
                    print('\n*** ERROR: Invalid input, closing the helper ***')
                    quit = True

            except NameError:
                print('\n*** ERROR: The data must be a list or a 1D numpy array of numbers ***')

        else :  # If the user has entered an invalid mode, then give an error message
            print("\n*** ERROR: Invalid mode ***")
            print('Please try again with one of the following modes: "math" or "stats".')

    print('\nThank you for using the calcualtor, hope to see you again soon :)')
    print('')