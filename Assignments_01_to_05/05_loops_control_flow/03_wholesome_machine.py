AFFIRMATION = "I am capable of doing anything I put my mind to"
  
def main():
    
    while True:
        user_input = input(f"\nPlease type the following affirmation:\n {AFFIRMATION}")
        if user_input == AFFIRMATION :
            print("\nThat's right! :)")
            break  
        else:
            print("\nHmmm.. That was not the affirmation. Please try again.")
            break

if __name__ == "__main__":
    main()