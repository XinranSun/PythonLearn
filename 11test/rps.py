import sys
import random
from enum import Enum


def rps(name="player"):
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
                if __name__ == "__main__":
                    sys.exit("bye")
                else:
                    return

    return play_rps


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personalized game experience."
    )

    parser.add_argument(
        '-n', '--name', metavar='name',
        required=True, help='The name of the person playing the game.'
    )

    args = parser.parse_args()

    rock_paper_scissors = rps(args.name)
    rock_paper_scissors()
# import sys
# import random
# from enum import Enum


# def rps(name='PlayerOne'):
#     game_count = 0
#     player_wins = 0
#     python_wins = 0
#
#     def play_rps():
#         nonlocal name
#         nonlocal player_wins
#         nonlocal python_wins
#
#         class RPS(Enum):
#             ROCK = 1
#             PAPER = 2
#             SCISSORS = 3
#
#         playerchoice = input(
#             f"\n{name}, please enter... \n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n")
#
#         if playerchoice not in ["1", "2", "3"]:
#             print(f"{name}, please enter 1, 2, or 3.")
#             return play_rps()
#
#         player = int(playerchoice)
#
#         computerchoice = random.choice("123")
#
#         computer = int(computerchoice)
#
#         print(f"\n{name}, you chose {str(RPS(player)).replace('RPS.', '').title()}.")
#         print(
#             f"Python chose {str(RPS(computer)).replace('RPS.', '').title()}.\n"
#         )
#
#         def decide_winner(player, computer):
#             nonlocal name
#             nonlocal player_wins
#             nonlocal python_wins
#             if player == 1 and computer == 3:
#                 player_wins += 1
#                 return f"🎉 {name}, you win!"
#             elif player == 2 and computer == 1:
#                 player_wins += 1
#                 return f"🎉 {name}, you win!"
#             elif player == 3 and computer == 2:
#                 player_wins += 1
#                 return f"🎉 {name}, you win!"
#             elif player == computer:
#                 return "😲 Tie game!"
#             else:
#                 python_wins += 1
#                 return f"🐍 Python wins!\nSorry, {name}.. 😢"
#
#         game_result = decide_winner(player, computer)
#
#         print(game_result)
#
#         nonlocal game_count
#         game_count += 1
#
#         print(f"\nGame count: {game_count}")
#         print(f"\nPython wins: {python_wins}")
#         print(f"\n{name}'s wins: {player_wins}")
#
#         print(f"\nPlay again, {name}?")
#
#         while True:
#             playagain = input("\nY for Yes or \nQ to Quit\n")
#             if playagain.lower() not in ["y", "q"]:
#                 continue
#             else:
#                 break
#
#         if playagain.lower() == "y":
#             return play_rps()
#         else:
#             print("\n🎉🎉🎉🎉")
#             print("Thank you for playing!\n")
#             if __name__ == "__main__":
#                 sys.exit(f"Bye {name}! 👋")
#             else:
#                 return
#
#     return play_rps
#
#
# if __name__ == "__main__":
#     import argparse
#
#     parser = argparse.ArgumentParser(
#         description="Provides a personalized game experience."
#     )
#
#     parser.add_argument(
#         '-n', '--name', metavar='name',
#         required=True, help='The name of the person playing the game.'
#     )
#
#     args = parser.parse_args()
#
#     rock_paper_scissors = rps(args.name)
#     rock_paper_scissors()
