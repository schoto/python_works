#A simple game with some questions and answers
#User gets one point for every right answer
#User is allowed to answer 4 questions
print("Welcome to my computer quiz game! Have fun!")

playing = input("Do you want to play a game? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's then play!")
score = 0

#Question 1
answer = input("What is the capital of France? ")

if answer.lower() == "paris":
    print("Correct!")
    #add one point to score
    score += 1
else:
    print("Incorrect!")

#Question 2
answer = input("What does IBM stands for? ")

if answer.lower() == "international business machines corporation":
    print("Correct!")
    score += 1

else:
    print("Incorrect!")
    
#Question 3
answer = input("Who is the CEO of Apple? ")

if answer.lower() == "tim cook":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

#Question 4
answer = input("Who is the CEO of Twitter? ")

if answer.lower() == "elon musk":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " answers correct!")
print("Or " + str((score/4)*100) + " % of the questions right!")
print("Thanks for playing!")