inches : int = 12

def main():
    feet = int(input("\nEnter the number of feet: "))
    conversion : float = feet * inches
    print(f"\n{feet} feet is {conversion} inches..\n")


if __name__ == "__main__":
    main()