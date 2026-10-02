# Week 3 Day 2 Dictionaries

# Create and Read
contacts = {"alice":"0774838834"}
print(contacts["alice"])

#add and update
contacts["bob"] = "0717633733" # adding a new key
contacts["alice"] = "07776655432" # overwriting the existing key
print(contacts) # {'alice': '07776655432', 'bob': '0717633733'}

# deleting
del  contacts["bob"] # KeyError if "bob" is missing
phone = contacts.pop("alice", None ) # returns value, or None if missing
print(phone)
print(contacts)

# safe lookup with .get()
contacts = {"alice": "077", "bob": "071"}

#print(contacts["kavi"]) # KeyError: crashes
print(contacts.get("kavi")) #None
print(contacts.get("kavi", "N/A")) # N/A

# check if a key exist
print("alice" in contacts) #True
print("kavi" in contacts) #False
# in checks keys only not values

# loop

for name , phone in contacts.items(): #alice 077, bob 071
    print(name, phone)

for name in contacts:
    print(name)

# sorted loop

for name , phone in sorted(contacts.items()):
    print(name, phone)

# contact_book.py
contacts = {}
while True:
    print("\n1. Add\n2. Look up\n3. Delete\n4. View all\n5. Quit")
    choice = input("Enter your choice:")


    if choice == "1":
        name = input("Enter the name of contacts: ").strip().lower()
        phone = input("Enter the phone number: ").strip()

        if name in contacts:
            print(f"Updated , {name}")
        else:
            print(f"Added, {name}")
        contacts[name] = phone

    elif choice == "2":
        look_name = input("Enter the  name to look up: ").strip().lower()
        if look_name in contacts:
            look_phone = contacts.get(look_name)
            print(look_name, look_phone)
        else:
            print(f"{look_name} not found")



    elif choice == "3":
        del_name = input("Enter the contact to delete: ").strip().lower()
        if del_name in contacts:
            del contacts[del_name]
            print(f"Deleted {del_name}")
        else:
            print(f"{del_name}, not found")

    elif choice == "4":
        if not contacts:
            print("no contacts")
        else:
            for name , phone in sorted(contacts.items()):
                print(name, phone)


    elif choice == "5":
        break

    else:
        print("Invalid")







