import math 

def main():
    ab = float(input('\nEnter the length of the side AB: '))
    ac = float(input('\nEnter the length of the side BC: '))
    bc = math.sqrt(ab**2 + ac**2)

    print(f"\nThe length of BC (the hypoteneus) is {bc:.2f}\n")

if __name__ == "__main__":
    main()