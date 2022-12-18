print("This is my Math Quiz Game.")
score = 0
while True:
    playing = input("Do you want to play? Y/N: ")
    if playing.lower() == "n":
        quit()
    if playing.lower() == "y":
        print("Let's Play")
        break
    else:
        print("Please enter the valid answer: ")
print("Question 1 out of 5...\n")
answer = input("What is 6 + 7 = ")
if answer == '13':
    print("Answer is correct\n")
    score += 1
else:
    print('Answer is incorrect\n')
print("Question 2 out of 5...\n")
answer = input("What is 19 - 8 - 3 = ")
if answer == '8':
    print("Answer is correct\n")
    score += 1
else:
    print('Answer is incorrect\n')
print("Question 3 out of 5...\n")
answer = input("What is 5*5 = ")
if answer == "25":
    print("Answer is correct\n")
    score += 1
else:
    print('Answer is incorrect\n')
print("Question 4 out of 5...\n")
answer = input("What is 3/3 = ")
if answer == '1':
    print("Answer is correct\n")
    score += 1
else:
    print('Answer is incorrect\n')
print("Question 5 out of 5...\n")
answer = input("What is 6*4 = ")
if answer == '24':
    print("Answer is correct\n")
    score += 1
else:
    print('Answer is incorrect\n')
print("Quiz finished.\n The number of right answers is " + str(score))
