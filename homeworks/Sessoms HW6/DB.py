'''
File Name:DB
Author: Carson Sessoms
Email: sessomsc@usca.edu
Homework #6
Acts as the reader and writer for the csv file in HW 6
Last changed: 3/19/2023
'''
import csv
FILENAME = "Baseball Lineups.csv"

def write_lineup(players):
    with open(FILENAME, "w", newline = "") as file:
        writer = csv.writer(file)
        writer.writerows(players)
def read_lineup():
    with open(FILENAME, newline = "") as file:
        reader = list(csv.reader(file))
        #for row in reader:
            #print(row[0:])
        return reader
