#THIS IS AN IMPROVEMENT TO jargon_jumble.py

#MODULES
import random

#CREATING A TABLE OF WORDS
print("Player 1")
theme = input("Enter a theme: ")
words = []
print()

for x in range (0, 3):
    words.append(input(f"Enter the {i + 1} word related to the theme you chose: ").strip(" "))

#CHOOSING A WORD AND SCRAMBLING IT
word = random.choice(words)
letters = list(word)
random.shuffle(letters)
scrambled_word = "".join(letters)
print()
print("Player 2")
print(f"Scrambled word: {scrambled_word}")

#GUESSING THE WORD
guess = input(f"The theme is {theme}. Descramble the word (You have 5 tries): ")
guesses = 1

while guess != word and guesses != 5:
    guess = input("Wrong, guess again: ")
    guesses += 1

if guess == word:
    print(f"Well done! You took {guesses} guesses.")
elif guesses == 5 and guess != word:
    print(f"Failed, the word was {word}")
