print("Welocme to Quiz!")
playing = input("Do you want to play? (yes/no)")
if playing.lower()!="yes":
    quit()
print("Ok lets Play!")
score = 0
question = input("Is Single and Double Quotes equal in python? ")
if question.lower() == "yes":
    print("Wow Correct Answer!")
    score+=1
else:
    print("Incorrect")
question = input("Is python tuples are ordered? ")
if question.lower() == "yes":
    print("Wow Correct Answer!")
    score += 1
else:
    print("Incorrect")
question = input("Will List allow to store multiple data type values in python ? ")
if question.lower() == "yes":
    print("Wow Correct Answer!")
    score += 1
else:
    print("Incorrect")
question = input("Is List and Tuple same in python? ")
if question.lower() == "no":
    print("Wow Correct Answer!")
    score += 1
else:
    print("Incorrect")
question = input("To Compare two values have to be used = in python? ")
if question.lower() == "no":
    print("Wow Correct Answer!")
    score += 1
else:
    print("Incorrect")
print ("*****************************************")
print("You got: " + str(score)+" Scores Out of 5")
print("You got: "+ str(score/5*100)+"%")
print ("*****************************************")

