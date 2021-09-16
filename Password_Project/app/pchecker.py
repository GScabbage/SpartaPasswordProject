import re

class passrep:
    password = (input(" Enter your password: "))
    #length = str(len(password))
    digits = len(re.findall(r'[0-9]', password))
    score = 0
    def scoreinc(cls):
        cls.score+=10

    def length_character(self, password):
        password_length_good = False
        if len (password) < 8:
            print("[!] Password should be atleast 8 characters long")
            print("[!] Password is only", length, "characters long" )
            password_length_good = False;

        else:
                print("(*) Your password is", length, "characters :)  ")
                password_length_good = True;

                if password_length_good == True:
                    self.scoreinc()
                    #global score
                    #score += 10

    #length_character(password)

    #

    # working
    def uppercase_character(self, password):
        UpperLength = len(re.findall(r'[A-Z]', password))
        print("(*) Your password contains", UpperLength, "uppercase characters")
        password_char_good = False

        if UpperLength > 0:
            password_char_good = True;

        if UpperLength == 0:
            print("[!] Your password should have atleast 1 uppercase character!")

        if password_char_good == True:
            #global score
            #score += 10
            self.scoreinc()

    #uppercase_character(password)

    #

    #working
    def num_digits(self, password):
        password_num_good = False
        digits = len(re.findall(r'[0-9]', (password)))
        print("(*) Your password contains", digits, "numeric digits")

        if digits == 0:
            print("[!] Your password should have atleast 1 Number!")

        if digits > 0:
            password_num_good = True

        if password_num_good == True:
            #global score
            #score += 10
            self.scoreinc()
    #num_digits(password)



    #
    #working
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
        if special_char >= 1:
            print("(*) You have {} Special Character/s in your password ".format(special_char))
        else:
            print("[!] Your password should have atleast 1 special character!")

        if special_char > 0:
            password_special_good = True

        if password_special_good == True:
            #global score
            #score += 10
            self.scoreinc()


    if __name__ == '__main__' :
        string = password
    #count_special_character(password)


    def score_total(self):

        if score < 19:
            print("your password is weak")

        elif score <= 19 <= 30:
            print("your password strength is medium")
        elif score > 30:
            print("your password is strong")

    def policycheck(self):

    #score_total(score)
