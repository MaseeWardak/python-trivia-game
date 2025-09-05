# ISU_GAME.py
# ISU Game By Masee Wardak

import os

# Function to clear the screen
def clear_screen():
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For macOS and Linux
        os.system('clear')


levels = ['a', 'b', 'c']
completed_levels = []  # List to track completed levels
points = 3  # The number of lives.

# Function that will display remaining lives
def display_lives(points):
    print(f"Lives remaining: {points}")

# Message if you lose:
lost = ("You have run out of lives!\n"
        "Wisdom has been chasing you, but you have always been faster.\n"
        "Game over, better luck next time")

# Question for Canada Level.
q_one_canada = ("Trump has invaded Canada saying he wants to make it the 51st state!!\n"
                "What would a real patriot do?\n"
                "Press A to Fight for Canada\n"
                "Press B to Fight for Trump\n"
                "Press C to Migrate to Europe\n"
                "Press D to Do nothing")

# Question for Hydrocity level.
q_two_hydrocity = ("What type of rock cannot be found in the ocean?\n"
                   "Press A for igneous rock.\n"
                   "Press B for sedimentary rock\n"
                   "Press C for a dry rock\n"
                   "Press D for metamorphic rock")

# Question for Giza:
q_three_giza = ("Why did the British not take the pyramids of Giza with them to Great Britain?\n"
                "Press A for They did take them! Giza is in England.\n"
                "Press B for The Egyptians were brave and didn't allow them to be stolen.\n"
                "Press C for The pyramids are not significant enough.\n"
                "Press D for The pyramids were too heavy for the British to carry, so they left them.")

# Starting screen
while True:
    start = input('Greetings Professor!, click S to start or click T for tutorial').lower()
    if start == 't':
        clear_screen()
        print('This is a text-based Trivia game')
        print('It has three levels, You start with 10 lives and each incorrect answer deducts one point')
        print('You may proceed to the next level after answering correctly')
    elif start == "s":
        clear_screen()
        print("You may now choose which level to start from!")
        print('The available options are: Canada, Hydrocity, Giza')
        print('Press A for Canada')
        print('Press B for Hydrocity')
        print('Press C for Giza')
        while True:
            level = input("Which level would you like to play? ").lower()
            if level in levels and level not in completed_levels:
                break  # This should exit the loop if a valid level name is entered and not completed
            else:
                print("Please enter a valid level from the list or check for spelling errors ")

        break

# Canada Level
if level == 'a':
    clear_screen()
    print('Welcome to Canada!')
    while True:
        question_one = input(q_one_canada).lower()
        clear_screen()
        if question_one == 'b':
            print('Traitor!, You will be deported to wherever your ancestors came from and you lose a point now!')
            points -= 1
            display_lives(points)
            if points == 0:
                print(lost)
                break
        elif question_one in ['c', 'd']:
            print('I thought you were brave. You lost a point')
            points -= 1
            display_lives(points)
            if points == 0:
                print(lost)
                break
        elif question_one == 'a':
            print('I knew you were a patriot, let us proceed to the next level!')
            completed_levels.append('a')  # Mark as completed after answering correctly
            if len(completed_levels) == 3:
                print("Congratulations! You have completed all levels!")
                break
            while True:
                print('Good Job! Press B for Hydrocity or Press C for Giza')
                level = input("Which level would you like to play? ").lower()
                if level in levels and level not in completed_levels:
                    break
                else:
                    print("Please choose a valid, incomplete level.")
            break

# Hydrocity Level
if level == 'b':
    clear_screen()
    print('Welcome to Hydrocity! The land of many rivers and oceans!')
    while True:
        question_two = input(q_two_hydrocity).lower()
        clear_screen()
        if question_two in ['a', 'b', 'd']:
            print('Wrong, try again.')
            points -= 1
            display_lives(points)
            if points == 0:
                print(lost)
                break
        elif question_two == 'c':
            print("Ah ha, clever one ain't it? You may proceed to the next level now!")
            completed_levels.append('b')  # Mark as completed after answering correctly
            if len(completed_levels) == 3:
                print("Congratulations! You have completed all levels!")
                break
            while True:
                print('You are almost there! Press A for Canada or Press C for Giza')
                level = input("Which level would you like to play? ").lower()
                if level in levels and level not in completed_levels:
                    break
                else:
                    print("Please choose a valid, incomplete level.")
            break

