#Activity 4.2: Interactive To-Do List (using List Operations)

todo_list = []
con = 1
print(". ݁₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁. Welcome to my To-Do List . ݁₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.","\n")
print("What do you want to do today? ≽^• ˕ • ྀི≼","\n") 
while (con == 1):
    print("────۶ৎ────────۶ৎ────────۶ৎ────")
    print("ᛝ-1-ᛝ ➜  Add a task  ♫")
    print("ᛝ-2-ᛝ ➜  View tasks  ♡⸝⸝")
    print("ᛝ-3-ᛝ ➜  Mark as done to a task  ͙͘͡★")
    print("ᛝ-4-ᛝ ➜  Exit  ಄")
    print("────۶ৎ────────۶ৎ────────۶ৎ────")
    choice = int(input("Please choose 1-4 : "))

    if (choice == 1):
        addList = input("Please add the new Todo-List : ")
        todo_list.append(addList)

    elif (choice == 2):
        print("This is all of your task : ",todo_list)

    elif(choice == 3):
        index = int(input("Please idex the list : "))
        print(todo_list[index-1]," is now mark as done!! ꉂ(˵˃ ᗜ ˂˵)")
        todo_list.remove(todo_list[index-1])

    elif(choice == 4):
        print("Thank you for your hard working!! ⸜(｡˃ ᵕ ˂ )⸝♡")
        break

    else:
        print("Hey! Please type only 1-4")

    print("\n")