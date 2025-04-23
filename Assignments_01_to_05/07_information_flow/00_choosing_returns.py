ADULT_AGE = 18 

def is_adult(age):
    return age >= ADULT_AGE

def main():
    age = int(input("\nHow old is this person?: "))
    
    if is_adult(age):
        print("(Entered age is an adult age)")
    else:
        print("(Entered age is not an adult age)")
    
    print(is_adult(age))  

if __name__ == "__main__":
    main()