#  Week 3 Day 5 to-co app

# Step 1: Why plan first

#Writing what each option does before coding stops you from rewriting later. For each menu option, answer three questions:

#Option	Input needed	Changes	Prints
#View	none	nothing	numbered list
#Complete	task number	flips done to True	confirmation
#Delete	task number	removes a dict	confirmation
#Quit	none	nothing	nothing


#Step 2: Why a list of dictionaries

#One task has two facts: its text and whether it's done. A dict holds both, and a list holds many tasks in order.

#python
#todos = [
#    {"task": "buy milk", "done": False},
#    {"task": "study python", "done": True},
#]
#The list gives order and numbering (position 0, 1, 2...).
#Each dict gives named fields, so t["task"] is clearer than remembering "index 0 is the text".

#Step 3: Reading nested data, one step at a time

#python
#todos[1]["done"]
#todos[1] takes the item at index 1. That is the dict {"task": "study python", "done": True}.
#["done"] looks up the key "done" in that dict. Result: True.

#Read left to right. Each [] goes one level deeper. You can write to it the same way: todos[1]["done"] = False.

#Step 4: The view loop, line by line

#python
#for i, t in enumerate(todos, 1):
#    mark = "x" if t["done"] else " "
#    print(f"{i}. [{mark}] {t['task']}")
#enumerate(todos, 1) gives a counter i starting at 1, plus each dict t.
#"x" if t["done"] else " " is a one-line if/else. It gives "x" when done is True, otherwise a space.
#The f-string inserts i, mark, and the task text. Inside an f-string quoted with ", use ' for dict keys (t['task']), or Python ends the string early.

#Step 5: Why done is a bool

#You can use it directly in a condition: if t["done"]:. With strings like "yes" or "Yes" or "y", every comparison can mismatch on spelling or case. A bool has exactly two values, so there is nothing to mistype.

#Milestone 2 todos.py
todos = []
while  True:
    print("\n1. Add\n2. View\n3. Complete\n4/ Delete\n5. Quit ")
    choice = input("Enter your choice: ").strip()

    if choice == "1":
        task = input("Enter your task: ").strip()
        if task == "":
            print("Empty Task")
        else:
            todos.append({"task":task, "done":False})
            print("Added")
    elif choice == "2":
        if len(todos) == 0:
            print("No Tasks")
        else:
            for i, task in enumerate(todos,1):
                mark = "X" if task["done"] else ""
                print(f"{i}. [{mark}] {task['task']}")
    elif choice == "3":
        print("Not build yet")
    elif choice == "4":
        print("Not build yet")
    elif choice == "5":
        break
    else:
        print("Invalid Choice")

