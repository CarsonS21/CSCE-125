'''
File Name:DB
Author: Carson Sessoms
Email: sessomsc@usca.edu
Homework #7
Acts as the reader and writer for the csv file in HW 7
Last changed: 3/26/2023
'''
import csv
import sys
FILENAME = input("Please enter the name of your csv file with your lineup: ")
def write_lineup(players):
    try:
        with open(FILENAME, "w", newline = "") as file:
            writer = csv.writer(file)
            writer.writerows(players)
    except Exception as e:
        print(type(e), e)
        sys.exit()
def read_lineup():
    try:
        with open(FILENAME, newline = "") as file:
            reader = list(csv.reader(file))
        return reader
    except FileNotFoundError:
        print("Could not find " + FILENAME + " file.")
        sys.exit()
    except Exception as e:
        print(type(e), e)
        sys.exit()
