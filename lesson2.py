#guessing game 
import random 

guessesTaken = 0

print "What's your name?"
myName = raw_input()

number = random.randint(1, 10)
print "I am thinking of a number between 1 and 10. What is it?"

while guessesTaken < 3:
	print "Guess what number?"
	guess = raw_input()
	guess = int(guess)

	guessesTaken = guessesTaken + 1

	if guess < number:
		print "Your guess is too low."

	if guess > number:
	    print "Your guess is too high."	

    if guess == number:
    	break

if guess == number:
	guessesTaken = str(guessesTaken)
	print "Good job, " + myName + "! You guessed my number in " + guessesTaken + " guesses!"u

if guess != number:
	number = str(number)
	print "Try again. I am not thinking the number " + number