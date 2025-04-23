def get_one_digit(number:int):
    print("The one digit is:", number % 10)

def main():
    num = int(input("Enter a number: "))
    get_one_digit(num)


if __name__ == '__main__':
    main()