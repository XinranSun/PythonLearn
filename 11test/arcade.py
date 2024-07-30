import sys
from rps import rps
from guess_number import guess_number


def arcade(name):

    while True:
        print("hello", name)
        print(" choose a game:")
        print(" 1. rock paper scissors")
        print(" 2. guess_number")
        print(" 3. print x exit")
        player_choice = input()
        if player_choice not in ["1", "2", "3", "x"]:
            print("invalid")
            return arcade(name)
        if player_choice == "1":
            rock = rps(name)
            rock()
        elif player_choice == "2":

            gus = guess_number(name)
            gus()
        else:
            sys.exit()

    # welcome_back = False
    #
    # while True:
    #     if welcome_back == True:
    #         print(f"\n{name}, welcome back to the Arcade menu.")
    #
    #     playerchoice = input(
    #         "\nPlease choose a game:\n1 = Rock Paper Scissors\n2 = Guess My Number\n\nOr press \"x\" to exit the Arcade\n\n"
    #     )
    #
    #     if playerchoice not in ["1", "2", "x"]:
    #         print(f"\n{name}, please enter 1, 2, or x.")
    #         return arcade(name)
    #
    #     welcome_back = True
    #
    #     if playerchoice == "1":
    #         rock_paper_scissors = rps(name)
    #         rock_paper_scissors()
    #     elif playerchoice == "2":
    #         guess_my_number = guess_number(name)
    #         guess_my_number()
    #     else:
    #         print("\nSee you next time!\n")
    #         sys.exit(f"Bye {name}! 👋")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--name", required=True)
    arg = parser.parse_args()

    arcade(arg.name)
