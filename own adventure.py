while True:

    name = input("Type your name: ")
    print(f"Welcome {name} to this adventure!")

    answer= input(
    "You are on a dirt road. It has come to an end.\n"
        "You can go left or right. Which way would you like to go? "
    ).lower()

    if answer == "left":

        answer = input(
            "You come to a river. Do you want to walk around it or swim across?\n"
            "Type 'walk' or 'swim': "
        ).lower()

        if answer == "swim":
            print("You swam across and were eaten by an alligator. You lose!")

        elif answer == "walk":
            print("You walked for many miles, ran out of water, and lost the game!")

        else:
            print("Not a valid option. You lose!")

    elif answer == "right":

        answer= input(
            "You come to a bridge. It looks wobbly.\n"
            "Do you want to cross it or go back?\n"
            "Type 'cross' or 'back': "
        ).lower()

        if answer == "back":
            print("You go back and lose!")

        elif answer == "cross":

            answer= input(
                "You cross the bridge and meet a stranger.\n"
                "Do you talk to them? (yes/no): ").lower()

            if answer == "yes":
                print("You talk to the stranger. They give you gold. You win!")

            elif answer == "no":
                print("You ignore the stranger. They are offended. You lose!")

            else:
                print("Not a valid option. You lose!")

        else:
            print("Not a valid option. You lose!")

    else:
        print("Not a valid option. You lose!")

    again= input("\nDo you want to play again? (yes/no): ").lower()
    if again != "yes":
        print("Thanks for playing!")
        break