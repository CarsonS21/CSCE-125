FILENAME = "studentsRec.txt"

def write_studentsList(studentsList):
    with open(FILENAME, "w") as file:
        for student in studentsList:
            file.write(student + "\n")    

def read_studentsList():
    studentsList = []
    with open(FILENAME) as file:
        for line in file:
            line = line.replace("\n", "")
            studentsList.append(line)
    return studentsList   

def list_studentsList(studentsList):
    for i in range(len(studentsList)):
        student = studentsList[i]
        print(str(i+1) + ". " + student)
    print()
  
def add_student(studentsList):
    student = input("student: ")
    studentsList.append(student)
    write_studentsList(studentsList)
    print(student + " was added.\n")

def delete_student(studentsList):
    index = int(input("Number: "))   
    student = studentsList.pop(index - 1)
    write_studentsList(studentsList)
    print(student + " was deleted.\n")

def mean_grades():
    fin = open(FILENAME,"r")
    print( "{0:<10}: {1:<20}: {2:<20}".format("name","grades","mean"))
    print("------------------------------------------------------------")
    for line in fin:
        line = line.split()
        if len(line) > 1:
            name = line[0]
            grades = map(float, line[1:])
            mean = sum(grades)/len(line[1:])
            grades_str=""
            for item in  (line[1:]):
                grades_str += item +" "
            print( "{0:<10}: {1:<20}: {2:<20.2f}".format(name,grades_str,mean))
        
def display_menu():
    print("The student List program")
    print()
    print("COMMAND MENU")
    print("list -  List all studentsList")
    print("add  -  Add a student")
    print("del  -  Delete a student")
    print("mean -  Calculate student's grade mean")
    print("exit -  Exit program")
    print()
    
def main():
    display_menu()
    studentsList = read_studentsList()
    while True:
        command = input("Command: ")
        if command == "list":
            list_studentsList(studentsList)
        elif command == "add":
            add_student(studentsList)
        elif command == "del":
            delete_student(studentsList)
        elif command == "mean":
            mean_grades()
        elif command == "exit":
            print("Bye!")
            break
        else:
            print("Not a valid command. Please try again.")

if __name__ == "__main__":
    main()
