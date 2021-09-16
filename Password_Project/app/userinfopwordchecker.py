class uipchecker:
    def compare(self, userdata, password):
        while True:
            if any(info in password for info in userdata):
                return 1
            else:
                return 0
