import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        user_input = int(input("\nEnter the length of your desired password: "))
        if user_input > 0:
            password = generate_password(user_input)
            print(f"My password is: [ {password} ]\n")
        else:
            print("Password length must be greater than 0.\n")
    except ValueError:
        print("Please enter a valid number.\n")

if __name__ == '__main__':
    main()