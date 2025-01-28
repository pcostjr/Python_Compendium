# grocerylist_stock.py
# description: a program that simulates a grocery list. Users are allowed to add, remove, display contents,
# and calculate the cost of the grocery list. grocery items are stored as (name, price, quantity)
# this version does not use functions or objects, just a long chain of if statements
# author: pcostjr
# created: 09.19.2024
# last update: 10.1.2024

# checklist:
# [X] Add an item
# [ ] Make it so that not using an index will just append it to the end
# [X] Remove an item
# [x] Display List contents with different priority ( input order, price(l/h), quantity (l/h)
# [-] Calculate total cost & total items
# [X] Exit

# grocerylist parallels
gl_name = []
gl_quantity = []
gl_cost = []

# set runflag to true and go
running = True
while running:
    print(f"Welcome to GroceryList! Select an option:\n"
          f"[1]: Add a new item to the list\n"
          f"[2]: Remove an item from the list\n"
          f"[3]: Display contents\n"
          f"[4]: Exit")
    selection = int(input("Choose an option: "))
    if selection == 1:
        gl_name.append(input("Enter the name of the item: "))
        gl_cost.append(float(input("Enter the cost of the item: ")))
        gl_quantity.append(int(input("Enter the quantity of the item: ")))
        print("Item added.")
    elif selection == 2:
        item = input("Enter the EXACT name of the item you'd like to remove")
        drop = gl_name.index(item)
        del gl_name[drop]
        del gl_quantity[drop]
        del gl_cost[drop]
        print("Item removed.")
    elif selection == 3:
        print(f"Please select list display order.\n"
              f"[1]: Default\n"
              f"[2]: Price: High to Low\n"
              f"[3]: Price: Low to High\n"
              f"[4]: Quantity: High to Low\n"
              f"[5]: Quantity: Low to High\n"
              f"[6]: Alphabetical Order")
        selection = int(input("Choose an option: "))
        # if selection is 1, display the list as it was entered
        if selection == 1:
            print("======= GROCERY LIST =======")
            for i in range(len(gl_name)):
                # prints each item in the list, and provides the sum total as well as the per cost
                print(f"{i + 1}: {gl_name[i]} x {gl_quantity[i]} | ${gl_cost[i] * gl_quantity[i]:.2f}"
                      f" (${gl_cost[i]:.2f} ea.)")
            print("============================")

        # price high to low: perform insertion sort
        elif selection == 2:
            # create three copies of the list
            # [:] creates an exact copy without referencing lists
            tmp_name = gl_name[:]
            tmp_quantity = gl_quantity[:]
            tmp_cost = gl_cost[:]

            # perform an insertion sort on all three entries in the list
            for i in range(1, len(tmp_cost)):
                # the key is the item we're looking to sort
                key_name = tmp_name[i]
                key_cost = tmp_cost[i]
                key_quantity = tmp_quantity[i]
                j = i - 1

                # while we have values to iterate, and key is greater than numbers
                while j >= 0 and key_cost > tmp_cost[j]:
                    # swap the locations of the values
                    tmp_name[j + 1] = tmp_name[j]
                    tmp_cost[j+1] = tmp_cost[j]
                    tmp_quantity[j + 1] = tmp_quantity[j]
                    j -= 1
                # reserve a new key
                tmp_name[j + 1] = key_name
                tmp_cost[j + 1] = key_cost
                tmp_quantity[j + 1] = key_quantity

            # default print but with the temp lists now
            print("======= GROCERY LIST =======")
            for i in range(len(tmp_name)):
                # prints each item in the list, and provides the sum total as well as the per cost
                print(f"{i + 1}: {tmp_name[i]} x {tmp_quantity[i]} | ${tmp_cost[i] * tmp_quantity[i]:.2f}"
                      f" (${tmp_cost[i]:.2f} ea.)")
            print("============================")

        # price low to high
        # exactly the same as above, with the symbol reversed
        elif selection == 3:
            # create three copies of the list
            # [:] creates an exact copy without referencing lists
            tmp_name = gl_name[:]
            tmp_quantity = gl_quantity[:]
            tmp_cost = gl_cost[:]

            # perform an insertion sort on all three entries in the list
            for i in range(1, len(tmp_cost)):
                # the key is the item we're looking to sort
                key_name = tmp_name[i]
                key_cost = tmp_cost[i]
                key_quantity = tmp_quantity[i]
                j = i - 1

                # while we have values to iterate, and key is greater than numbers
                while j >= 0 and key_cost < tmp_cost[j]:
                    # swap the locations of the values
                    tmp_name[j + 1] = tmp_name[j]
                    tmp_cost[j + 1] = tmp_cost[j]
                    tmp_quantity[j + 1] = tmp_quantity[j]
                    j -= 1
                # place the key in the corresponding slot
                tmp_name[j + 1] = key_name
                tmp_cost[j + 1] = key_cost
                tmp_quantity[j + 1] = key_quantity

            # default print but with the temp lists now
            print("======= GROCERY LIST =======")
            for i in range(len(tmp_name)):
                # prints each item in the list, and provides the sum total as well as the per cost
                print(f"{i + 1}: {tmp_name[i]} x {tmp_quantity[i]} | ${tmp_cost[i] * tmp_quantity[i]:.2f}"
                      f" (${tmp_cost[i]:.2f} ea.)")
            print("============================")

        # quantity high to low
        # same as 2, but now we sort on quantity
        elif selection == 4:
            # create three copies of the list
            # [:] creates an exact copy without referencing lists
            tmp_name = gl_name[:]
            tmp_quantity = gl_quantity[:]
            tmp_cost = gl_cost[:]

            # perform an insertion sort on all three entries in the list
            for i in range(1, len(tmp_quantity)):
                # the key is the item we're looking to sort
                key_name = tmp_name[i]
                key_cost = tmp_cost[i]
                key_quantity = tmp_quantity[i]
                j = i - 1

                # while we have values to iterate, and key is greater than numbers
                while j >= 0 and key_quantity > tmp_quantity[j]:
                    # swap the locations of the values
                    tmp_name[j + 1] = tmp_name[j]
                    tmp_cost[j + 1] = tmp_cost[j]
                    tmp_quantity[j + 1] = tmp_quantity[j]
                    j -= 1
                # reserve a new key
                tmp_name[j + 1] = key_name
                tmp_cost[j + 1] = key_cost
                tmp_quantity[j + 1] = key_quantity

            # default print but with the temp lists now
            print("======= GROCERY LIST =======")
            for i in range(len(tmp_name)):
                # prints each item in the list, and provides the sum total as well as the per cost
                print(f"{i + 1}: {tmp_name[i]} x {tmp_quantity[i]} | ${tmp_cost[i] * tmp_quantity[i]:.2f}"
                      f" (${tmp_cost[i]:.2f} ea.)")
            print("============================")

        # quantity low to high same as above, but with the comparator flipped
        elif selection == 5:
            # create three copies of the list
            # [:] creates an exact copy without referencing lists
            tmp_name = gl_name[:]
            tmp_quantity = gl_quantity[:]
            tmp_cost = gl_cost[:]

            # perform an insertion sort on all three entries in the list
            for i in range(1, len(tmp_quantity)):
                # the key is the item we're looking to sort
                key_name = tmp_name[i]
                key_cost = tmp_cost[i]
                key_quantity = tmp_quantity[i]
                j = i - 1

                # while we have values to iterate, and key is greater than numbers
                while j >= 0 and key_quantity < tmp_quantity[j]:
                    # swap the locations of the values
                    tmp_name[j + 1] = tmp_name[j]
                    tmp_cost[j + 1] = tmp_cost[j]
                    tmp_quantity[j + 1] = tmp_quantity[j]
                    j -= 1
                # reserve a new key
                tmp_name[j + 1] = key_name
                tmp_cost[j + 1] = key_cost
                tmp_quantity[j + 1] = key_quantity

            # default print but with the temp lists now
            print("======= GROCERY LIST =======")
            for i in range(len(tmp_name)):
                # prints each item in the list, and provides the sum total as well as the per cost
                print(f"{i + 1}: {tmp_name[i]} x {tmp_quantity[i]} | ${tmp_cost[i] * tmp_quantity[i]:.2f}"
                      f" (${tmp_cost[i]:.2f} ea.)")
            print("============================")

        elif selection == 6:
            # create three copies of the list
            # [:] creates an exact copy without referencing lists
            tmp_name = gl_name[:]
            # INDEXOF THE ALREADY SORTED LIST. THAT'S WHAT WE'RE LOOKING FOR.
            tmp_quantity = gl_quantity[:]
            tmp_cost = gl_cost[:]

            

    elif selection == 4:
        # if the user chooses to display the list, do so before quitting
        if input("Would you like to display the final list? (y / n)") == "y":
            print("======= GROCERY LIST =======")
            for i in range(len(gl_name)):
                # prints each item in the list, and provides the sum total as well as the per cost
                print(
                    f"{i + 1}: {gl_name[i]} x {gl_quantity[i]} | ${gl_cost[i] * gl_quantity[i]:.2f}"
                    f" (${gl_cost[i]:.2f} ea.)")
            print("============================")
        # quit program
        print("Exiting.")
        running = False
    else:
        print("Sorry, I'm not sure what to do with that option.")
