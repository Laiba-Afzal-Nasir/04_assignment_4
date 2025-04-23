
def main():
    side_1 : float = float(input("What is the length of side 1: "))
    side_2 : float = float(input("What is the length of side 2: "))
    side_3 : float = float(input("What is the length of side 3: "))

    print("The perimeter of the triangle is : " + str(side_1 + side_2 + side_3))
# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()