print("Welcome to Guesses Game")
print("Now listen to me")
print("You have only five guesses")
print("the number in between 1 to 99")

ans_win = 97
gues = 0

while(gues<=5):
    user_put = int(input("Enter your number:\n"))
    print("You have", 5 - gues - 1, "left")
    gues = gues + 1
    if user_put<ans_win:
        print("your guess is to low...")
    elif user_put==ans_win:
        print("congrates, you won")
        print("you won in", gues, "Gues")
        break
    else:
        print("Your guess is to high...")
        continue

if gues>5:
    print("Game Over")
