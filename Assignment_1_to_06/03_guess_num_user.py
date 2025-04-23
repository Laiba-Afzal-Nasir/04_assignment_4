# Guess the number game (user)
import random 
def main():
    target = random.randint(1,100)
    while True :
        user_choice = input("Guess my number or Quit: ")
        if user_choice == "":
            break

        user_choice = int(user_choice)
        if user_choice == target:
            print(f"Congrats! The number was: {target}")
            break
        elif user_choice < target:
            print("Your guess is too low. Guess again!")
        else:
            print("Your guess is too high. Guess again!")

    print("-----GAME OVER-----")


if __name__ == '__main__':
    main()