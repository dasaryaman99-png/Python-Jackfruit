import random

# ASCII art for moves
rock = '''
      ______
-----'  ____)
       (_____)
       (_____)
       (_____)
---.___(____)
       '''

paper = '''
    _____
---'  ___)____
          _____)
          _______)
         _______)
----_______)
'''

scissors = '''
    ____
---'   _)_______
          ______)
       _________)
      (___)
---._(___)
'''

game_images = [rock, paper, scissors]
move_names = ["Rock", "Paper", "Scissors"]

# Score counters
player_wins = 0
computer_wins = 0
ties = 0
rounds = 0

# Move count trackers
player_moves = [0, 0, 0]
computer_moves = [0, 0, 0]

# Streak counters
current_streak = 0
best_streak = 0

print("Welcome to Rock-Paper-Scissors !")
print("Enter 0 for Rock, 1 for Paper, 2 for Scissors")
print("Or type r/p/s. Type 'score' to view stats. Type 'q' to quit.\n")

while True: # while loop is being used so that the game continues till the user wants to quit.
    user_input = input("Your move (0/1/2 or r/p/s): ").lower()

    # Quit
    if user_input == 'q':
        print("\nFinal Summary:")
        print("Rounds played:", rounds)
        print("You won:", player_wins)
        print("Computer won:", computer_wins)
        print("Ties:", ties)
        print("Your move counts -> Rock:", player_moves[0], "Paper:", player_moves[1], "Scissors:", player_moves[2])
        print("Computer move counts -> Rock:", computer_moves[0], "Paper:", computer_moves[1], "Scissors:", computer_moves[2])
        print("Your best winning streak:", best_streak)

        if player_wins > computer_wins:
            print("Overall result: YOU WIN the match!")
        elif player_wins < computer_wins:
            print("Overall result: COMPUTER WINS the match.")
        else:
            print("Overall result: It's a tie match.")

        print("Goodbye!")
        break

    # Show score
    if user_input == "score":
        print("\n--- Current Stats ---")
        print("Rounds played:", rounds)
        print("You:", player_wins)
        print("Computer:", computer_wins)
        print("Ties:", ties)
        print("Your move usage -> Rock:", player_moves[0], ", Paper:", player_moves[1], ", Scissors:", player_moves[2])
        print("Best winning streak:", best_streak)
        print("---------------------\n")
        continue

    # Convert r/p/s to 0/1/2
    if user_input == 'r':
        user_choice = 0
    elif user_input == 'p':
        user_choice = 1
    elif user_input == 's':
        user_choice = 2
    else:
        # Try checking if it is a number
        if user_input.isdigit():
            num = int(user_input)
            if num >= 0 and num <= 2:
                user_choice = num
            else:
                print("Invalid number! Must be 0, 1, or 2.\n")
                continue
        else:
            print("Invalid input! Try again.\n")
            continue

    # Update usage count
    player_moves[user_choice] += 1

    # Show player's move
    print("\nYou chose:", move_names[user_choice])
    print(game_images[user_choice])

    # Computer choice
    computer_choice = random.randint(0, 2)
    computer_moves[computer_choice] += 1

    print("Computer chose:", move_names[computer_choice])
    print(game_images[computer_choice])

    rounds += 1

    # Determine winner
    if user_choice == computer_choice:
        print("It's a tie!\n")
        ties += 1
        current_streak = 0

    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):

        print("You WIN this round!\n")
        player_wins += 1
        current_streak += 1

        if current_streak > best_streak:
            best_streak = current_streak
    else:
        print("You LOSE this round.\n")
        computer_wins += 1
        current_streak = 0

    # After each round show a mini-scoreboard
    print("Scoreboard after", rounds, "round(s):")
    print("You:", player_wins, " | Computer:", computer_wins, " | Ties:", ties)
    print("Your best streak:", best_streak)
    print("\n---------------------------------------\n")
