import random
options = ["rock", "paper", "scissors"]
def playRPS():
    player_choice = input("Would you like to play rock, paper, or scissors? ")
    computer_choice = random.choice(options)
    if player_choice.lower() not in options:
        print("Please enter a valid option of either rock, paper, or scissors.")
    elif player_choice.lower() == computer_choice:
        print("Computer choice:", computer_choice)
        print("You tied with the computer.")
    elif (player_choice.lower() == "scissors" and computer_choice == options[0]) or \
         (player_choice.lower() == "rock" and computer_choice == options[1]) or \
         (player_choice.lower() == "paper" and computer_choice == options[2]):
        print("Computer choice: ", computer_choice)
        print("You lost, better luck next time!")
        #if we are counting losses, the list containing the info on wins and losses needs to have the loss area added here
    else:
        print("Computer choice: ", computer_choice)
        print("You won! good job.")
        #this is where the win is added to the number depending on where the wins for rps is saved

# i dont think we need this part for the main code but you could copy and paste it for playing it and just change the function name
def main():
    RPS_choice = True 
    while RPS_choice == True:
        playRPS()
        print()
        user_choice = input("Would you like to play again? please type y/n: ")
        print()
        if user_choice.lower() == "y":
            RPS_choice = True
        elif user_choice.lower() == "n":
            RPS_choice = False
        else:
            print("Please play again and enter a valid input of y or n next time.")

if __name__ == "__main__":
    main()

            
        

              

        
