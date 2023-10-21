import random
def roll_custom_dice(sides):
    return random.randint(1, sides)

# Ask the user for the maximum number on the dice
max_number = int(input("Enter the maximum number on the dice: "))

while True:
    result = roll_custom_dice(max_number)
    print(f"Rolled: {result}")
    if result == max_number:
        print(f"You rolled the maximum number, {max_number}! Exiting.")
        break
