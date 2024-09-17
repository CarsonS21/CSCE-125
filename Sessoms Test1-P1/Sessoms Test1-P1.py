# File name: Sessoms Test1-P1
# Author: Carson Sessoms
# Email Address: sessomsc@usca.edu
# Test1-P1
# Determine if an inputed number between 1 and 50 is odd or even
# last changed 2/13/2023

#the code for the menu and to input what the user wants to do.
def menu():
    print()
    print("MENU OPTIONS")
    print("1 - Enter a number(between 1 .. 50) to check")
    print("2 - Exit Program")
    global choice
    choice = int(input("Menu option: "))

#the code to recieve a number and check if it is even or odd.
def check_number():
    print()
    print("Check Odd or Even...")
    chosen_number = int(input("Please enter a number: "))
    if 0 < chosen_number < 51:
        if (chosen_number % 2) == 0:
            print("Your number is: Even")
        else:
            print("Your number is: Odd")
    else:
        print("Not a valid Data option. Please try again.")

#the main function that determines when to end the loop
#and adds visual effects to the opening
def main():
    print("==================================================================================")
    print("                         Odd or Even Game")
    menu()
    print("==================================================================================")
    print()
    while True:
        if choice == 1:
            check_number()
            menu()
        elif choice == 2:
            print("Bye!")
            break
        else:
            print("Not a valid Menu option. Please try again.")
            menu()
if __name__ == "__main__":
    main()
    
                        
                        
