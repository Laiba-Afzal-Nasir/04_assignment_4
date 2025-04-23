def double(num:int):
    return num * 2

def main():
    get_num = int(input("Enter a number: "))
    double_num = double(get_num)
    print(f"Double that is {double_num}")


if __name__ == '__main__':
    main()