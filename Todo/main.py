import os
print("[ToDo App 1.5]")

base = open("base.txt", "w")
base.close()

ListOfToDos = []

while True:
    #######
    def ShowToDos():
        # global ListOfToDos
        with open("base.txt", "r") as file:
            ListOfToDos = file.read().split("\n")
        ListOfToDos = ListOfToDos[:-1]
        if ListOfToDos == [""]:
            ListOfToDos = []
            with open("base.txt", "w+") as f:
                    f.write("\n".join(ListOfToDos))
        if ListOfToDos == []:
            print("List of todos in empty")
        else:
            for i in ListOfToDos:
                print(f"({ListOfToDos.index(i) + 1}) => {i}")
    ########
    
    def AddToDos():
        item = input("Item: ")
        if input("Is it clear? (y/n): ").lower() == "y":
            with open("base.txt", "a") as file:
                file.write(item + "\n")
            print("Add successfully")
        else:
            print("Add Canceled !")

    ########
    
    def RemoveToDos():
        os.system("cls")
        ShowToDos()
        Item = input("\nItem: ")
        with open("base.txt", "r") as file:
            ListOfToDos = file.read().split("\n")
            ListOfToDos = ListOfToDos[:-1]
        if input("Is it clear? (y/n): ").lower() == "y":

                if Item.isdigit():

                    try:
                        del ListOfToDos[int(Item)-1]
                        with open("base.txt", "w+") as reFile:
                            reFile.write("\n".join(ListOfToDos)+"\n")

                    except :
                        print("The index you entered could not be found")
                        RemoveToDos()

                    else:
                        print("Remove Successfully")
                
                else:

                    try:
                        ListOfToDos.remove(Item)
                        with open("base.txt", "w+") as reFile:
                            reFile.write("\n".join(ListOfToDos)+"\n")
                    
                    except :
                        print("The ToDo you entered could not be found")
                        RemoveToDos()
                    
                    else:
                        print("Remove Successfully")
                
        else:
            print("Remove Cancelled")
        
        

    ########
    
    def UpdateToDos():
        os.system("cls")
        ShowToDos()
        Item = input("\nItem: ")
        changer = input("New item: ")
        if input("Is it clear? (y/n): ").lower() == "y":

            with open("base.txt", "r") as file:
                ListOfToDos = file.read().split("\n")
                ListOfToDos = ListOfToDos[:-1]
                if Item.isdigit():

                    try:
                        ListOfToDos[int(Item)-1] = changer
                        with open("base.txt", "w+") as reFile:
                            reFile.write("\n".join(ListOfToDos)+"\n")

                    except :
                        print("The index you entered could not be found")
                        RemoveToDos()

                    else:
                        print("Update Successfully")
                
                else:

                    try:
                        ListOfToDos[ListOfToDos.index(Item)] = changer
                        with open("base.txt", "w+") as reFile:
                            reFile.write("\n".join(ListOfToDos)+"\n")
                    
                    except :
                        print("The ToDo you entered could not be found")
                        RemoveToDos()
                    
                    else:
                        print("Update Successfully")

        else:
            print("Update Cancelled")
    ########

    def ClearToDos():
        if input("Is it clear? (y/n): ").lower() == "y":
            with open("base.txt", "w+") as file:
                file.write("")
            print("Clear successfully")
        else:
            print("Clear Cancelled")


    def Command():
        print("\n(1)Show ToDos\n(2)Add ToDos\n(3)Remove ToDos\n(4)Update ToDos\n(5)Clear List\n(6)Exit App\n")
        command = input(">>> ")
        if command == "1":
            ShowToDos()
        elif command == "2":
            AddToDos()
        elif command == "3":
            RemoveToDos()
        elif command == "4":
            UpdateToDos()
        elif command == "5":
            ClearToDos()
        elif command == "6":
            os.system("cls")
            exit()
        else:
            print("Command not found. Please try again.")
            Command()

    Command()