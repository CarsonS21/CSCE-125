# File name: Sessoms HW3
# Author: Carson Sessoms
# Email Address: sessomsc@usca.edu
# Homework #3
# calculates a baseball players batting average with a menu
# last changed 2/12/2023

#introduction
def menu():
    print("==================================================================================")
    print("                         Baseball Team Manager")
    print("MENU OPTIONS")
    print("1 - Display lineup")
    print("2 - Add player")
    print("3 - remove player")
    print("4 - move player")
    print("5 - edit player position")
    print("6 - edit player statistics")
    print("7 - exit program")
    print("Positons")
    print("C, 1B, 2B, 3B, SS, LF, CF, RF, P")
    print("==================================================================================")
    print()
    global choice
    choice = int(input("Menu option:"))
    print()
pos_tuple = ("C", "1B", "2B", "3B", "SS", "LF", "CF", "RF", "P")
lineup_list = []
def option1():
    print(lineup_list)
    menu()
def option2():
    name = input("Please enter the players name: ")
    ab = float(input("Please enter the players number of at bats: "))
    hits = float(input("Please enter the players number of hits: "))
    batav = round(hits / ab, 3)
    if batav < 0 or batav > 1:
        print("please enter valid numbers of at bats and hits and try again")
        print()
        return
    else:
        print()
        print(name + "'s batting average is " + str(batav))
        print()
"""
def batting_avg():
    name = input("Please enter the players name: ")
    ab = float(input("Please enter the players number of at bats: "))
    hits = float(input("Please enter the players number of hits: "))
    batav = round(hits / ab, 3)
    if batav < 0 or batav > 1:
        print("please enter valid numbers of at bats and hits and try again")
        print()
        return
    else:
        print()
        print(name + "'s batting average is " + str(batav))
        print()
"""
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
