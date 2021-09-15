#pw = ("blitz") #This will become the input

class Pass_Check:
    def __init__()
    def common_pw_check(self, ):
        pw = input("What password would you like to check the list for? : \n")

        common_pw_file = open("Top 10000 Passwords.txt").read().splitlines()
        if (pw) in (common_pw_file):
            print ("This password has been marked as a common password")
        else:
            print("This password does not appear to be a common password, please check your password policy before you use it ")
        cpc_retest(self)

    def cpc_retest(self, ):
        try:
            print("1. Retest another password")
            print("2. Go back to menu")
            retest = int(input("What would you like to do from the above options? :\n"))

            while retest not in [1,2]:
                print()
                print("1. Retest another password")
                print("2. Go back to menu")
                retest = int(input("What would you like to do from the above options? :\n"))
            if retest == 1:
                common_pw_check(self)
            elif retest == 2:
                print("this should go back to menu")
        except ValueError:
            print()
            print ("You have not selected a valid option, please re-enter your choice :\n")
            print()
            cpc_retest(self)
