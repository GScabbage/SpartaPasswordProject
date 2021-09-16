import re

class passrep:

    def length_character(self, password):
        length = str(len(password))
        print("(*) Your password is", length, "characters :)  ")
        if len (password) >= 8 and len(password) < 12:
            return 10
        elif len(password) >=12:
            return 20
        else:
            print("[!] Password should be atleast 8 characters long")
            return 10


    def lowercase_character(self, password):
        LowerLength = len(re.findall(r'[a-z]', password))
        print("(*) Your password contains", LowerLength, "lowercase characters")

        if LowerLength == 1:
            return 10
        elif LowerLength >= 2:
            return 20
        else:
            print("[!] Your password should have atleast 1 lowercase character!")
            return 0

    def uppercase_character(self, password):
        UpperLength = len(re.findall(r'[A-Z]', password))
        print("(*) Your password contains", UpperLength, "uppercase characters")

        if UpperLength == 1:
            return 10
        elif UpperLength >= 2:
            return 20
        else:
            print("[!] Your password should have atleast 1 uppercase character!")
            return 0

    def num_digits(self, password):
        password_num_good = False
        digits = len(re.findall(r'[0-9]', (password)))
        print("(*) Your password contains", digits, "numeric digits")

        if digits == 1:
            return 10
        elif digits >= 2:
            return 20
        else:
            print("[!] Your password should have atleast 1 Number!")
            return 0



    def count_special_character(self, password):
        password_special_good = False

        special_char= 0
        for i in range(0, len(password)):
            if (password[i].isalpha()):
                continue
            elif (password[i].isdigit()):
                continue
            else:
                special_char += 1
        print("(*) You have {} Special Character/s in your password ".format(special_char))
        if special_char == 1:
            return 10
        elif special_char >= 2:
            return 20
        else:
            print("[!] Your password should have atleast 1 special character!")
            return 0


    if __name__ == '__main__' :
        string = password
    #count_special_character(password)

        if score < 19:
            print("your password is weak")

        elif score <= 19 <= 30:
            print("your password strength is medium")
        elif score > 30:
            print("your password is strong")

    def policycheck(self,password,user,common):
        lpoints = self.length_character(password)
        lowpoints = self.lowercase_character(password)
        uppoints = self.uppercase_character(password)
        dpoints = self.num_digits(password)
        spoints = self.count_special_character(password)
        score = lpoints + lowpoints + uppoints + dpoints + spoints
        if user == 1 and common ==1:
            score-=100
            print ("Your password lost 100 points as it containted personal information and a common password")
        elif user == 1 or common == 1:
            score-=50
            print ("Your password lost 50 points as it containted either personal information or a common password")
        else:
            pass
        print("Your password scored",score,"points!")
        if score <= 60 and (lpoints >= 10 and lowpoints >= 10 and uppoints >= 10 and dpoints >= 10 and spoints >= 10):
            print("Your password strength is weak")
            reqmet=1
        elif score > 60 and score <= 80 and (lpoints >= 10 and lowpoints >= 10 and uppoints >= 10 and dpoints >= 10 and spoints >= 10):
            print("Your password strength is medium")
            reqmet=1
        elif score > 80 and (lpoints >= 10 and lowpoints >= 10 and uppoints >= 10 and dpoints >= 10 and spoints >= 10):
            print("Your password strength is strong")
            reqmet=1
        else:
            print("Your password may have scored sufficient points to be rated but it does not meet the password policy requirements")
            reqmet=0
        return [lpoints, lowpoints, uppoints, dpoints, spoints, score, reqmet, user, common]
