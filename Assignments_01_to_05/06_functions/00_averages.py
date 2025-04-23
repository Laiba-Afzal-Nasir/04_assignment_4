def avg(a:float,b:float):
    sum = a + b 
    avg = sum / 2
    return avg

def main():
    avg_1 = avg(5, 10)
    avg_2 = avg(8, 10)
    
    final = avg(avg_1, avg_2)
    print(f"The average between the two numbers is {final}")


if __name__ == '__main__':
    main()