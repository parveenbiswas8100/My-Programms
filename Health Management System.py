import datetime

def getdate():
    return datetime.datetime.now()

while(True):
    print("******** Select your View ********")
    print("1. Add Client Details")
    print("2. View Clients Details")

    user_cli = input("Enter your Number(1/ 2):\n")

    if user_cli=='1':
        print("****** LIST OF THE CLIENTS ******")
        print("1. Parveen Biswas")
        print("2. Gaurav Biswas")
        print("3. Rupesh Singh")

        add_cli = input("Enter your Client Number(1/ 2/ 3):\n")

        if add_cli=='1':
            print("1. Diet_lock")
            print("2. Exercise_lock")

            user_put = input("Enter your chosien Number(1/ 2):\n")

            if user_put=='1':
                user_die = str(input("Enter your Diet:\n"))
                die = user_die + "\n"
                with open("par_Diet.txt", "a") as f:
                    f.write(str([str(getdate())])+ " :  " + die)
                    print("Successfully Written")

            elif user_put=='2':
                user_exe = str(input("Enter your Exercise:\n"))
                exe = user_exe + "\n"
                with open("par_Exercise.txt", "a") as f:
                    f.write(str([str(getdate())])+ " :  " + exe)
                    print("Successfully Written")

        if add_cli=='2':
            print("1. Diet_lock")
            print("2. Exercise_lock")

            user_put = input("Enter your chosien Number(1/ 2):\n")

            if user_put=='1':
                user_die = str(input("Enter your Diet:\n"))
                die = user_die + "\n"
                with open("gau_Diet.txt", "a") as f:
                    f.write(str([str(getdate())])+ " :  " + die)
                    print("Successfully Written")

            elif user_put=='2':
                user_exe = str(input("Enter your Exercise:\n"))
                exe = user_exe + "\n"
                with open("gau_Exercise.txt", "a") as f:
                    f.write(str([str(getdate())])+ " :  " + exe)
                    print("Successfully Written")


        if add_cli=='3':
            print("1. Diet_lock")
            print("2. Exercise_lock")

            user_put = input("Enter your chosien Number(1/ 2):\n")

            if user_put=='1':
                user_die = str(input("Enter your Diet:\n"))
                die = user_die + "\n"
                with open("rup_Diet.txt", "a") as f:
                    f.write(str([str(getdate())])+ " :  " + die)
                    print("Successfully Written")

            elif user_put=='2':
                user_exe = str(input("Enter your Exercise:\n"))
                exe = user_exe + "\n"
                with open("rup_Exercise.txt", "a") as f:
                    f.write(str([str(getdate())])+ " :  " + exe)
                    print("Successfully Written")

    elif user_cli=='2':
        print("****** LIST OF THE CLIENTS ******")
        print("1. Parveen Biswas")
        print("2. Gaurav Biswas")
        print("3. Rupesh Singh")

        add_cli = input("Enter your Client Number(1/ 2/ 3):\n")

        if add_cli == '1':
            print("1. Diet_lock")
            print("2. Exercise_lock")

            user_put = input("Enter your chosien Number(1/ 2):\n")

            if user_put == '1':
                with open("par_Diet.txt", "rt") as f:
                    a = f.readlines()
                    print(a)

            elif user_put == '2':
                with open("par_Exercise.txt", "rt") as f:
                    a = f.readlines()
                    print(a)

        if add_cli == '2':
            print("1. Diet_lock")
            print("2. Exercise_lock")

            user_put = input("Enter your chosien Number(1/ 2):\n")

            if user_put == '1':
                with open("gau_Diet.txt", "rt") as f:
                    a = f.readlines()
                    print(a)

            elif user_put == '2':
                with open("gau_Exercise.txt", "rt") as f:
                    a = f.readlines()
                    print(a)

        if add_cli == '3':
            print("1. Diet_lock")
            print("2. Exercise_lock")

            user_put = input("Enter your chosien Number(1/ 2):\n")

            if user_put == '1':
                with open("rup_Diet.txt", "rt") as f:
                    a = f.readlines()
                    print(a)

            elif user_put == '2':
                with open("rup_Exercise.txt", "rt") as f:
                    a = f.readlines()
                    print(a)
    else:
        break
    re_aga = str(input("Do you want to repeat again(y/n):\n"))
    if re_aga=='y':
        continue
    else:
        break