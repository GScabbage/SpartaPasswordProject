from app.check import Pass_Check
pc=Pass_Check()
from app.userinfo import userinfoclass
ui=userinfoclass()
from app.password_gen import passwordgenclass
pg=passwordgenclass()

class Homepage:

    #def __init__(self):
    #    print ("self")


    def function_choice(self):
        try:
            function = int(input("Please choose one of the above options to select the function you would like to use :\n"))

            while function not in [1,2,3]:
                print()
                print("You have not selected a valid option, please re-enter your choice :\n")
                function = int(input("Please choose one of the above options to select the function you would like to use :\n"))

            if function == 1:
                pc.common_pw_check()

            elif function == 2:
                pg.gen()

            elif function == 3:
                print()
                exit("Thank you for using the app")

        except ValueError:
            print()
            print ("You have not selected a valid option, please re-enter your choice :\n")
            print()
            self.function_choice()



    def welcome(self):
        while True:
            print("Welcome to the password Analyser/Generator")
            print()
            print("1. Password Analyser")
            print("2. Password Generator")
            print("3. Exit Application")
            print()
            self.function_choice()
