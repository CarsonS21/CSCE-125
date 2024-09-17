# File name: Sessoms HW2
# Author: Carson Sessoms
# Email Address: sessomsc@usca.edu
# Homework #2
# calculates a baseball players batting average with a menu
# last changed 2/5/2023

#introduction
print()
print("==================================================================================")
print("                         Baseball Team Manager")
print("MENU OPTIONS")
print("1 - Calculate batting average")
print("2 - Exit program")
print("==================================================================================")
print()
#choosing which action to take
choice = int(input("Menu option:"))
#this choice runs the program
while True:
    if choice == 1:
        name = input("Please enter the players name: ")
        ab = float(input("Please enter the players number of at bats: "))
        hits = float(input("Please enter the players number of hits: "))
        batav = round(hits / ab, 3)
        print()
        print(name + "'s batting average is " + str(batav))
        print()
        choice = int(input("Menu option:"))
        print()
    elif choice == 2:
        print ("thank your for using this program!")
        break
    else:
        print("please enter a valid option")
        print()
        choice = int(input("Menu option:"))
        print()
