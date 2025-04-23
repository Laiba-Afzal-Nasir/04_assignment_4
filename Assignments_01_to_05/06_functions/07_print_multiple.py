def make_multiple(message:str, repeat:int):
    for i in range(repeat):
        print(message)

def main():
    message = input("Enter a mesage: ")
    repeat = int(input("Enter a number: "))
    make_multiple(message, repeat)

if __name__ == '__main__':
    main()