import random

def main():
    random_numbers = [random.randint(1,100) for _ in range(10)]
    random_numbers.sort()
    print("Random numbers are: ", *random_numbers)

if __name__ == "__main__":
    main()