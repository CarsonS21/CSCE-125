#import csv file
import csv
import random
import sys
FILENAME = "leaderboard.csv"

'''
in the comments above the functions are the main contributors,
however we all worked together in the library one day and helped
to fix all the issues throughout all the codes that we did separately
'''
#create writing leaderboard function
#kaeden
def write_leaderboard(leaderboard):
    try:
        with open(FILENAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(leaderboard)
    except Exception as e:
        print(type(e),e)
        exitProgram()

#create reading leaderboard function
#kaeden
def read_leaderboard():
    try:
        leaderboard = []
        with open(FILENAME, newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                leaderboard.append(row)
        return leaderboard
    except FileNotFoundError:
        print(f"Could not find {FILENAME} file.")
        exitProgram()
    except Exception as e:
        print(type(e), e)
        exitProgram()

#exit program function
#kaeden
def exitProgram():
    print("Terminating the program")
    sys.exit()

#display menu function
#kaeden
def menu():
    print("-" * 64)
    print("Welcome to the game program! Let's play!")
    print()
    print("Game Menu:")
    print("1 -  Rock-Paper-Scissors")
    print("2 -  Hangman")
    print("3 -  Number Guessing Game")
    print("4 -  Display Past Results")
    print("5 -  Exit Program")
    print()
    print("-" * 64)
    
#carson
def find_name(leaderboard, playerName):
    j = 0
    newlist = []
    for i in leaderboard:
        if playerName in i:
            newlist = leaderboard.pop(j)
            return newlist
        elif playerName not in i:
            j+= 1
            continue
    if playerName in newlist:
        return newlist
    else:
        newlist = [playerName, 0, 0, 0, 0]
        return newlist

#carson
def playRPS(player):
    options = ["rock", "paper", "scissors"]
    player_choice = input("Would you like to play rock, paper, or scissors? ")
    computer_choice = random.choice(options)
    if player_choice.lower() not in options:
        print("Please enter a valid option of either rock, paper, or scissors.")
        print()
    elif player_choice.lower() == computer_choice:
        print("Computer choice:", computer_choice)
        print("You tied with the computer.")
        print()
    elif (player_choice.lower() == "scissors" and computer_choice == options[0]) or \
         (player_choice.lower() == "rock" and computer_choice == options[1]) or \
         (player_choice.lower() == "paper" and computer_choice == options[2]):
        print("Computer choice: ", computer_choice)
        print("You lost, better luck next time!")
        print()
    else:
        print("Computer choice: ", computer_choice)
        print("You won! good job.")
        print()
        player[2] += 1

#fernando
def hangman(player):
    # Load words from file
    with open('words.txt', 'r') as file:
        words = file.read().splitlines()

    # Pick a random word from the list
    word = random.choice(words).upper()

    # Set up the game
    guesses = []
    turns = 7

    # Loop until the player wins or runs out of turns
    while turns > 0:
        # Print current progress
        progress = ''
        for letter in word:
            if letter in guesses:
                progress += letter
            else:
                progress += '_'
        print('Progress: ' + progress)

        # Ask for a guess
        guess = input('Guess a letter: ').upper()

        # Check if the guess is correct
        if guess in word:
            print('Correct!')
            guesses.append(guess)
        else:
            print('Wrong!')
            turns -= 1

        # Check if the player has won
        if '_' not in progress:
            print('Congratulations, you won!')
            player[1] += 1
            return

    # If the player has run out of turns, they lose
    print('Sorry, you lost. The word was ' + word)
    
#siddh
def numberGuessing(player):
    # Generate a random number between 1 and 6
    secret_number = random.randint(1, 6)
   
    # Initialize the number of tries and the user's guess
    num_guesses = 0
    guess = None
   
    # Loop until the user guesses the correct number
    while guess != secret_number:
        # Get the user's guess as an integer
        while True:
            try:
                guess = int(input("Guess the secret number (between 1 and 6): "))
                break
            except ValueError:
                print("Please enter a valid integer between 1 and 6.")

        # Check if the guess is higher or lower than the secret number
        if guess < secret_number:
            print("The secret number is higher.")
        elif guess > secret_number:
            print("The secret number is lower.")
       
        # Increment the number of tries
        num_guesses += 1
   
    # Print the number of tries and store the result in the CSV file
    print(f"Congratulations! You guessed the secret number in {num_guesses} tries.")
   
    # Append the number of tries to the CSV file
    player[3] += num_guesses
    player[4] += 1

#kaeden and carson      
def results(leaderboard, player):
    if len(leaderboard) == 0:
        print("There are no past results for the games.")
    else:
        #print("f{'Players Name': 16 {'Hangman Wins':>14 {'RPS Record':>12} {'Average # Guesses':>18}")
        print("{:>16} {:>16} {:>12} {:>22}".format('Players Name', 'Hangman Wins', 'RPS wins', 'Average # Guesses'))
        print("-" * 80)
        for i, playerA in enumerate(leaderboard, start=1):
            playerGuesses = float(player[3])
            playerTotal = float(player[4])
            try:
                numPlayerPercent = round(playerGuesses / playerTotal, 3)
            except:
                numPlayerPercent = 0
            print("{:>10} {:>16} {:>14} {:>18}".format(playerA[0], playerA[1], playerA[2], numPlayerPercent))
        try:
            numMainPercent = round(float(player[3]) / float(player[4]), 3)
        except:
            numMainPercent = 0
        print("{:>10} {:>16} {:>14} {:>18}".format(player[0], player[1], player[2], numMainPercent))
        print("-" * 80)
#kaeden
def main():
    playerName = input("Enter your name: ")
    playerName = playerName.lower()
    menu()
    leaderboard = read_leaderboard()
    player = find_name(leaderboard, playerName)
    while True:
        try:
            menuOption = int(input("Select game to play: "))
            print()
        except ValueError:
            print("Invalid integer. please try again.")
            continue
        if menuOption == 1:
            playRPS(player)
        elif menuOption == 2:
            hangman(player)
        elif menuOption == 3:
            numberGuessing(player)
        elif menuOption == 4:
            results(leaderboard, player)
        elif menuOption == 5:        
            break
        else:
            print("Invalid integer. Please try again.")
            print()
    leaderboard.append(player)
    write_leaderboard(leaderboard)
    print("Bye!")
    print("Thanks for playing!")

if __name__ == "__main__":
    main()
