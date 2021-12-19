# If you guess the right number, you win.  If not, try again.
import random

top_of_range = input("Choose a number between 1 and 10: \n")
if top_of_range.isdigit():
  top_of_range = int(top_of_range)
  
  if top_of_range <= 0:
    print("Please type a number between 0 and 10 next time.")
    quit()
else:
  print("Please type a number next time.")
  quit()

random_number = random.randint(0,top_of_range)
guesses = 0

while True: 
  guesses += 1
  user_guess = input("Try again: \n")
  if user_guess.isdigit():
    user_guess = int(user_guess)
  else:
    print("Please type a number next time.")
    continue

  if user_guess == random_number:
    print("Your got it!")
    break
  else:
    if user_guess > random_number:
      print("You were above the number:")
    else:
      print("You were below the number:")

print("you got it in", guesses, "guessses")
