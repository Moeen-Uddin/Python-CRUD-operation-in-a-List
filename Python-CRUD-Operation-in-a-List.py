names = ["moeen", "oishi", "sumyta", "uddin"]
print(f"The name list is : {names}")
while True:
    user_input = input("Press 1 for creat ,Press 2 for read,Press 3 for delete,Press 4 for edit,Press Enter to exit : ")
    if user_input == "":
        break
    elif user_input == "1":
        names.append(input("Enter a new name :"))
        print(f"New list is : {names}")
    elif user_input == "2":
        print(names)
    elif user_input == "3":
        # delete
        deletedName = input("Enter name you want to delete : ").strip()
        if deletedName in names:
            names.remove(deletedName)
            print(f"{deletedName} has been deleted from the list.The new list is : {names}")
        else:
            print(f"{deletedName} does not exist in the list.The name list is : {names}")

    elif user_input == "4":
        # edit
        editedName = input("Enter name you want to edit : ").strip()
        if editedName in names:
            newName = input("Enter replaced name : ").strip()
            index = names.index(editedName)
            names[index] = newName  # Update the name at that index
            print(f"{editedName} has been updated to {newName}.")
            print(f"New name list is : {newName}.")
        else:
            print(f"{editedName} does not exist in the list.")
