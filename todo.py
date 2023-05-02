# Adds a new task to a todo list.
import csv, os

# Appends a new item to the .csv file.
def addNewItem(list):
    answer = "Y"
    while answer == "Y":
        newItem = {"task": input("Input new TODO item: " + "\n"), "complete": False}
        list.append(newItem)
        answer = input("Continue [Y] or Save & Exit [N]?\t")

    with open("todoList.csv", "w", newline="") as updated:
        keys = list[0].keys()
        writer = csv.DictWriter(updated, keys)
        writer.writeheader()
        writer.writerows(list)
        
def listAllItems(): # Creates a list object of all tasks in the TODO List
    os.system("cls")
    with open("todoList.csv", "r") as input:
        todoList = []
        reader = csv.DictReader(input)
        n = 1
        for row in reader:
            todoList.append(row)
            if row["complete"] == str(False):
                print(str(n) + ". " + "[ ] " + row["task"])
            else:
                print(str(n) + ". " + "[x] " + row["task"])
            n += 1
    return todoList
    
    
def updateItem(list):
        try:
            choice = int(input("Which item have you completed? \t")) - 1
            for i in range(len(list)):
                if i == choice:
                    if list[i]["complete"] == False: # Flips the bool value:
                        updatedTask = {"task": list[i]["task"], "complete": True}
                    else: 
                        updatedTask = {"task": list[i]["task"], "complete": False}
                    list.pop(i)
                    list.insert(i, updatedTask)
        except ValueError:
            print("Please enter a number.")

                
        # Rewrites todoList.csv with updated value.
        with open("todoList.csv", "w", newline="") as updated:
            keys = list[0].keys()
            writer = csv.DictWriter(updated, keys)
            writer.writeheader()
            writer.writerows(list)

                
            
# Program Start!
# Print the list:
todoList = listAllItems()

option = ""
while True:
    print("\nWhat would you like to do? \n")
    option = input("[1] Update List.\n[2] Add a New Item.\n[3] List Items\n[4] Exit.\n")
    if option == "1":
        updateItem(todoList)
    elif option == "2":
        addNewItem(todoList)
    elif option =="3":
        listAllItems()
    elif option == "4":
        quit()