# Canada Level
if level == 'a':
    clear_screen()
    print('Welcome to Canada!')
    while True:
        question_one = input(q_one_canada).lower()
        clear_screen()
        if question_one == 'b':
            print('Traitor!, You will be deported to wherever your ancestors came from and you lose a point now!')
            points -= 1
            display_lives(points)
            if points == 0:
                print(lost)
                break
        elif question_one in ['c', 'd']:
            print('I thought you were brave. You lost a point')
            points -= 1
            display_lives(points)
            if points == 0:
                print(lost)
                break
        elif question_one == 'a':
            print('I knew you were a patriot, let us proceed to the next level!')
            completed_levels.append('a')  # Mark as completed after answering correctly
            if len(completed_levels) == 3:
                print("Congratulations! You have completed all levels!")
                break
            while True:
                print('Good Job! Press B for Hydrocity or Press C for Giza')
                level = input("Which level would you like to play? ").lower()
                if level in levels and level not in completed_levels:
                    break
                else:
                    print("Please choose a valid, incomplete level.")
            break

# Giza Level
if level == "c":
    clear_screen()
    print('Welcome to Giza! The land of one of the seven wonders of the world!')
    while True:
        question_three = input(q_three_giza).lower()
        clear_screen()
        if question_three in ['a', 'b', 'c']:
            print('Wrong, try again.')
            points -= 1
            display_lives(points)
            if points == 0:
                print(lost)
                break
        elif question_three == 'd':
            print("Ah ha, The damn pyramids! Wish they were lightweight, a perfect addition to the British Museum.\n"
                   "You may proceed to the next level now!")
            completed_levels.append('c')  # Mark as completed after answering correctly
            if len(completed_levels) == 3:
                print("Congratulations! You have completed all levels!")
                break
            while True:
                print('You are almost there! Press A for Canada or Press B for Hydrocity')
                level = input("Which level would you like to play? ").lower()
                if level in levels and level not in completed_levels:
                    break
                else:
                    print("Please choose a valid, incomplete level.")
            break

# Hydrocity Level
if level == 'b':
    clear_screen()
    print('Welcome to Hydrocity! The land of many rivers and oceans!')
    while True:
        question_two = input(q_two_hydrocity).lower()
        clear_screen()
        if question_two in ['a', 'b', 'd']:
            print('Wrong, try again.')
            points -= 1
            display_lives(points)
            if points == 0:
                print(lost)
                break
        elif question_two == 'c':
            print("Ah ha, clever one ain't it? You may proceed to the next level now!")
            completed_levels.append('b')  # Mark as completed after answering correctly
            if len(completed_levels) == 3:
                print("Congratulations! You have completed all levels!")
                break
            while True:
                print('You are almost there! Press A for Canada or Press C for Giza')
                level = input("Which level would you like to play? ").lower()
                if level in levels and level not in completed_levels:
                    break
                else:
                    print("Please choose a valid, incomplete level.")
            break

# Canada Level
if level == 'a':
    clear_screen()
    print('Welcome to Canada!')
    while True:
        question_one = input(q_one_canada).lower()
        clear_screen()
        if question_one == 'b':
            print('Traitor!, You will be deported to wherever your ancestors came from and you lose a point now!')
            points -= 1
            display_lives(points)
            if points == 0:
                print(lost)
                break
        elif question_one in ['c', 'd']:
            print('I thought you were brave. You lost a point')
            points -= 1
            display_lives(points)
            if points == 0:
                print(lost)
                break
        elif question_one == 'a':
            print('I knew you were a patriot, let us proceed to the next level!')
            completed_levels.append('a')  # Mark as completed after answering correctly
            if len(completed_levels) == 3:
                print("Congratulations! You have completed all levels!")
                break
            while True:
                print('Good Job! Press B for Hydrocity or Press C for Giza')
                level = input("Which level would you like to play? ").lower()
                if level in levels and level not in completed_levels:
                    break
                else:
                    print("Please choose a valid, incomplete level.")
            break