import sys


def item_display(item_name, rarity):
    print(f"You have chosen to display your {item_name}")
    print(f"Its rarity is {rarity}")


# LIST OF ITEMS

rarity_list = ["0. Common", "1. Uncommon",
               "2. Rare", "3. Epic", "4. Legendary"]
item_list = ["0. Hammer", "1. Sword",
             "2. Pen", "3. Bow", "4. Gun"]

# NEW CODE FOR ITEMS

for number in range(5):
    try:
        item_selection = input(f"Select your item: {item_list[0:5]}")
        item_int = int(item_selection)
        error = True
        if error and item_int < 5:
            print(f"You have chosen {item_list[item_int]}")
            break
        if error and item_int >= 5:
            print("Item not recognized")
    except ValueError:
        print("Only insert numbers and try again!")
else:
    error = False
    print("Missed attempts relaunch code!")
    sys.exit()

# NEW CODE FOR RARITY

for number in range(5):
    try:
        rarity_selection = input(f"Select rarity: {rarity_list[0:5]}")
        rarity_int = int(rarity_selection)
        error_rarity = True
        if error_rarity and rarity_int < 5:
            print(f"You have chosen {rarity_list[rarity_int]}")
            break
        if error_rarity and rarity_int >= 5:
            print("Item not recognized")
    except ValueError:
        print("Only insert numbers and try again!")
else:
    error_rarity = False
    print("Missed attempts relaunch code!")
    sys.exit()

try:
    item_display(item_list[item_int], rarity_list[rarity_int])
except ValueError:
    print("Error when displaying items!")
