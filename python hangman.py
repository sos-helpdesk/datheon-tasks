
import random

words = ["python", "cloud", "apple", "laptop", "coding"]
word = random.choice(words).upper()

guessed = set()
wrong = 0
max_attempts = 6

stages = [
    """
     +---+
         |
         |
         |
        ===
    """,
    """
     +---+
     O   |
         |
         |
        ===
    """,
    """
     +---+
     O   |
     |   |
         |
        ===
    """,
    """
     +---+
     O   |
    /|   |
         |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
         |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
    /    |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
    / \\  |
        ===
    """
]

print("===== HANGMAN GAME =====")

while wrong < max_attempts:
    print(stages[wrong])

    display = " ".join(
        letter if letter in guessed else "_"
        for letter in word
    )

    print("Word:", display)
    print("Guessed letters:", sorted(guessed))
    print("Attempts left:", max_attempts - wrong)

    if all(letter in guessed for letter in word):
        break

    guess = input("Guess a letter: ").strip().upper()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter one letter only!")
        continue

    if guess in guessed:
        print("You already guessed that letter!")
        continue

    guessed.add(guess)

    if guess in word:
        print("Correct guess!")
    else:
        wrong += 1
        print("Wrong guess!")

if all(letter in guessed for letter in word):
    print("\nYOU WIN!")
    print("The word was:", word)
else:
    print(stages[wrong])
    print("\nGAME OVER!")
    print("The word was:", word)
