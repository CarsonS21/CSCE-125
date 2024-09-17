# File name: Sessoms HW5
# Author: Carson Sessoms
# Email Address: sessomsc@usca.edu
# Homework #5
# calculates a baseball players batting average with a menu
# last changed 2/28/2023

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
pos_tuple = ("C", "1B", "2B", "3B", "SS", "LF", "CF", "RF", "P")
player_lineup = [["name": "Joe", "position": "P", "at_bats": 1, "num_hits"] 
def list(player_lineup):
    print("Player POS AB H AVG")
    print("----------------------------------------")
    for i, player in enumerate(player_lineup, start=1):
        print(f"{i}.{player['name'] }")
def add(player_lineup):
    player = input("Name: ")
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
def main():
    def decision():
        global choice
        choice = int(input("Menu option:"))
    menu()
    decision()
    while True:
        if choice == 1:
            print(player)
            decision()
        #elif choice == 2:
        elif choice == 7:
            print ("thank your for using this program!")
            break
        else:
            print("please enter a valid option")
            print()
            decision()
            
if __name__ == "__main__":
    main()
