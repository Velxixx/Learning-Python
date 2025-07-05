# import math  # Math Modules

# eggs_count = 38  # Unused Variables
# \n Creates a new line, \" and \' Called Escape Sequence
# company_name = "AcVisa \nCorporation"
# len command get the amount of characters, converts it to numbers
# company_name_lenght = len(company_name)

# x = 1  # Examples of variables
# y = 3

# print(len(company_name))

# if company_name_lenght < 8:
# print("Company name is to short")
# else:
# print("Company name is available")

# funny_joke = "Gaydwaydawydwaydawdawyda"
# funny_joke_count = len(funny_joke)
# first = "Ricardo"
# last = "Norat"
# f is a formatted string brackets call the variables
# full_name = f"{first} {last}"

# print(funny_joke_count)
# print(funny_joke[0:3])  # Will print only 3 letters from 0 to 3
# car = "Ferrari"
# print(car[3:-1])
# print(company_name)
# print(full_name)

# String methods

# project_name = "   project python"

# print(project_name.upper())  # Uppercase the STRING
# print(project_name.lower())  # Lowercase the STRING
# print(project_name.title())  # Sets uppercase for titles
# print(project_name.strip())  # Deletes any space
# print(project_name.find("python"))  # Finds word, returns as index
# print(project_name.replace("python", "snake"))  # Replaces
# print("python" in project_name)  # Returns a boolean (True or False) In
# print("snake" not in project_name)  # Return boolean Not

# Small number project Add verify integer from imput
# health_input = input("How Much health your character has?: ")
# health_int = int(health_input)
# damage_input = input("How much damage you do: ")
# damage_int = int(damage_input)

# print(f"Healthpoints Remaining: {health_int - damage_int}")

# Numbers
# print(20 + 5)
# print(20 - 3)
# print(10 * 5)
# print(20 / 3)
# print(20 // 3)
# print(10 % 3)
# print(20 ** 3)

# print(round(2.9))  # Round the Number
# print(abs(-2.9))  # Return absolute value of a number
# print(math.ceil(2.2))  # For getting the ceiling of a number

# Example of Augmented Assignmet operator

# x = 10
# x = x + 3  # They are all the same
# x += 3

# Type conversions

# input_age = input("Your age: ")
# input_integer = int(input_age)
# year_born = input("Birth year: ")
# year_born_int = int(year_born)

# print(f"Your age is: {input_integer} and you where born in {year_born_int}")
# print(type(year_born))

# All Type conversions

# int()
# float()
# bool() Boolean Falsy "" Empty String is False 0 is False Object None is False
# str()

# Comparison Operators

# 10 > 3 True
# 10 >= 3 True
# 10 < 20 True
# 10 <= 20 True
# 10 == 10 True
# 10 == "10" False
# 10 != "10" True

# Conditional Statements
# weight_limit = 500
# current_weight = input("Weight: ")
# current_weight_int = int(current_weight)

# if current_weight_int > weight_limit:
# elegible = f"You are over the weight limit\nCurrent weight limit is: {weight_limit}\nYour Weight: {current_weight_int}"
# elif current_weight_int == weight_limit:
# elegible = "You are lucky pal!"
# else:
# elegible = "You are under the weight limit"
# print(elegible)

# Code above ternary same code but with only 2 options and 1 line needs variables from above

# elegible = f"You are over the weight limit\nCurrent weight limit is: {weight_limit}\nYour Weight: {current_weight_int}" if current_weight_int > 500 else "You are under the weight limit"
# print(elegible)

# Logical operators and.or.not
# region_america = False

# minimun_player_level = 20
# player_level_input = input("Player level: ")
# player_level_int = int(player_level_input)
# player_level_decision = minimun_player_level < player_level_int

# player_rank_minimun = 2
# player_rank_input = input(
# "What is your rank?\n1.Silver\n2.Gold\n3.Platinum\n4.Diamond\nInsert a number: ")
# player_rank_int = int(player_rank_input)
# player_rank_decision = player_rank_int >= player_rank_minimun


