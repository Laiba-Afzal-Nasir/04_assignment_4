def get_first_element(lst):
    print("First element in the list is:", lst[0])

def main():
    n = int(input("How many elements do you want to enter? "))
    user_list = []

    for i in range(n):
        element = input(f"Enter element {i + 1}: ")
        user_list.append(element)
        
    get_first_element(user_list)

if __name__ == '__main__':
    main()