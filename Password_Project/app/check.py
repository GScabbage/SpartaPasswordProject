from app.userinfo import userinfoclass
ii=userinfoclass()
from app.userinfopwordchecker import uipchecker
oo=uipchecker()

#def classname  = new Pass_Check
#classname.test
class Pass_Check:
    def __init__(self):
        print ("self")

    def question(self):
        #print("1. Enter new info")
        #print("2. Retrieve existing info")

        #response = int(input("Which do you want to do? :"))

        while True:
            print()
            print("1. Enter new info")
            print("2. Retrieve existing info")
            response = int(input("Which do you want to do? :\n"))

            if response == 1:
                print("NEW INFO")
                newinfo = ii.gatherinfo()
                return newinfo

            elif response == 2:
                print("RETRIEVE")
                retrieve_info = ii.userdataretrieve()
                return retrieve_info
            else:
                print("Invalid Entry")
                return





    def common_pw_check(self):

        ui = self.question()

        print(ui)

        pw = input("What password would you like to check the list for? : \n")

        oo.compare(ui, pw)

        common_pw_file = open("app/Top 10000 Passwords.txt").read().splitlines()
        if (pw) in (common_pw_file):
            print ("This password has been marked as a common password")
        else:
            print("This password does not appear to be a common password, please check your password policy before you use it ")
        self.cpc_retest()

    def cpc_retest(self):
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
                self.common_pw_check()
            elif retest == 2:
                print("this should go back to menu")
                return

        except ValueError:
            print()
            print ("You have not selected a valid option, please re-enter your choice :\n")
            print()
            self.cpc_retest()
