# ==========================================
# QUIZ & EXAMINATION SYSTEM
# ==========================================

questions = [
    ("Which keyword is used to define a function in Python?",
     "A. function", "B. define", "C. def", "D. fun", "C"),

    ("Which data type is immutable?",
     "A. List", "B. Dictionary", "C. Tuple", "D. Set", "C"),

    ("Which symbol is used for comments?",
     "A. //", "B. #", "C. /*", "D. --", "B"),

    ("Which function takes user input?",
     "A. print()", "B. input()", "C. scan()", "D. read()", "B"),

    ("Which loop is used when the number of iterations is known?",
     "A. while", "B. do-while", "C. for", "D. repeat", "C"),

    ("Which operator is used for exponentiation?",
     "A. ^", "B. **", "C. //", "D. %", "B"),

    ("Which collection stores unique values?",
     "A. List", "B. Dictionary", "C. Set", "D. Tuple", "C"),

    ("Which keyword exits a loop?",
     "A. continue", "B. pass", "C. stop", "D. break", "D"),

    ("Which data type stores key-value pairs?",
     "A. List", "B. Dictionary", "C. Tuple", "D. Set", "B"),

    ("Which function displays output?",
     "A. print()", "B. input()", "C. display()", "D. show()", "A")
]


# Grade Function
def calculate_grade(percent):

    if percent >= 90:
        return "O"
    elif percent >= 80:
        return "A+"
    elif percent >= 70:
        return "A"
    elif percent >= 60:
        return "B+"
    elif percent >= 50:
        return "B"
    else:
        return "F"


# Display Question
def display_question(question):

    print("\n" + question[0])
    print(question[1])
    print(question[2])
    print(question[3])
    print(question[4])


# Get Valid Answer
def get_answer():

    while True:

        answer = input("Enter Your Answer (A/B/C/D): ").upper()

        if answer == "A" or answer == "B" or answer == "C" or answer == "D":
            return answer

        else:
            print("Invalid Choice.")
            # Evaluate Quiz
def evaluate_quiz():

    score = 0
    wrong_answers = []

    for i in range(len(questions)):

        question = questions[i]

        display_question(question)

        answer = get_answer()

        if answer == question[5]:
            print("Correct!")
            score += 1
        else:
            print("Wrong!")
            wrong_answers.append((question[0], question[5], answer))

    return score, wrong_answers


# Show Wrong Answers
def show_wrong_answers(wrong_answers):

    if len(wrong_answers) == 0:
        print("\nExcellent! No Wrong Answers.")
        return

    print("\n========== WRONG ANSWERS ==========")

    for question, correct, entered in wrong_answers:

        print("Question :", question)
        print("Your Answer :", entered)
        print("Correct Answer :", correct)
        print("-----------------------------------")


# Show Final Report
def show_report(name, roll, score, wrong_answers):

    total_questions = len(questions)

    percentage = (score / total_questions) * 100

    grade = calculate_grade(percentage)

    print("\n========== RESULT REPORT ==========")
    print("Student Name :", name)
    print("Roll Number  :", roll)
    print("Score        :", score, "/", total_questions)
    print("Percentage   : {:.2f}%".format(percentage))
    print("Grade        :", grade)

    if percentage >= 50:
        print("Result       : PASS")
    else:
        print("Result       : FAIL")

    show_wrong_answers(wrong_answers)
    # Main Function
def main():

    print("===================================")
    print("      PYTHON QUIZ SYSTEM")
    print("===================================")

    name = input("Enter Student Name: ")

    while True:
        try:
            roll = int(input("Enter Roll Number: "))
            break
        except ValueError:
            print("Invalid Roll Number.")

    score, wrong_answers = evaluate_quiz()

    show_report(name, roll, score, wrong_answers)


# Program Starts Here
if __name__ == "__main__":
    main()