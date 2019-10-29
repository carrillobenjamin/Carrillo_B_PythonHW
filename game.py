# import the random package to geenrate a random choice
from random import randint

# set up variables for player and ai lives
player_lives = 5
computer_lives = 5

# choices is an array => an array is a container that can hold multiple values
choices = ["rock", "paper", "scissors"]

# set the computer variable to one of these choices 
computer = choices[randint(0, 2)]

# set up the game loop so we dont have to restart
player = False

while player is False:
	# set player to true
	print("******************************************\n\n")
	print("computer lives: ", computer_lives, "/5\n")
	print("player lives: ", player_lives, "/5\n")
	print("Choose your weapn!\n")

	player = input("rock, paper or scissors\n")
	player = player.lower()


	print("computer chose ", computer, "\n")
	print("player chose ", player, "\n")

	if player.lower() == "quit":
		exit()
	elif computer == player:
		print("tie! no one wins, play again")

	elif player.lower() == "rock":
		if computer == "paper":
			print("You lose!", computer, "covers", player, "\n")
			player_lives = player_lives - 1
		else:
			print("You win!", player, "smashes", computer, "\n")
			computer_lives = computer_lives - 1

	elif player.lower() == "paper":
		if computer == "scissors":
			print("You lose!", computer, "cuts", player, "\n")
			player_lives = player_lives - 1
		else:
			print("You win!", player, "covers", computer, "\n")
			computer_lives = computer_lives - 1

	elif player.lower() == "scissors":
		if computer == "rock":
			print("You lose!", computer, "smashes", player, "\n")
			player_lives = player_lives - 1
		else:
			print("You win!", player, "cuts", computer, "\n")
			computer_lives = computer_lives - 1

	else:
		print("Thats not a valid option, try again")


	# handle all loves lost for player and ai
	if player_lives is 0:
		print("GAME OVER! play again?")
		choice = input("Y / N")
		print(choice)

		if (choice is "N") or (choice is "n"):
			print("you chose to quit")
			exit()

		elif (choice is "Y") or (choice is "y"):
			# rest game so we can start over
			player_lives = 5
			computer_lives = 5
			player = False
			computer = choices[randint(0,2)]

	elif computer_lives is 0:
		print("WINNER WINNER CHICKEN DINNER! play again?")
		choice = input("Y / N")
		print(choice)

		if (choice is "N") or (choice is "n"):
			print("you chose to quit")
			exit()

		elif (choice is "Y") or (choice is "y"):
			# rest game so we can start over
			player_lives = 5
			computer_lives = 5
			player = False
			computer = choices[randint(0,2)]

	else:
		# need to check all conditions after checking for a tie
		player = False
		computer = choices[randint(0, 2)]

