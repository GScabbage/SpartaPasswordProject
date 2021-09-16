import random
# Below are the characters, numbers, and symbols that are allowed in the password.
char_lower= "abcdefghijklmnopqrstuvwxyz"
char_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
sym = "!@$%^&*()-_=+[{}]|<,.>/?"
num = "123456789"
#Below are the required lengths and number of special characters in the generated password.
min_pass_length = 5
required_char_lower=1
required_char_upper=1
required_char_sym=1
required_char_num=1

while 1:
    password_len = int(input("what length would you like your password to be?  :"))
    if password_len > min_pass_length:#The password_len has to be greater than the min_pass_length otherwise it will go to the else: at the bottom of the code.

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

        print("Here is your password:  ", password)
        print("---------------------")
        print("---------------------")
        regen = str(input("Would you like to generate another password?     y/n  :"))
        if regen.lower() == 'y':
            continue
            #print("you pressed yes")
        else:
            print("Goodbye")
            break
    else:
        print("Please enter more than", min_pass_length, "characters")
