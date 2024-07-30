import sys
import random
from enum import Enum


def rps():
    game_count = 0
    player_wins = 0
    computer_wins = 0

    def play_rps():
        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        playchoices = int(input("1-Rock, 2-Paper, 3-Scissors\n"))

        if playchoices not in [1, 2, 3]:
            print("invalid")
            return play_rps()
        player = int(playchoices)

        computerchoice = int(random.choice('123'))
        computer = computerchoice
        if playchoices < 1 or playchoices > 3:
            sys.exit("cuole")

        def decide_winner(player, computer):
            nonlocal player_wins
            nonlocal computer_wins
            if player == 1 and computer == 3 or player == 2 and computer == 1 or player == 3 and computer == 2:
                print("com" + str(RPS(computer)).replace("RPS.", " "))
                print(("play" + str(RPS(player)).replace("RPS.", " ")))

                player_wins += 1
                return "you win"
            elif player == computer:
                print("Draw")
                return "draw"
            else:
                print("com" + str(RPS(computer)).replace("RPS.", " "))
                print(("play" + str(RPS(player)).replace("RPS.", " ")))
                computer_wins += 1
                return "you lose"

        game_result = decide_winner(player, computer)
        print(game_result)
        nonlocal game_count
        game_count += 1
        print("\nGame count: " + str(game_count))

        while True:
            playagain = input("continue ? y/n\n")

            if playagain.lower() == "y":
                return play_rps()
            else:
                break

    return play_rps()


kaishi=rps()

if __name__ == "__main__":
    kaishi