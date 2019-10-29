# import the random package to geenrate a random choice
from random import randint

# choices is an array => an array is a container that can hold multiple values
choices = ["rock", "paper", "scissors"]

# set the computer variable to one of these choices 
computer = choices[randint(0, 2)]

# set up the game loop so we dont have to restart
player = False

while player is False:
	# set player to true
	print("******************************************\n\n")
	print("Choose your weapn!\n")

	player = input("rock, paper or scissors\n")


	print("computer chose ", computer, "\n")
	print("player chose ", player, "\n")

	if player.lower() == "quit":
		exit()
	elif computer == player:
		print("tie! no one wins, play again")

	elif player.lower() == "rock":
		if computer == "paper":
			print("You lose!", computer, "covers", player, "\n")
		else:
			print("You win!", player, "smashes", computer, "\n")

	elif player.lower() == "paper":
		if computer == "scissors":
			print("You lose!", computer, "cuts", player, "\n")
		else:
			print("You win!", player, "covers", computer, "\n")

	elif player.lower() == "scissors":
		if computer == "rock":
			print("You lose!", computer, "smashes", player, "\n")
		else:
			print("You win!", player, "cuts", computer, "\n")

	else:
		print("Thats not a valid option, try again")

	# need to check all conditions after checking for a tie
	player = False
	computer = choices[randint(0, 2)]

