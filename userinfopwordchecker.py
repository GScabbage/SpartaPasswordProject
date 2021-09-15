class uipchecker:
    def compare(self, userdata, password):
        if any(info in password for info in userdata):
            print("Your password contains some of your personal information")
        else:
            print("Your password is clean")
