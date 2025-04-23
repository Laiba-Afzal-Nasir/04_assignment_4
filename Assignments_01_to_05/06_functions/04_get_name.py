def get_name(name:str):
    return name 

def main():
    user_name = input("\nEnter your name: ")
    get_name(user_name)
    print(f"Howdy {user_name}!😎")

if __name__ == '__main__':
    main()