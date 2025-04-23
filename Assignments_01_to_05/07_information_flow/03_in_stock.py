def num_in_stock(fruit):
    inventory = {
        "apple": 10,
        "banana": 5,
        "pear": 15,
        "mango": 12
    }
    return inventory.get(fruit, 0)

def main():
    fruit = input("\nEnter a fruit: ")
    count = num_in_stock(fruit)

    if count > 0:
        print("This fruit is in stock! Here is how many:")
        print(count,"\n")
    else:
        print("This fruit is not in stock.\n")

if __name__ == "__main__":
    main()