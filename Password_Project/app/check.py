from app.userinfo import userinfoclass
ii=userinfoclass()
from app.userinfopwordchecker import uipchecker
oo=uipchecker()
from app.pchecker import passrep
pp=passrep()
from app.reportexporter import reportclass
rep=reportclass()
#def classname  = new Pass_Check
#classname.test
class Pass_Check:
    #def __init__(self):

    def question(self):

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
        while True:
            pw = input("What password would you like to check the list for? : \n")

            use = oo.compare(ui, pw)
            if use == 1:
                print("Your password contains some of your personal information")
            else:
                print("Your password is clean of your user information")
            com = self.list_check(pw)
            replist = pp.policycheck(pw,use,com)

            while True:
                getrep=input("Would you like to generate a detailed report about your password? (y/n)")
                if getrep.lower() == "y":
                    rep.reportgen(replist,pw)
                    break
                elif getrep.lower() == "n":
                    break
                else:
                    print("Invalid option selected")

            re = self.cpc_retest()
            if re == 1:
                print("Retesting")

            elif re == 2:
                print("this should go back to menu")
                return




    def list_check(self,password):
        common_pw_file = open("app/Top 10000 Passwords.txt").read().splitlines()
        if any(info in password for info in common_pw_file):
            print ("This password has been marked as either a common password or contains a common password")
            return 1
        else:
            print("This password does not appear to be a common password, please check your password policy before you use it ")
            return 0
#        self.cpc_retest()

    def cpc_retest(self):

        while True:
            print()
            print("1. Retest another password")
            print("2. Go back to menu")
            retest = int(input("What would you like to do from the above options? :\n"))
            if retest == 1 or 2:
                return retest
            else:
                print()
                print ("You have not selected a valid option, please re-enter your choice :\n")
                print()
