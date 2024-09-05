import random

def print_game_status(mistakes, guesses, remaining_guesses):
    if mistakes == 0:
        print("  |------|-")
        print("  |      | ")
        print("  |          ")
        print("  |          ")
        print("  |          ")
        print("  |          ")
        print("  /|\\       ")
        print(" / | \\      ")
    elif mistakes == 1:
        print("  |------|-")
        print("  |      | ")
        print("  |      o ")
        print("  |          ")
        print("  |          ")
        print("  |          ")
        print("  /|\\       ")
        print(" / | \\      ")
    elif mistakes == 2:
        print("  |------|-")
        print("  |      | ")
        print("  |      o ")
        print("  |      | ")
        print("  |      | ")
        print("  |          ")
        print("  /|\\       ")
        print(" / | \\      ")
    elif mistakes == 3:
        print("  |------|-")
        print("  |      | ")
        print("  |      o ")
        print("  |     /| ")
        print("  |      | ")
        print("  |          ")
        print("  /|\\       ")
        print(" / | \\      ")
    elif mistakes == 4:
        print("  |------|-")
        print("  |      | ")
        print("  |      o ")
        print("  |     /|\\")
        print("  |      | ")
        print("  |          ")
        print("  /|\\       ")
        print(" / | \\      ")
    elif mistakes == 5:
        print("  |------|-")
        print("  |      | ")
        print("  |      o ")
        print("  |     /|\\")
        print("  |      | ")
        print("  |     /  ")
        print("  /|\\       ")
        print(" / | \\      ")
    elif mistakes == 6:
        print("  |------|-")
        print("  |      | ")
        print("  |      o ")
        print("  |     /|\\")
        print("  |      | ")
        print("  |     / \\")
        print("  /|\\  |   ")
        print(" / | \\  |  ")

    print("Word: ", end='')
    for element in guesses:
        print(f"{element}", end='')
    print(f"\nYou have {remaining_guesses} guess(es) left")

words = ["elbow", "writer", "circle", "polish", "bridge", "store", "fang", "scarecrow", "show", "jeans", "attempts", "waxing", "aftermath", "banana", "wrist", "wheel", "spring", "cheer"]
guesses = []
remaining_guesses = 6
mistakes = 0
word = random.choice(words).upper()

for i in range(len(word)):
    guesses.append("_")

game_over = False

while not game_over:
    print_game_status(mistakes, guesses, remaining_guesses)
    user_input = input("Please enter a letter\n")

    if len(user_input) != 1:
        print("That's not a valid input. Please try again")
        continue

    letter = user_input[0].upper()

    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                guesses[i] = letter

        if all(guess != '_' for guess in guesses):
            game_over = True
    else:
        print("Sorry, that's not part of the word")
        remaining_guesses -= 1
        mistakes += 1

        if mistakes == 6:
            game_over = True

if mistakes == 6:
    print_game_status(mistakes, guesses, remaining_guesses)
    print(f"Sorry, you lost. The word was {word}")
else:
    for i in range(4):
        print("\U0001F389 \U0001F388", end="")
    print()
    print("Congratulations, you won!")
    print(f"The word was {word}")