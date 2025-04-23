def add_three_copies(some_list, data):
    some_list.append(data)
    some_list.append(data)
    some_list.append(data)


def main():
    message = input("\nEnter a message to copy: ")  
    my_list = []  
    print("\nList before:", my_list) 
    add_three_copies(my_list, message) 
    print("\nList after:", my_list)  

if __name__ == '__main__':
    main()