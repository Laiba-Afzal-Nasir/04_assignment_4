# this function adds two numbers

def sum():
    first_num = input("Enter first number")
    first_num:int = int(first_num)
    second_num = input("Enter first number")
    second_num:int = int(second_num)
    sum : int = first_num + second_num
    print(f"The sum of two number is {sum}")

if __name__ == '__main__':
    sum()