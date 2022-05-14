#A simple game with some questions and answers
#User gets one point for every right answer
print("Welcome to my computer quiz game! Have fun!")

playing = input("Do you want to play a game? ")

if playing != "yes":
    quit()

print("Okay! Let's then play!")

#Question 1
answer = input("What is the capital of France? ")

if answer == "paris":
    print("Correct!")
else:
    print("Incorrect!")

#Question 2
answer = input("What does IBM stands for? ")

if answer == "international business machines corporation":
    print("Correct!")
else:
    print("Incorrect!")
    
#Question 3
answer = input("Who is the CEO of Apple? ")

if answer == "tim cook":
    print("Correct!")
else:
    print("Incorrect!")

#Question 4
answer = input("Who is the CEO of Twitter? ")

if answer == "elon musk":
    print("Correct!")
else:
    print("Incorrect!")

