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
----------------------------------------------------------------------------------------------------------------------------
# ==========================================
#       QUIZ APPLICATION - CORE PYTHON
# ==========================================

# Quiz questions stored in a list of dictionaries
questions = [
    {
        "question": "What is the full form of CPU?",
        "options": ["A. Central Processing Unit",
                    "B. Computer Processing Unit",
                    "C. Central Program Unit",
                    "D. Control Processing Unit"],
        "answer": "A"
    },
    {
        "question": "Which language is used for Python programming?",
        "options": ["A. HTML",
                    "B. Python",
                    "C. CSS",
                    "D. SQL"],
        "answer": "B"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["A. //",
                    "B. /* */",
                    "C. #",
                    "D. --"],
        "answer": "C"
    },
    {
        "question": "Which function is used to take input from the user?",
        "options": ["A. print()",
                    "B. input()",
                    "C. scan()",
                    "D. get()"],
        "answer": "B"
    },
    {
        "question": "Which data type is used to store multiple values in Python?",
        "options": ["A. int",
                    "B. float",
                    "C. list",
                    "D. bool"],
        "answer": "C"
    }
]


# Function to display quiz
def start_quiz():

    score = 0

    print("\n====================================")
    print("        WELCOME TO QUIZ APP")
    print("====================================")

    print("Total Questions:", len(questions))
    print("Each correct answer = 1 mark")
    print("------------------------------------")

    # Loop through all questions
    for i, q in enumerate(questions, start=1):

        print("\nQuestion", i, ":", q["question"])

        # Display options
        for option in q["options"]:
            print(option)

        # Take answer from user
        user_answer = input("Enter your answer (A/B/C/D): ").upper()

        # Validate input
        while user_answer not in ["A", "B", "C", "D"]:
            print("Invalid answer! Please enter A, B, C or D.")
            user_answer = input("Enter your answer: ").upper()

        # Check answer
        if user_answer == q["answer"]:
            print("Correct Answer!")
            score += 1
        else:
            print("Wrong Answer!")
            print("Correct Answer is:", q["answer"])


    # Calculate percentage
    percentage = (score / len(questions)) * 100

    # Display result
    print("\n====================================")
    print("             QUIZ RESULT")
    print("====================================")

    print("Total Questions :", len(questions))
    print("Correct Answers :", score)
    print("Wrong Answers   :", len(questions) - score)
    print("Score           :", score, "/", len(questions))
    print("Percentage      :", percentage, "%")

    # Performance feedback
    if percentage >= 80:
        print("Performance     : Excellent!")
    elif percentage >= 60:
        print("Performance     : Very Good!")
    elif percentage >= 40:
        print("Performance     : Good, Keep Practicing!")
    else:
        print("Performance     : Need More Practice!")

    print("====================================")
    print("       Thank You for Playing!")
    print("====================================")


# Start the quiz
start_quiz()



# Step 1: Questions ko Store Karna

# questions = [
#     {
#         "question": "What is the full form of CPU?",
#         "options": ["A. Central Processing Unit",
#                     "B. Computer Processing Unit",
#                     "C. Central Program Unit",
#                     "D. Control Processing Unit"],
#         "answer": "A"
#     }
# ]


# Step 2: Quiz Start Karne Ke Liye Function

# Maine quiz ke main logic ko ek function ke andar rakha
# def start_quiz():


# Step 3: Questions Ko Ek-Ek Karke Display Karna

# Questions ko one-by-one display karne ke liye for loop use kiya:

# for i, q in enumerate(questions, start=1):



# Step 4: User Ka Answer Lena Aur Check Karna

# # User se answer lene ke liye:
# user_answer = input("Enter your answer (A/B/C/D): ").upper()


# Step 5: Final Percentage Calculate Karna

# Quiz complete hone ke baad:
# percentage = (score / len(questions)) * 100
------------------------------------------------------------------------------------------------------------------------------
NAME: MOHIN KURESHI
ENROLMENT NUM: T2611430300021
