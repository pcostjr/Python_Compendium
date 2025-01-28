# store.py
# description: A simple program to exemplify list parallels in Python.
# author: pcostjr
# created: 10.15.2024
# last update: 10.16.2024

def add_item(list_name, list_quantity):
    item = input("Enter itemname: ").lower().strip()
    quantity = int(input("Enter quantity: ").lower().strip())
    list_name.append(item)
    list_quantity.append(quantity)
    print("Item added.")

def display(list_name, list_quantity):
    print("======= GROCERY LIST =======")
    for i in range(len(list_name)):
        # prints each item in the list, and provides the sum total as well as the per cost
        print(f"{i + 1}: {list_name[i]} x {list_quantity[i]}")
    print("============================")

def sort_list(list_name, list_quantity):
    sort_names = list_name[:]
    sort_quantity = list_quantity[:]

    # perform the bubblesort
    for i in range(len(sort_quantity) - 1):
        # assume the final value in each pass is sorted
        for j in range(len(sort_quantity) - i - 1):
            # perform the swap using a temp variable
            if sort_quantity[j] > sort_quantity[j + 1]:
                sort_quantity[j], sort_quantity[j + 1] = sort_quantity[j + 1], sort_quantity[j]
                sort_names[j], sort_names[j + 1] = sort_names[j + 1], sort_names[j]

    display(sort_names, sort_quantity)


# grocerylist parallels
item_name = ["seaweed", "rice", "chicken parm", "graham grackers", "animal crackers"]
item_quantity = [12, 22, 19, 34, 8]



running = True
while running:
    print(f"Welcome to the Shop! Select an option:\n"
          f"[1]: Add a new item to the store\n"
          f"[2]: Display contents of store\n"
          f"[3]: Display sorted contents of store\n"          
          f"[4]: Exit")
    selection = int(input("Choose an option: "))
    if selection == 1:
        add_item(item_name, item_quantity)
    elif selection == 2:
        display(item_name, item_quantity)
    elif selection == 3:
        sort_list(item_name, item_quantity)
    elif selection == 4:
        print("Goodbye.")
        exit()