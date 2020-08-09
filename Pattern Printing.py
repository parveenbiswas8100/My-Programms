print("**********Welcome to Pattern Printing**********")
while(True):
    user_Put = int(input("Enter your number:\n"))
    bool_Put = input("1 for True Or 0 for False:\n")

    if bool_Put=='1':
        for item in range(0,user_Put+1):
            print("*"*int(item))
    elif bool_Put=='0':
        for item in range(user_Put,0,-1):
            print("*"*int(item))
    else:
        print("Error!!!!")
        break
    use_again = str(input("Do you want to print again(y/n):\n"))
    if use_again=='y':
        continue
    else:
        break