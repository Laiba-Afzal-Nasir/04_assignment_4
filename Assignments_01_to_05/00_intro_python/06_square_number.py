def main():
    get_number : float = float(input("Type a number to see its square: "))
    sqr_number : float = get_number * get_number
    print(f"{get_number} squared is {sqr_number}")

if __name__ == '__main__':
    main()