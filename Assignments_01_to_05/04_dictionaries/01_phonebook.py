def main():
    phonebook = {}

    while True:
        print("\nPhonebook Menu:")
        print("1. Add a contact")
        print("2. Lookup a contact")
        print("3. Delete a contact")
        print("4. Show all contacts")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            name = input("Enter name: ")
            number = input("Enter phone number: ")
            phonebook[name] = number
            print(f"Contact added: {name} - {number}")
        
        elif choice == '2':
            name = input("Enter name to lookup: ")
            if name in phonebook:
                print(f"{name}'s phone number is {phonebook[name]}")
            else:
                print(f"Contact not found for {name}.")
        
        elif choice == '3':
            name = input("Enter name to delete: ")
            if name in phonebook:
                del phonebook[name]
                print(f"Contact {name} deleted.")
            else:
                print(f"Contact not found for {name}.")
        
        elif choice == '4':
            if phonebook:
                print("\nAll Contacts:")
                for name, number in phonebook.items():
                    print(f"{name}: {number}")
            else:
                print("No contacts in the phonebook.")
        
        elif choice == '5':
            print("Exiting phonebook program.")
            break
        
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()