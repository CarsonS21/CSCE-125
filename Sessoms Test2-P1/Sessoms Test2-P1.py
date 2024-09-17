#Sessoms Test2-P1
#Carson Sessoms
#sessomsc@usca.edu
#test 2
#imports contacts and allows the user to add or change or remove contacts
#3/15/2023
import csv
FILENAME = "contacts.csv"
MENU_OPTIONS = ("list", "view", "add", "del", "exit")

def read_contact_list():
    contact_list = []
    with open(FILENAME) as file:
        for line in file:
            line = line.replace("\n", "")
            contact_list.append(line)
    return contact_list

def display_contacts(contact_list):
    for i in range(len(contact_list)):
        contact = contact_list[i]
        print(str(i+1) + ". " + contact)
    print()

#def view_contact(contact_list):
def add_contact(contact_list):
    name = input("Name: ")
    email = input("Email: ")
    phone = input("Phone: ")

    contact = []
    contact.append(name)
    contact.append(email)
    contact.append(phone)
    contact_list.append(contact)
def del_contact(contact_list):
    number = get_contact_number(contact_list, "Number: ")
    contact = contact_list.pop(number-1)
    print(contact + " was deleted. \n")
 
def get_contact_number(contact_list, prompt):
    while True:
        try:
            number = int(input(prompt))
        except ValueError:
            print("Invalid integer. Please try again.")
            continue
        
        if number < 1 or number > len(contact_list):
            print("Invalid contact number. " +
                  "Please try again.")
        else:
            break

    return number

def display_menu():
    print("\t\t Contact Manager")
    print()
    print("COMMAND MENU")
    print("---------------------------------------------------")
    print("list - Display all contacts")
    print("view - View a contact")
    print("add - Add a contact")
    print("del - Delete a contact")
    print("exit - Exit program")
    print()
def main():
    display_menu()
    contact_list = read_contact_list()
    while True:
        command = input("Command: ")
        if command == "list":
            display_contacts(contact_list)
        elif command == "view":
            view_contact(contact_list)
        elif command == "add":
            add_contact(contact_list)
        elif command == "del":
            del_contact(contact_list)
        elif command == "exit":
            print("Bye!")
            break
        else:
            print("Not a valid command. Please retry.")
if __name__ == "__main__":
    main()
    
