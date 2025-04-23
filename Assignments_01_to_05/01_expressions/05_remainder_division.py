def main():
    dividend = int(input("\nPlease enter an integer to be divided: "))
    divisor  = int(input("\nPlease enter an integer to divide by: "))

    division = dividend // divisor
    remainder = dividend % divisor

    print(f"\nThe result of this division is {division} with a remainder of {remainder}")

if __name__ == "__main__":
    main()