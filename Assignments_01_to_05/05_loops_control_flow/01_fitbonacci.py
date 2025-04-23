MAX_VALUE = 10000

def main():
    a = 0
    b = 1
    while a < MAX_VALUE:
        print(a, end=" ")  
        c = a + b
        a = b
        b = c 

if __name__ == '__main__':
    main()