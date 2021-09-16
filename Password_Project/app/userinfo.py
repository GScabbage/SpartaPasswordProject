import sqlite3
from contextlib import closing

class userinfoclass:
    def checkvalid(cls,t):
        while True:
            check = input("Is the above correct?(y/n) ")
            if check.lower() == "y":
                print ("Great! next")
                return False
                break
            elif check.lower() == "n":
                print("ok, please re-enter data")
                return True
                break
            else:
                print("Error, ivalid option entered")

    def dayofb(self):

        while True:
            try:
                dayofb = int(input("Please enter day of birth: "))
                if (len(str(dayofb))==2 or len(str(dayofb))==1) and dayofb in range(1,32):
                    print (dayofb)
                    return dayofb
                else:
                    print ("date of birth outside of range")

            except:
                print("The data you entered was invalid, please enter an integer between 1-31")
    def monthofb(self):
        while True:
            try:
                monthofb = int(input("Please enter month of birth: "))
                if (len(str(monthofb))==2 or len(str(monthofb))==1) and monthofb in range(1,13):
                    print (monthofb)
                    return monthofb
                else:
                    print ("Month of birth can't exist on earth")

            except:
                print("The data you entered was invalid, please enter an integer between 1-12")

    def yearofb(self):
        while True:
            try:
                yearofb = int(input("Please enter year of birth: "))
                if (len(str(yearofb))==4) and yearofb >=1903 and yearofb <=2021:
                    print (yearofb)
                    return yearofb
                else:
                    print ("Year of birth can't exist, you are either dead or not born")

            except:
                print("The data you entered was invalid, please enter an integer between 1903-2021")

    def senduserdb(self, infodump):
        try:
            with closing(sqlite3.connect("users.db")) as connection:
                with closing(connection.cursor()) as cursor:
                    cursor.execute("CREATE TABLE user_info (id INTEGER PRIMARY KEY, FirstName TEXT, LastName TEXT, DayofBirth TEXT, MonthofBirth TEXT, YearofBirth TEXT, MoBtxt TEXT, YoBl2 TEXT);")
                    connection.commit()
        except:
            pass
        with closing(sqlite3.connect("users.db")) as connection:
            with closing(connection.cursor()) as cursor:
                cursor.execute("INSERT INTO user_info (FirstName, LastName, DayofBirth, MonthofBirth, YearofBirth, MoBtxt, YoBl2) VALUES (?,?,?,?,?,?,?)",(infodump[0],infodump[1],infodump[2],infodump[3],infodump[4],infodump[5],infodump[6],))
                connection.commit()
    def gatherinfo(self):
        t=True
        while t==True:
            fn = input("Please enter first name: ")
            ln = input("Please enter last name: ")
            print (fn, ln)
            t = self.checkvalid(t)
            if t==False:
                break
            else:
                pass
        d=True
        while d==True:
            dfb = self.dayofb()
            mfb = self.monthofb()
            yfb = self.yearofb()
            print(dfb,'/',mfb,'/',yfb)
            d=self.checkvalid(d)

            if d==False:
                break
            else:
                pass

        while True:
            if mfb==2 and dfb>=29:
                leapyears = [1904, 1908, 1912, 1916, 1920, 1924, 1928, 1932, 1936, 1940, 1944, 1948, 1952, 1956, 1960, 1964, 1968, 1972, 1976, 1980, 1984, 1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016, 2020]
                if yfb in leapyears and dfb==29:
                    print("I see you are a rare leap year baby")
                    break
                else:
                    print ("That day isn't in February!")
                    dfb = self.dayofb()
            elif mfb in [4,6,9,11] and dfb==31:
                print("Your birth month has 30 days not 31!")
                dfb=self.dayofb()
            else:
                print("That all looks great, Thank You!")
                break

        userinfolist =[fn.lower(),ln.lower(),str(dfb),str(mfb),str(yfb)]
        if mfb == 1:
            userinfolist.append("jan")
        elif mfb == 2:
            userinfolist.append("feb")
        elif mfb == 3:
            userinfolist.append("mar")
        elif mfb == 4:
            userinfolist.append("apr")
        elif mfb == 5:
            userinfolist.append("may")
        elif mfb == 6:
            userinfolist.append("jun")
        elif mfb == 7:
            userinfolist.append("jul")
        elif mfb == 8:
            userinfolist.append("oct")
        elif mfb == 9:
            userinfolist.append("sep")
        elif mfb == 10:
            userinfolist.append("oct")
        elif mfb == 11:
            userinfolist.append("nov")
        else:
            userinfolist.append("dec")
        userinfolist.append(str(yfb)[-2:])
        #print(userinfolist)
        self.senduserdb(userinfolist)
        return userinfolist
    def userdataretrieve(self):
        while True:
            fn=input("Please enter your first name: ")
            ln=input("Please enter your last name: ")
            with closing(sqlite3.connect("users.db")) as connection:
                with closing(connection.cursor()) as cursor:
                    cursor.execute("SELECT * FROM user_info WHERE FirstName=? and LastName=?", (fn,ln,))
                    udat= cursor.fetchone()
                    if udat==None:
                        print("No data found")
                        n=input("Search again?(y/n) ")
                        if n.lower()=="y":
                            print ("Resetting")
                        else:
                            break
                    else:
                        udat = list(udat)
                        id = udat.pop(0)
                        return udat
