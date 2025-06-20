# Python Quiz Game

questions = ("How many elements are in the periodic table?: ",
             "Which animal lays the largest eggs?: ",
             "What is the most abundant gas in the Earth's Atmosohere?: ",
             "How many bones are there in the Human Body?: ",
             "Which planet in the solar syatem is the hottest?: ")

options = (("A. 116", "B. 117", "C. 118", "D. 119"),
           ("A. Whale", "B. Ostrich", "C. Crocodile", "D. The Shark"),
           ("A. Nitrogen", "B. Carbon-Dioxide", "C. Oxygen", "D. Hydrogen"),
           ("A. 206", "B. 207", "C. 208", "D. 209"),
           ("A. Mercury", "B. Venus", "C. Mars", "D. Jupiter"))

answers = ("C", "B", "A", "A", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("--------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
        
    guess = input("Enter Your Answer (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score+=1
        print("CORRECT !!!")
    
    else:
        print("INCORRECT !!!")
        print(f"{answers[question_num]} is the Correct Answer.")
        print()
    
    print()
    question_num +=1
    
    
print("----------------------")  
print("         RESULTS      ") 
print("----------------------")

print()
print("Answers: ", end=" ")
for answer in answers:
    print(answer, end=", ")
print()

print("Guesses: ", end=" ")
for guess in guesses:
    print(guess, end=", ")
print()

score = int((score / len(questions) * 100))
print()
print(f"Your Final Score is : {score}%")