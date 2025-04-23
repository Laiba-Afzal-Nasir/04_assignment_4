def main():
    numbers: list[int] = [1, 2, 3, 4, 5]  
    for i in range(len(numbers)): 
        index_number = numbers[i]  
        numbers[i] = index_number * 2 
    print("Numbers:",numbers)  

if __name__ == '__main__':
    main()