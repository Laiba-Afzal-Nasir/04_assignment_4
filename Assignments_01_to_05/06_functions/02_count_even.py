def main(lst):
    while True:
        user_input = input("Enter an integer or press enter to stop: ")
        if user_input == "":
            break  
        try:
            lst.append(int(user_input))  
        except ValueError:
            print("Please enter a valid integer.")  

    even_count = 0
    for num in lst:
        if num % 2 == 0:
            even_count += 1

    print(f"Number of even numbers are: {even_count}")

if __name__ == '__main__':
    main([])