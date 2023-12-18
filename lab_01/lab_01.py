
## List [Item1, Item2, Item3]
## Item {"name":"Jon", "phone":"0631234567"}

# already sorted list
list = [
    {"name":"Bob", "phone":"0631234567", "mail":"bob@example.com", "age":"17"},
    {"name":"Emma", "phone":"0631234567", "mail":"emma@example.com", "age":"18"},
    {"name":"Jon",  "phone":"0631234567", "mail":"jon@example.com", "age":"20"},
    {"name":"Zak",  "phone":"0631234567", "mail":"zak@example.com", "age":"20"}
]

def printAllList():
    for elem in list:
        strForPrint = "Student name is " + elem["name"] + ",  Phone is " + elem["phone"] + ", Mail is " + elem["mail"] + ", Age is " + elem["age"]  
        print(strForPrint)
    return

def addNewElement():
    name = input("Pease enter student name: ")
    phone = input("Please enter student phone: ")
    mail = input("Please enter student mail: ")
    age = input("Please enter student age: ")

    newItem = {"name": name, "phone": phone, "mail": mail, "age": age}

    # find insert position
    insertPosition = 0
    for item in list:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    list.insert(insertPosition, newItem)
    print("New element has been added")
    return

def deleteElement():
    name = input("Please enter name to be deleted: ")
    deletePosition = -1
    for item in list:
        if name == item["name"]:
            deletePosition = list.index(item)
            break
    if deletePosition == -1:
        print("Element was not found")
    else:
        print("Dele position " + str(deletePosition))
        # list.pop(deletePosition)
        del list[deletePosition]
    return


def updateElement():
    name = input("Please enter name to be updated: ")
    for index, student in enumerate(list):
        if name == student["name"]:
            new_name = input("Enter new name: ")
            new_phone = input("Enter new phone: ") 
            new_mail = input("Enter new mail: ")
            new_age = input("Enter new age: ")
            newElement = {"name": new_name, "phone": new_phone, "mail": new_mail, "age": new_age} 

            
            del list[index]
            insertPos = 0
            for pos, elem in enumerate(list):
                if new_name > elem["name"]:
                    insertPos = pos + 1
                else:
                    break
            list.insert(insertPos, newElement)
            print("Element has been updated")
            break
    else:
        print("Student not found")

def main():
    while True:
        chouse = input("Please specify the action [ C create, U update, D delete, P print,  X exit ] ")
        match chouse:
            case "C" | "c":
                print("New element will be created:")
                addNewElement()
                printAllList()
            case "U" | "u":
                print("Existing element will be updated")
                updateElement()
            case "D" | "d":
                print("Element will be deleted")
                deleteElement()
            case "P" | "p":
                print("List will be printed")
                printAllList()
            case "X" | "x":
                print("Exit()")
                break
            case _:
                print("Wrong choice")

main()