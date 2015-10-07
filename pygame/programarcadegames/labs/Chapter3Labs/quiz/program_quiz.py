"""This program is a 5 question quiz"""

#This program will ask 5 questions
#These questions should vary in type - multiple choice, number, and text
#The program should let the user know which questions they got correct
#At the end, the program should let the user know their percentage of correct questions

#These functions determine whether the answers to the questions are correct - the questions come later!

def question_one(answer):
    if answer == 151:
        return True
    else:
        return False

def question_two(answer):
    if answer == "paul":
        return True
    else:
        return False

def question_three(answer):
    if answer == "a":
        return True
    else:
        return False

def question_four(answer):
    if answer == "infinity":
        return True
    else:
        return False

def question_five(answer):
    if answer == 3:
        return True
    else:
        return False

score = 0 #This variable will be used later to total up scores
answers = [] #This list will keep track of correct answers

#This part will use input to ask the questions, then call the appropriate function to check whether the answer
#given is correct, then append the result to the answers list
answers.append(question_one(int(input("Question 1: How many pokemon were present in pokemon red?\n"))))
answers.append(question_two(str.lower(input("Question 2: What is the name of the monster that lives in Phil's living room?\n"))))
answers.append(question_three(str.lower(input("Question 3: Which of these codes is not actually a code\n\
A: Lodge, a code that uses place names for functions, and requires you to plan your travels between them\n\
B: Piet, a code which uses bitmap pictures which resemble modern art\n\
C: SPL, a code which requires users to write in the form of a shakespeare play\n"))))
answers.append(question_four(str.lower(input("Question 4: A good program contains three numbers: 0, 1 and ___?\n"))))
answers.append(question_five(int(input("Question 5: What is the biblical value of pi?"))))

#This loop will check each answer, print out whether the question was answered correctly or not,
#and update the score if answered correctly
for i in range(len(answers)):
    if answers[i] == True:
        print("You got question %s correct!" % (i + 1))
        score = score + 1
    else:
        print("You got question %s wrong, you suck!" % (i + 1))

#This print statement just states how many questions were answered correctly
print("You answered %s out of %s question correctly" % (score, len(answers)))

#This print statement will display percentage score. It uses a magic number to calculate the percentage
print("Your score is %d%%" % ((score / (len(answers)) * 100)))

#This function will check if all the answers were correct, and print an ppropriate statement
if score == len(answers):
    print("You got all the questions correct! Hooray!")
elif score == 0:
    print("You didn't get any of the answers correct, are you even trying?!")
else:
    print("You didn't get all the questions correct - try again!")
