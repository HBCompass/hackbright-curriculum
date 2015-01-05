import random

#greet user
print "Hello, what's your name?"

#get player name
name = raw_input("> ")

highscore = 100

def guess():
	print ("%s , I'm thinking of a number between 1 and 100. Try to guess my number." % name)

#Create variable for random number within the range and defines score variable
	num = random.randint(0, 100)
	score = 0

#declare global variable highscore
	global highscore

#Get number from player and test if it's a valid entry
	while True: 
		guess = raw_input("> ")
		try:
			guess = int(guess)
		except ValueError:
			print ("That is not a number! Don't you know what a number is?")
			continue

		if guess < 1 or guess > 100:
			print ("Enter a number between 1 and 100")
			continue

		score += 1
		if guess < num:
			print "Your guess is too low. Try again."
		elif guess > num:
			print "Your guess is too high. Try again."
		else:
			print "You got it! You tried %d times." % score
			if score < highscore:
				highscore = score
				print "You beat the high score! The new high score is %d" % highscore
			break

#Function to repeat gameplay
def gameplay():
	playagain = "yes"

	while playagain == "yes":
		guess()

		print "Would you like to play again? Type yes or no."

		playagain = raw_input("> ").lower()

	print "Thanks for playing!"

#Initial call to start the game
gameplay()