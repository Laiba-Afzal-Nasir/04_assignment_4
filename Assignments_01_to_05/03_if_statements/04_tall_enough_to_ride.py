MIN_HEIGHT = 50 

def main():
    while True:
        height_input = input("How tall are you? ")

        if height_input == "":
            print("Goodbye!")
            break

        height = int(height_input)
        
        if height >= MIN_HEIGHT:
            print("You're tall enough to ride!")
        else:
            print("You're not tall enough to ride, but maybe next year!")

if __name__ == "__main__":
    main()