# if (player_level_decision and player_rank_decision) and not region_america:
# finals_decision = "You qualify for the finals!"
# else:
# finals_decision = "You do not qualify!"
# print(finals_decision)

# high_income = False
# good_credit = True
# student = True

# if (high_income or good_credit) and not student:
#    print("Eligible")
# else:
#    print("Not Eligible")

# Chaining commparisong operators
# level must be between 20 and 85

# level = 45

# if level >= 45 and level < 85:
# print("You qualify")

# Chained comparison operators same code better written!

# if 45 <= level < 85:
# print("Qualified")

# For Loops

# message = "car extended warranty"

# for number in range(0, 50):
# print(message.title(), number + 1, (number + 1) * ".")
# if succesful:
# print("Succesful")
# break
# else:
# print("Could not reach client")

# import secrets
# import random

# agent = random.choice(
#     ["Luke", "Carlos", "Josh", "Fred", "Dominic", "NPC NAV"])
# print(f"This is the random person chosen: {agent}")

# succesful = True

# client_message = "Hi this is AcVisa reaching you about your new adquired game code"
# generated_code = secrets.token_hex(25)

# for number in range(5):
#     print(client_message)
#     if succesful:
#         client_message = input(
#             "Would you like your code to be send via email Y/N: ")
#         client_reply = str(client_message.lower())
#         if client_reply == "y":
#             print(f"Here is your code: {generated_code}")
#             break
#         elif client_reply == "n":
#             print("Please use this link to redeem your code anytime: https://www.youtube.com/watch?v=xvFZjo5PgG0&list=RDxvFZjo5PgG0&start_radio=1")
#             break
#         else:
#             print("Invalid input please try again!")
# else:
#     print("Client could not be reached")

# Nested loops

# for apples in range(8):
#     for oranges in range(10):
#         print(f"Apples quantity: {apples} Oranges quantity: {oranges}")

# Iterables

# for text in range(1, 6):
#     print(f"{text} {(text) * "."}")
#     break

# enumerate counts index for each string
# for bond in enumerate("Galaxy", 1):
#     print(bond)

# for index, letter in enumerate("Galaxy", 1):
#     print(f"{letter} {index}")

# succesful = False

# for number, word in enumerate("Destiny", ):
#     print(f"{word} Position: {number} {(number) * "."}")
#     if succesful:
#         print("First letter was sent succesfully")
#         break
# else:
#     print("Full word has been sent")

# While loops

# command = ""

# while command.lower() != "exit":
#     command = input("> Type here: ")
#     print(f"Here is what you typed: {command}")

# Infinite Loops Same output as a while loop but it runs permanently, break is important

# while True:
#     command = input("> Type here: ")
#     print(f"Here is what you typed: {command}")
#     if command.lower() == "quit":
#         break

# iterate numbers and then check if each number is a even number

# try:
#     a_input_string = input("Minimun number: ")
#     b_input_string = input("Max number: ")
#     a_int = int(a_input_string)
#     b_int = int(b_input_string)
#     random_number = random.randint(a_int, b_int)
#     if random_number % 2 == 0:
#         print(f"Your random number is a even number: {random_number}")
#     elif random_number % 2 != 0:
#         print(f"Your random number is a uneven number: {random_number}")
# except ValueError:
#     print("Invalid!")

# count = 0

# for number in range(1, 11):
#     if number % 2 == 0:  # Prints every even number on set range
#         count += 1 # Counting
#         print(number)

# print(f"I have counted {count} even numbers :)")

# How to write own functions
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
        if error == True and item_int < 5:
            print(f"You have chosen {item_list[item_int]}")
            break
        elif error == True and item_int >= 5:
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
        if error_rarity == True and rarity_int < 5:
            print(f"You have chosen {rarity_list[rarity_int]}")
            break
        elif error_rarity == True and rarity_int >= 5:
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
