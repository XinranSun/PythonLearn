import random
import sys


def guess_number(player_name="John"):
    game_count = 0
    computer_wins = 0
    player_wins = 0
    percentage = 0

    def play_guess_number():
        player_input = input(f"{player_name}guess whichi number 1,2,3 : ")
        player = int(player_input)
        if player_input not in ["1", "2", "3"]:
            print("invalid input")
            return play_guess_number()

        computer_input = int(random.choice("123"))
        print(computer_input)
        nonlocal game_count
        nonlocal player_wins

        nonlocal computer_wins
        nonlocal percentage
        game_count += 1
        if player == computer_input:
            print("Congratulations! You guessed the number!")
            player_wins += 1
            print(f"computer is {computer_input}")
            percentage = (player_wins / game_count * 100).__round__(2)
            percentage = str(percentage) + "%"
            print(f"Your winning percentage is {percentage}")

        else:
            print("Sorry! You didn't guess the number.")
            computer_wins += 1

        while True:
            play_again = input("continue? y/n\n")
            if play_again.lower() == "y":
                return play_guess_number()
            else:
                if __name__ == "__main__":
                    sys.exit("bye")
                else:
                    return

    return play_guess_number


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--name", required=True, help="name of the user")
    arg = parser.parse_args()
    guess_my_number = guess_number(arg.name)
    guess_my_number()
