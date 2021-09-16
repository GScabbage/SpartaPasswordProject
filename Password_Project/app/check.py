from app.userinfo import userinfoclass
infoget=userinfoclass()
from app.userinfopwordchecker import uipchecker
infocheck=uipchecker()
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
                newinfo = infoget.gatherinfo()
                return newinfo

            elif response == 2:
                retrieve_info = infoget.userdataretrieve()
                return retrieve_info
            else:
                print("Invalid Entry")
                return

    def common_pw_check(self):

        ui = self.question()
        while True:
            pw = input("What password would you like to check the list for? : \n")

            use = infocheck.compare(ui, pw)
            if use == 1:
                print("Your password contains some of your personal information")
            else:
                print("Your password is clean of your user information")
            com = self.list_check(pw)
            if com ==1:
                print ("This password has been marked as either a common password or contains a common password")
            else:
                print("This password does not appear to be a common password, please check your password policy before you use it ")
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
                return


    def list_check(self,password):
        common_pw_file = open("app/Top 1 Million Passwords.txt").read().splitlines()
        if any(info in password for info in common_pw_file):
            return 1
        else:
            return 0

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
