class uipchecker:
    def compare(self, userdata, password):
        while True:
            if any(info in password for info in userdata):
                print("Your password contains some of your personal information")
                return 1
            else:
                print("Your password is clean")
                return 0
