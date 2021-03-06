import random
from app.userinfo import userinfoclass
infoget=userinfoclass()
from app.userinfopwordchecker import uipchecker
infocheck=uipchecker()
from app.check import Pass_Check
gencheck=Pass_Check()

class passwordgenclass:
    def question(self):
        while True:
            print()
            print("1. Enter new info")
            print("2. Retrieve existing info\n")
            response = input("Which do you want to do? :\n")

            if response == "1":
                newinfo = infoget.gatherinfo()
                return newinfo

            elif response == "2":
                retrieve_info = infoget.userdataretrieve()
                if retrieve_info == None:
                    pass
                else:
                    return retrieve_info
            else:
                print("Invalid Entry")
                pass

    def gen(self):
        ui = self.question()
        while True:
            while True:
                password_len = int(input("what length would you like your password to be?  :"))
                min_pass_length = 8
                if password_len >= min_pass_length:
                    password = self.passgen(password_len, ui)
                    break
                else:
                    print("Please enter more than", min_pass_length, "characters")
            print("Here is your password:  ", password)
            print("---------------------\n")
            print("1.Generate a new password")
            print("2.Go back to home menu\n")
            regen = int(input("Would you like to do? :"))
            if regen == 1:
                continue
            elif regen == 2:
                print("Thanks for using the password generator\n")
                break
            else:
                print("Please enter a valid response")

    def passgen(self, password_len, userinfo):
        char_lower= "abcdefghijklmnopqrstuvwxyz"
        char_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        sym = "!@$%^&*()-_=+[{}]|<,.>/?"
        num = "123456789"
        #Below are the required lengths and number of special characters in the generated password.

        required_char_lower=1
        required_char_upper=1
        required_char_sym=1
        required_char_num=1

        passlen_prime = password_len
        while True:
            password_len = passlen_prime
            password = ""
            if required_char_lower > 0:
                for x in range(0,required_char_lower):
                    password = password + random.choice(char_lower)
            if required_char_upper > 0:
                for x in range(0,required_char_upper):
                    password = password + random.choice(char_upper)
            if required_char_sym > 0:
                for x in range(0,required_char_sym):
                    password = password + random.choice(sym)
            if required_char_num > 0:
                for x in range(0,required_char_num):
                    password = password + random.choice(num)

                    password_len = password_len - required_char_lower - required_char_upper - required_char_num - required_char_sym
    #Below will randomise the order of the uppercase lowercase symbols and numbers
            for x in range(0,password_len):
                randomiser = random.randint(1,4)
                if randomiser == 1:
                    password = password + random.choice(char_lower)
                elif randomiser == 2:
                    password = password + random.choice(char_upper)
                elif randomiser == 3:
                    password = password + random.choice(sym)
                elif randomiser == 4:
                    password = password + random.choice(num)
    #Below will join the different items together randomly to form one string.
            password = ''.join(random.sample(password, len(password)))
            uservalid = infocheck.compare(userinfo, password)
            listvalid = gencheck.list_check(password)
            if listvalid != 1 and uservalid != 1:
                return password
