# File name: Sessoms HW3
# Author: Carson Sessoms
# Email Address: sessomsc@usca.edu
# Homework #3
# calculates a baseball players batting average with a menu
# last changed 2/12/2023

#introduction

def menu():
    print("MENU OPTIONS")
    print("1 - Calculate batting average")
    print("2 - Exit program")
    print()
    global choice
    choice = int(input("Menu option:"))
    print()
def batting_avg():
    name = input("Please enter the players name: ")
    ab = float(input("Please enter the players number of at bats: "))
    hits = float(input("Please enter the players number of hits: "))
    batav = round(hits / ab, 3)
    print()
    print(name + "'s batting average is " + str(batav))
    print()
def main():
    print("==================================================================================")
    print("                         Baseball Team Manager")
    menu()
    print("==================================================================================")
    print()
    while True:
        if choice == 1:
            batting_avg()
            menu()
        elif choice == 2:
            print ("thank your for using this program!")
            break
        else:
            print("please enter a valid option")
            print()
            menu()
if __name__ == "__main__":
    main()
