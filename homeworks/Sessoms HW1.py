# File name: Sessoms HW1
# Author: Carson Sessoms
# Email Address: sessomsc@usca.edu
# Homework #1
# calculates a baseball players batting average
# last changed 1/29/2023

#introduction
print("Welcome, this program will help you calculate"
      "\nyour players batting averages")
print()

# getting the info for the calculations and printing the batting average
name = input("Please enter the players name: ")
ab = float(input("Please enter the players number of at bats: "))
hits = float(input("Please enter the players number of hits: "))
batav = round(hits / ab, 3)
print()
print(name + "'s batting average is " + str(batav))
print()
print("Thank you for using this program!")

