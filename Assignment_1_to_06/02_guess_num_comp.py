# Guess thhe number game by computer
 
import random
def guess_the_number():
    number = random.randint(1,100)
    guesses_left = 7
    print("welcome to the Number Guessing Game.")
    print("I am thinking a number between 1 to 100")

    while guesses_left > 0:
        print(f'\nYou have {guesses_left} guesses left.')
        try:
            guess = int(input("Take a guess of number."))
        except ValueError:
            print("Invalid input: Please enter a number")
            continue

        if guess < number:
            print("Too low number. Try again!")
        elif guess > number:
            print("Too high number. Try again!")
        else:
            print(f"Congratultions! Correct Guess in {7 - guesses_left + 1} tries.")
            return
        
        guesses_left -= 1
    print(f"\nYou ran out of guess. The number was {number}.")

if __name__ == '__main__':
    guess_the_number()