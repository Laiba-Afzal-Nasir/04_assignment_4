import random

SIDES = 6

def dice_roll():
    die1 = random.randint(1,SIDES)
    die2 = random.randint(1,SIDES)

    total = die1 + die2

    print(f'Die 1: {die1}, Die 2: {die2}, Total: {total}')

def main():
    die1 = 10
    print(f'die1 as main() in {die1}')
    for _ in range(3):
        dice_roll()
        print(f'die1 as main() in end is {die1}')

if __name__ == "__main__":
    main()