'''
File Name:Sessoms HW9
Author: Carson Sessoms
Email: sessomsc@usca.edu
Homework #9
allows someone to view and edit a baseball lineup with batting averages and stores
it in a txt file
Last changed: 4/11/2023
'''
import sys
FILENAME = input("Please enter the name of your lineup file: ")
POSITIONS = ("C", "1B", "2B", "3B", "SS", "LF", "CF", "RF", "P")

def read_file():
    dataList = []
    try:
        with open(FILENAME) as file:
            for line in file:
                name, position, at_bats, hits = line.strip().split(",")
                at_bats = int(at_bats)
                hits = int(hits)
                average = round(hits / at_bats, 3)
                player = [name, position, at_bats, hits, average]
                dataList.append(player)
    except OSError:
        print("No file called " + FILENAME)
        sys.exit()
    return dataList
def write_lineup(players):
    with open(FILENAME, "w") as file:
        for player in players:
            file.write("{},{},{},{}\n".format(player[0], player[1], player[2], player[3]))
def add_player(players):
    name = input("Name: ")
    position = get_player_position()
    at_bats = get_at_bats()
    hits = get_hits()
    
    player = []
    player.append(name)
    player.append(position)
    player.append(at_bats)
    player.append(hits)
    players.append(player)
    write_lineup(players)
    print(name + " was added.\n")

def get_player_position():
    while True:
        position = input("Position: ")
        position = position.upper()
        if position in POSITIONS:
            return position
        else:
            print("Invalid position. Try again.")
            display_positions()

def get_at_bats():
    while True:
        at_bats = int(input("At bats: "))
        if at_bats >= 1 and at_bats <= 10000:
            return str(at_bats)
        else:
            print("Invalid entry. Must be from 1 to 10,000.")

def get_hits():
    while True:
        hits = int(input("Hits: "))
        if hits >= 0 and hits <= 10000:        
            return str(hits)
        else:
            print("Invalid entry. Must be from 0 to 10,000.")

def get_lineup_number(players, prompt):
    while True:
        try:
            number = int(input(prompt))
        except ValueError:
            print("Please enter a valid integer that corresponds to the player.")
            continue

        if number < 1 or number > len(players):
            print("Invalid player number. " +
                  "Please try again.")
        else:
            break

    return number

def delete_player(players):
    number = get_lineup_number(players, "Number: ")
    player = players.pop(number-1)
    write_lineup(players)
    print(player[0] + " was deleted.\n")

def move_player(players):
    old_number = get_lineup_number(players, "Current lineup number: ")
    player = players.pop(old_number-1)
    print(player[0] + " was selected.")
    new_number = get_lineup_number(players, "New lineup number: ")
    players.insert(new_number-1, player)
    print(player[0] + " was moved.\n")

def edit_player_position(players):
    number = get_lineup_number(players, "Lineup number: ")
    player = players[number-1]
    print("You selected " + player[0] + " POS=" + player[1])
    position = get_player_position()
    player[1] = position
    print(player[0] + " was updated.\n")

def edit_player_stats(players):
    number = get_lineup_number(players, "Lineup number: ")
    player = players[number-1]
    print("You selected " + player[0] +
          " AB=" + player[2] +
          " H=" + player[3])
    at_bats = get_at_bats()
    hits = get_hits()
    player[2] = at_bats
    player[3] = hits
    print(player[0] + " was updated.\n")

def display_lineup(players):
    if len(players) == 0:
        print("There are currently no players in the lineup.")        
    else:
        print("{:>11} {:>30} {:>5} {:>5} {:>5}".format("Player", "POS", "AB", "H", "AVG"))
        print("-" * 63)
        i = 1
        for player in players:
            name = player[0]
            position = player[1]
            at_bats = player[2]
            hits = player[3]
            avg = get_batting_avg(at_bats, hits)
            print("{:2} {:35} {:<5} {:<5} {:<5} {:<5}".format(i, name, position, at_bats, hits, avg))
            print()
            i += 1
    print()    

def get_batting_avg(at_bats, hits):
    try:
        avg = int(hits) / int(at_bats)
        return round(avg, 3)
    except ZeroDivisionError:
        return 0.0

def display_separator():
    print("=" * 63)

def display_title():
    print("                   Baseball Team Manager")

def display_menu():
    print("MENU OPTIONS")
    print("1 – Display lineup")
    print("2 – Add player")
    print("3 – Remove player")
    print("4 – Move player")
    print("5 – Edit player position")
    print("6 – Edit player stats")
    print("7 - Exit program")
    print()

def display_positions():
    print("POSITIONS")
    for position in POSITIONS:
        print(position + ", ", end = "")
    print()

def main():
    players = read_file()
    display_separator()
    display_title()
    display_menu()
    display_positions()
    display_separator()
    while True:
        try:
            option = int(input("Menu option: "))
        except ValueError:
            print("Not a valid option, please try again.")
            continue
        if option == 1:
            display_lineup(players)
        elif option == 2:
            add_player(players)
        elif option == 3:
            delete_player(players)
        elif option == 4:
            move_player(players)
        elif option == 5:
            edit_player_position(players)
        elif option == 6:
            edit_player_stats(players)
        elif option == 7:
            print("Bye!")
            break
        else:
            print("Not a valid option. Please try again.")
            continue

if __name__ == "__main__":
    main()
