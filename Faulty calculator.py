while (True):
    user_put1 = int(input("Enter your first number:\n"))
    user_put2 = int(input("Enter your second number:\n"))


    print("Select your Operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplition")
    print("4. Division")


    user_sym = input("Enter your Operation Number(1/ 2/ 3/ 4):\n")

    if user_put1==56 and user_put2==3:
        print("Answer is 60")
    elif user_put1==76 and user_put2==2:
        print("Answer is 12.5")
    elif user_sym=='1':
        result = user_put1 + user_put2
        print("Answer is", result)
    elif user_sym=='2':
        result = user_put1 - user_put2
        print("Answer is", result)
    elif user_sym=='3':
        result = user_put1 * user_put2
        print("Answer is", result)
    elif user_sym=='4':
        result = user_put1 / user_put2
        print("Answer is", result)
    else:
        print("check your equation...")
        break
    not1 = input("Do you want to calculate again(y/n):\n")

    if not1=='y':
        continue
    else:
        break

