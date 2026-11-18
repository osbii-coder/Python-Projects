#THIS IS AN IMPROVEMENT TO jargon_jumble.py

#MODULES
import random

#CREATING A TABLE OF WORDS
words = []
print("Player 1")
words.append(input("Enter a fruit: ").strip(" "))
words.append(input("Enter another fruit: ").strip(" "))
words.append(input("Enter another fruit: ").strip(" "))

#CHOOSING A WORD AND SCRAMBLING IT
word = random.choice(words)
letters = list(word)
random.shuffle(letters)
scrambled_word = "".join(letters)
print(scrambled_word)

#GUESSING THE WORD
print()
print("Player 2")
guess = input("The theme is fruits. Descramble the word (You have 5 tries): ")
guesses = 1

while guess != word and guesses!= 5:
    guess = input("Wrong, guess again: ")
    guesses += 1
   
if guesses == 6:
    print(f"Failed, the word was {word}")
else:
    print(f"Well done you took {guesses} guesses")
