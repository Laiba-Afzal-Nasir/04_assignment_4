import random

SIDES = 6

def main():
    die1 = random.randint(1,SIDES)
    die2 = random.randint(1,SIDES)

    total = die1 + die2

    print(f"\nDie 1: {die1}")
    print(f"Die 2: {die2}")
    print(f"The total of ({die1}) and ({die2}) is: {total}\n")

if __name__ == "__main__":
    main()