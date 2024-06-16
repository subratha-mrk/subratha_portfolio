from quiz_app_module import *
import time

print("***********************************")
print("   Welcome to the Quiz game!!!")

def check_ans(user_guess,correct_ans):
    if user_guess == correct_ans:
        return True
    else:
        return False
for question_num in range(len(question_bank)):
    print("***********************************")
    print(question_bank[question_num]["text"])
    for i in options[question_num]:
        print(i)

    guess_opt = input("Enter any one of the options given (A/B/C/D): ").upper()
    correct = check_ans(guess_opt,question_bank[question_num]["answer"])
    if correct:
        print("You're RIGHT!!")
        score += 1
    else:
        print("Incorrect Answer :(")
        print(f"The correct answer is {question_bank[question_num]['answer']}")
    print(f"Your current score is {score}/{question_num+1}")
    print()
print(f"You have given {score} correct answers.")
print(f"Your final score is {(score/len(question_bank))*100}%")
time.sleep(6)

