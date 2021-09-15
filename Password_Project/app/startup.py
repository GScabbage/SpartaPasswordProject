from check import Pass_Check


def welcome():
    print("Welcome to the password Analyser/Generator")
    print()
    print("1. Password Analyser")
    print("2. Password Generator")
    print("3. Exit Application")
    print()

def function_choice():
    try:
        function = int(input("Please choose one of the above options to select the function you would like to use :\n"))

        while function not in [1,2,3]:
        #while function > 3 or function < 1 or:
            print()
            print("You have not selected a valid option, please re-enter your choice :\n")
            function = int(input("Please choose one of the above options to select the function you would like to use :\n"))

        if function == 1:
            #run password analyser
            print ("This was option 1")
            Pass_Check.common_pw_check(self)

        elif function == 2:
            #run password generator
            print ("This was option 2")

        elif function == 3:
            print()
            exit("Thank you for using the app")

    except ValueError:
        print()
        print ("You have not selected a valid option, please re-enter your choice :\n")
        print()
        function_choice()

welcome()
function_choice()
print()
print("The code ran all the way")
