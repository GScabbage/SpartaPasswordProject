class reportclass:
    def reportgen(self, scorelist, password):
        spassword = ''.join(char for char in password if char.isalnum())
        with open('Password_report_%s.txt' %spassword, 'w') as f:
            f.write("This is your password analysis report")
            f.write('\n')
            f.write(password)
            f.write('\n')            
            if scorelist[0] == 20:
                f.write("You got the best score in password length as you password met the 8 character requirement and exceed 12 characters for extra security")
                f.write('\n')
            elif scorelist[0] == 10:
                f.write("You got the base score in password length as you password met the 8 character requirement")
                f.write('\n')
            else:
                f.write("You got no score in password length as you password has not met the 8 character requirement")
                f.write('\n')
            if scorelist[1] == 20:
                f.write("You got the best score in lower case characters as you password met the lower case character requirement and used multiple for extra security")
                f.write('\n')
            elif scorelist[1] == 10:
                f.write("You got the base score in lower case characters as you password met the lower case character requirement")
                f.write('\n')
            else:
                f.write("You got no score in lower case characters as you password has not met the lower case character requirement")
                f.write('\n')
            if scorelist[2] == 20:
                f.write("You got the best score in upper case characters as you password met the upper case character requirement and used multiple for extra security")
                f.write('\n')
            elif scorelist[2] == 10:
                f.write("You got the base score in upper case characters as you password met the upper case character requirement")
                f.write('\n')
            else:
                f.write("You got no score in lower case characters as you password has not met the upper case character requirement")
                f.write('\n')
            if scorelist[3] == 20:
                f.write("You got the best score in numerical characters as you password met the numerical character requirement and used multiple for extra security")
                f.write('\n')
            elif scorelist[3] == 10:
                f.write("You got the base score in numerical characters as you password met the numerical character requirement")
                f.write('\n')
            else:
                f.write("You got no score in numerical characters as you password has not met the numerical character requirement")
                f.write('\n')
            if scorelist[4] == 20:
                f.write("You got the best score in special characters as you password met the special character requirement and used multiple for extra security")
                f.write('\n')
            elif scorelist[4] == 10:
                f.write("You got the base score in special characters as you password met the special character requirement")
                f.write('\n')
            else:
                f.write("You got no score in special characters as you password has not met the special character requirement")
                f.write('\n')
            if scorelist[6] == 1:
                f.write("Your Password met all the requirements of the password policy")
                f.write('\n')
            else:
                f.write("Your Password did not meet all the requirements of the password policy")
                f.write('\n')
            if scorelist[7] == 0:
                f.write("Your Password did not contain any of your personal information")
                f.write('\n')
            else:
                f.write("Your Password did contain some of your personal information")
                f.write('\n')
            if scorelist[8] == 0:
                f.write("Your Password did not contain a common password")
                f.write('\n')
            else:
                f.write("Your Password did contain a common password")
                f.write('\n')
            if scorelist[5] <= 60 and scorelist[6] == 1:
                f.write("Your password strength is weak as it achieved 60 or less points")
            elif scorelist[5]> 60 and scorelist[5] <= 80 and scorelist[6] == 1:
                f.write("Your password strength is medium as it achieved between 61 and 80 points")
            elif scorelist[5] > 80 and scorelist[6] == 1:
                f.write("Your password strength is strong as it achieved more than 80 points")
            else:
                f.write("Your password may have scored sufficient points to be rated but it does not meet the password policy requirements")
