# Datheon Task 3 - Portfolio Generator# Datheon Task 4 - Hangman Game
import random

words = ["python", "datheon", "internship", "github", "capstone"]
word = random.choice(words)
guessed = ["_"] * len(word)
attempts = 6
used_letters = []

print("Welcome to Hangman! - Datheon Task")
print("Word: ", " ".join(guessed))

while attempts > 0 and "_" in guessed:
    guess = input("Guess a letter: ").lower()
    
    if guess in used_letters:
        print("You already tried that letter!")
        continue
    
    used_letters.append(guess)
    
    if guess in word:
        for i, letter in enumerate(word):
            if letter == guess:
                guessed[i] = guess
        print("Correct! ->", " ".join(guessed))
    else:
        attempts -= 1
        print(f"Wrong! {attempts} chances left -> {' '.join(guessed)}")

if "_" not in guessed:
    print(f"\nYou Won! The word was: {word}")
else:
    print(f"\nYou Lost! The word was: {word}")
