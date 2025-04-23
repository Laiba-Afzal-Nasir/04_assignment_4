# Rock Paper Scissors Game
import random 

choices = ['rock','paper','scissors']

player_choice = input("\nEnter Rock, Paper and Scissors: ").lower()

computer_choice = random.choice(choices)

if player_choice == computer_choice:
    print(f"\nIt's a tie.")
elif player_choice == 'rock' and computer_choice == 'scissors':
    print(f"\nPlayer wins! {player_choice} beats {computer_choice}")
elif player_choice == 'paper' and computer_choice == 'rock':
    print(f"\nPlayer wins! {player_choice} beats {computer_choice}")
elif player_choice == 'scissors' and computer_choice == 'paper':
    print(f"\nPlayer wins! {player_choice} beats {computer_choice}")
else:
    print(f"\nComputer wins! {computer_choice} beats {player_choice}")

print("\n-----GAME OVER-----\n")