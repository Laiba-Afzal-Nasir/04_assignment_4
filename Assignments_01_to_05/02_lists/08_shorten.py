MAX_LENGTH = 5

def shorten(list):
    while len(list) > MAX_LENGTH:
        removed_item = list.pop()
        print("Removed Item:", removed_item)

def main():
    list = input("Enter a list of values separated by space: ").split()    
    shorten(list)
    print("Final list:", list)

if __name__ == "__main__":
    main()