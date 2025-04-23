# Hangman Project
import random

word_list = ["python", "java", "javascript", "html", "css", "react", "tailwind", "nextjs"]

def choose_word():
    return random.choice(word_list)

def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def hangman():
    word = choose_word()
    guessed_letters = set()
    tries = 6  
    guessed_word = False

    print("Welcome to Hangman!")
    
    while tries > 0 and not guessed_word:
        print("\nWord:", display_word(word, guessed_letters))
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
        print(f"Tries left: {tries}")
        
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"Good guess! The letter {guess} is in the word.")
        else:
            tries -= 1
            print(f"Oops! The letter {guess} is not in the word.")
        
        if all(letter in guessed_letters for letter in word):
            guessed_word = True

    if guessed_word:
        print(f"\nCongratulations! You've guessed the word: {word}")
    else:
        print(f"\nGame Over! The word was: {word}")

if __name__ == "__main__":
    hangman()