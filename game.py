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