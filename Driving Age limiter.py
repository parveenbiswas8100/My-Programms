user_put = int(input("Enter your age:\n"))

if user_put<=14:
    print("You are to small for driving...")
elif user_put==18:
    print("If you have driving license. Then drive, other wise apply for driving license")
elif user_put>18 and user_put<=70:
    print("You can drive...")
else:
    print("Drive in your own risk...")

