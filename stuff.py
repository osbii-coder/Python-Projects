#MODULES
import random
import time

#CREATING A TABLE OF WORDS
words = ["apple", "pear", "orange"]
print("Player 1")
# words.append(input("Enter a fruit: ").strip(" "))
# words.append(input("Enter another fruit: ").strip(" "))
# words.append(input("Enter another fruit: ").strip(" "))

#CHOOSING A WORD AND SCRAMBLING IT
word = random.choice(words)
letters = list(word)
random.shuffle(letters)
scrambled_word = "".join(letters)
print(scrambled_word)

print("Player 2")
guess = input("Descramble the word (You have 5 tries): ")
guesses = 1

while guess != word and guesses!= 5:
    guess = int(input("wrong, guess again"))
    guesses = guesses + 1
   
if guesses == 3:
    print("Failed")
else:
    print(f"Well done you took {guesses} guesses")