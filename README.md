# Project.PythonGame
import random

def snake_ladder():
    position = 1
    snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
    ladders = {2: 38, 7: 14, 8: 31, 15: 26, 28: 84, 36: 44, 51: 67, 71: 91, 78: 98, 87: 94}

    print("Welcome to Snakes and Ladders! Reach 100 to win.")

    while position < 100:
        input("Press Enter to roll the dice: ")
        roll = random.randint(1, 6)
        position += roll
        print(f"You rolled {roll}. Moving to {position}.")

        if position in snakes:
            print("Oh no! A snake bit you!")
            position = snakes[position]
        elif position in ladders:
            print("Great! You found a ladder!")
            position = ladders[position]

        print(f"Current Position: {position}\n")
    
    print("Congratulations! You reached 100 and won!")

snake_ladder()
