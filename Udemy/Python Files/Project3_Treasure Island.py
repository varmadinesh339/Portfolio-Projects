print("""Welcome to todays Treacher Island game.
You Mission is to find the tresure.""")

a ="Please choose you first choice to go Right or Left ? "
choice = input(a)

choice = choice.lower();
if choice == "r" or choice == "right":
    print("Sorry you fell into a hole and game is over")
elif choice == "left" or choice == "l" :
    a ="""You have Reached a lake 
    Please make a choice between swim or wait for a boat"""
    choice =input(a)
    choice = choice.lower()
    if choice == "swim" or choice == "S":
        print("Sorry the Lake was very lengthy and are dead due to exhaustion. Game Over.")
    elif choice == "wait" or choice == "w":
        print("You have chossen to wait for a boat and then used it to pass the lake")

        a = "After passing the lake you encounter three doors one Yellow, Red and Blue "
        choice = input(a)
        choice = choice.lower()

        if choice == "yellow" or choice == "y" :
            print("You have won the treasure chest")
        else :
            print("You have found a empty room and lost the game.")
