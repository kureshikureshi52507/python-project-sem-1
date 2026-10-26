import random


# Function to play the game
def play_game():

    player_score = 0
    computer_score = 0

    choices = ["rock", "paper", "scissors"]

    print("\n====================================")
    print("     ROCK PAPER SCISSORS GAME")
    print("====================================")

    while True:

        print("\nChoose your option:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("4. Exit")

        user_choice = input("Enter your choice: ").lower()

        # Exit the game
        if user_choice == "4":
            break

        # Convert number choice into name
        if user_choice == "1":
            player = "rock"
        elif user_choice == "2":
            player = "paper"
        elif user_choice == "3":
            player = "scissors"
        else:
            print("Invalid choice! Please try again.")
            continue

        # Computer randomly selects a choice
        computer = random.choice(choices)

        print("\nYour choice     :", player)
        print("Computer choice :", computer)

        # Check the result
        if player == computer:
            print("Result: It's a Draw!")

        elif (
            (player == "rock" and computer == "scissors") or
            (player == "paper" and computer == "rock") or
            (player == "scissors" and computer == "paper")
        ):
            print("Result: You Win!")
            player_score += 1

        else:
            print("Result: Computer Wins!")
            computer_score += 1

        # Display score
        print("\nScore:")
        print("You      :", player_score)
        print("Computer :", computer_score)

    # Final result
    print("\n====================================")
    print("           FINAL RESULT")
    print("====================================")

    print("Your Score      :", player_score)
    print("Computer Score  :", computer_score)

    if player_score > computer_score:
        print("Congratulations! You are the Winner!")

    elif computer_score > player_score:
        print("Computer is the Winner!")

    else:
        print("The Game is Draw!")

    print("====================================")
    print("       Thank You for Playing!")
    print("====================================")
play_game()





# Ye Project Kaise Banaya? — Logic
# Is project ko banane ke liye maine 7 main steps follow kiye hain.


# Step 1: Random Module Import Karna
# Sabse pehle Python ka random module import kiya:

# import random


# Step 2: Score Variables Banana

# Game ke beginning mein:

# player_score = 0
# computer_score = 0

# Dono ka score initially 0 hai.

# Example:

# Player Score   = 0
# Computer Score = 0

# Agar player ek round jeetta hai:

# player_score += 1

# To:

# Player Score = 1

# Agar computer jeetta hai:

# computer_score += 1

# To:

# Computer Score = 1


# Step 3: Choices Ki List Banana

# Maine ek list banayi:

# choices = ["rock", "paper", "scissors"]

# Is list mein game ke teen possible choices hain:

# Rock
# Paper
# Scissors

# Computer isi list mein se randomly choice karega.



# Step 4: Multiple Rounds Ke Liye While Loop

# Game ko baar-baar chalane ke liye:

# while True:

# use kiya.

# Iska matlab hai game continuously chalega.

# Example:

# Round 1
#    ↓
# Round 2
#    ↓
# Round 3
#    ↓
# Round 4
# Game tab tak chalta rahega jab tak user Exit select nahi karta.



# Step 5: User Se Choice Lena

# User ko options diye:

# print("1. Rock")
# print("2. Paper")
# print("3. Scissors")
# print("4. Exit")

# Phir user ka input liya:

# user_choice = input("Enter your choice: ").lower()

# .lower() ka use isliye kiya hai taaki input lowercase mein aa jaye.

# Phir number ko actual choice mein convert kiya:

# if user_choice == "1":
#     player = "rock"

# elif user_choice == "2":
#     player = "paper"

# elif user_choice == "3":
#     player = "scissors"

# Example:

# User enters → 1

# Python converts:

# 1 → rock


# Step 7: Winner Decide Karna

# Ye project ka main logic hai.

# Rule 1: Same Choice

# Agar dono ki choice same hai:

# if player == computer:
#     print("Result: It's a Draw!")

# Example:

# Player    = Rock
# Computer  = Rock

# Result = Draw
# Rule 2: Player Wins

# Player tab jeetega jab:

# Rock beats Scissors
# Paper beats Rock
# Scissors beats Paper

# Code:

# elif (
#     (player == "rock" and computer == "scissors") or
#     (player == "paper" and computer == "rock") or
#     (player == "scissors" and computer == "paper")
# ):
#     print("Result: You Win!")
#     player_score += 1

# Example:

# Player    = Rock
# Computer  = Scissors

# Rock, Scissors ko beat karta hai.

# Therefore:

# You Win!

# Aur:

# player_score += 1

# se player ka score 1 increase ho jayega.

# Rule 3: Computer Wins

# Agar na draw hua aur na player jeeta, to computer winner hoga:

# else:
#     print("Result: Computer Wins!")
#     computer_score += 1

# Example:

# Player    = Rock
# Computer  = Paper

# Paper, Rock ko beat karta hai.

# Therefore:

# Computer Wins!

# Aur computer ka score:

# computer_score += 1

# se increase hoga.

# 3. Score Kaise Track Hota Hai?

# Har round ke baad score display hota hai:

# print("You      :", player_score)
# print("Computer :", computer_score)

# Example:

# Round 1
# You      : 1
# Computer : 0

# Round 2
# You      : 1
# Computer : 1

# Round 3
# You      : 2
# Computer : 1

# Is tarah variables continuously score ko store karte rehte hain.



# Final Winner Kaise Decide Hota Hai?

# Game exit hone ke baad final scores compare hote hain:

# if player_score > computer_score:
#     print("Congratulations! You are the Winner!")

# elif computer_score > player_score:
#     print("Computer is the Winner!")

# else:
#     print("The Game is Draw!")
# Example 1
# Player Score   = 3
# Computer Score = 1

# Player ka score zyada hai:

# Player Wins
# Example 2
# Player Score   = 1
# Computer Score = 3

# Computer ka score zyada hai:

# Computer Wins
# Example 3
# Player Score   = 2
# Computer Score = 2

# Dono ka score same hai:

# Game Draw