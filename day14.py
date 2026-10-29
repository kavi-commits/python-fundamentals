# day 7 , week 3

# try/except rules:
try:
    n = int(input("Number: "))
except ValueError:                 # catch the specific error
    print("Enter a number")
except (EOFError, KeyboardInterrupt):
    print("\nbye")

# catch specific exceptions only. Never use a bare except:, because it hides real bugs
#  Keep the try body small, so you know what failed

#  import json
#
# FILE = "todos.json"
#
# try:
#     with open(FILE, "r") as f:
#         todos = json.load(f)
# except (FileNotFoundError, json.JSONDecodeError):
#     todos = []
#
# if not isinstance(todos, list):
#     todos = []
# try:
#     while True:
#         print("\n1. Add\n2. View\n3. Complete\n4. Delete\n5. Quit")
#         choice = input("Enter your choice: ").strip()
#
#         if choice == "1":
#             task = input("Enter your task: ").strip()
#             if task == "":
#                 print("Empty task")
#             else:
#                 todos.append({"task": task, "done": False})
#                 with open(FILE, "w") as f:
#                     json.dump(todos, f, indent=2)
#                 print("Added")
#
#         elif choice == "2":
#             if len(todos) == 0:
#                 print("No tasks")
#             else:
#                 for i, t in enumerate(todos, 1):
#                     mark = "x" if t["done"] else " "
#                     print(f"{i}. [{mark}] {t['task']}")
#
#         elif choice == "3":
#             if len(todos) == 0:
#                 print("No tasks")
#             else:
#                 for i, t in enumerate(todos, 1):
#                     mark = "x" if t["done"] else " "
#                     print(f"{i}. [{mark}] {t['task']}")
#                 try:
#                     n = int(input("Task number to complete: ").strip())
#                     if 1 <= n <= len(todos):
#                         todos[n - 1]["done"] = True
#                         with open(FILE, "w") as f:
#                             json.dump(todos, f, indent=2)
#                         print("Completed")
#                     else:
#                         print("Invalid number")
#                 except ValueError:
#                     print("Enter a number")
#
#         elif choice == "4":
#             if len(todos) == 0:
#                 print("No tasks")
#             else:
#                 for i, t in enumerate(todos, 1):
#                     mark = "x" if t["done"] else " "
#                     print(f"{i}. [{mark}] {t['task']}")
#                 try:
#                     n = int(input("Task number to delete: ").strip())
#                     if 1 <= n <= len(todos):
#                         removed = todos.pop(n - 1)
#                         with open(FILE, "w") as f:
#                             json.dump(todos, f, indent=2)
#                         print(f"Deleted: {removed['task']}")
#                     else:
#                         print("Invalid number")
#                 except ValueError:
#                     print("Enter a number")
#
#         elif choice == "5":
#             break
#
#         else:
#             print("Invalid choice")
#
# except (KeyboardInterrupt, EOFError):
#     print("\nBye")
