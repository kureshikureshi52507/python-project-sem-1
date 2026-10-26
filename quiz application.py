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