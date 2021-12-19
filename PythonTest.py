print("Lets work on python retention skills")

playing = input("Ready to show off your big brain? \n")
if playing.lower() != "yes":
  quit()
print("Okay, Let's play :) ")

score = 0

#Question 1
answer = input("Does python follow the standard order of operations? \n")
if answer.lower() == "yes":
  print("Correct!")
  score += 1
else:
  print("Incorrect :( ")

#Question 2
answer = input("What symbol means 'equal to'? \n")
if answer.lower() == "==":
  print("Correct!")
  score += 1
else:
  print("Incorrect :( ")

#Question 3
answer = input("List the key word for a whole number? \n")
if answer.lower() == "int":
  print("Correct!")
  score += 1
else:
  print("Incorrect :( ")

#Question 4
answer = input("What key word allows you to create a function? \n")
if answer.lower() == "def":
  print("Correct!")
  score += 1
else:
  print("Incorrect :( ")

print("You got " + str(score) + " out of 4 questions correct")
print("You got " + str((score/4) * 100) + "% of the questions correct")
