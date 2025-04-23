def add_many_numbers(numbers:list[int]):
    total_number = 0
    for number in numbers:
        total_number += number
    return total_number
        
def main():
    num : list = [2,4,6,8,10]
    sum = add_many_numbers(num)
    print(sum)

if __name__ == '__main__':
    main()