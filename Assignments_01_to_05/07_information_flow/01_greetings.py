def greet(name:str):
    return name

def main():
    user_input = input("\nWhat's your name? ")
    result = greet(user_input)
    print(f"Greetings {result}!\n")

if __name__ == "__main__":
    main()