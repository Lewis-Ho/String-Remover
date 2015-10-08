"""
This module demonstrates how to recursively remove given sub-string from a string
and ensure the returned string contain no whitespace and no occurences of the substring.
"""

import string

catch = 0       # Number of time of matched sub-string
stringA = ""    # Copy of sub-string for displaying at the end
stringB = ""    # Copy of string for displaying at the end


def show_result(Str):
    """ Display resulting string C and the number of time for catched string A """

    global stringA
    global stringB

    # Removed all white space before printing out result
    Str = Str.strip().replace(' ','')
    
    if (catch == 0):
        print(stringB + ' Contain No ' + stringA + '!')
        print('Final Result: ' + Str)
    else:
        print(stringB + ' Contain ' + str(catch) + ' Times of ' + stringA + ' in Total.')
        print('Final Result: ' + Str)


def remove_string(subStr, Str):
    """ Remove sub-string from a string and perform another sub-string check if neccessary """
    
    index = Str.find(subStr)

    # Only remove sub-string if find function catch the right string, then advance to next search 
    if (len(subStr) > len(Str)):
        show_result(Str)
    else:
        # Find no match sub-string
        if (index == -1):
            show_result(Str)
        else:
            global catch
            catch += 1
            Str = Str[:index] + Str[len(subStr)+index:]
            print('Sub-String Removed. Currently String C is: ' + Str)
            remove_string(subStr,Str)
        

def ask_for_continue():
    """ Take input from client for continuing new problem set """
    
    flag = True
    
    while ( flag ) :
        again = raw_input('Do You Want to Continue? (Y For Yes, N For No)')
        if (again == 'Y'):
            # Reset
            global catch
            catch = 0
            flag = False
            return True
        elif (again == 'N'):
            print('Thank You For Your Time. See You!')
            flag = False
            return False
        else:
            print('You Sure Your Input is Correct?')


def main():
    """ Take input as string A and B """
    
    global stringA
    global stringB
    start = True

    while(start == True):
        stringA = raw_input('Please Enter String A: ')
        stringB = raw_input('Please Enter String B: ')

        # Handle special cases
        if (stringA == ''):
            if (stringB == ''):
                print("Can't Compare Empty String with Empty String.")
            else:
                show_result(stringB)
        else:
            if (len(stringA) <= len(stringB)):
                remove_string(stringA,stringB)
            else:
                show_result(stringB)

        # Ask client for continue if there is new problem set
        start = ask_for_continue()


if __name__ == "__main__":
    main()
