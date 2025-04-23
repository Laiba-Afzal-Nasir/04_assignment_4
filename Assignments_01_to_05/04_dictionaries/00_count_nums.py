def main():
    counts = {}
    while True:
        num = input("Enter a number: ")
        if num == "":
            break

        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    for num in counts:
        print(f"{num} appears {counts[num]} times.")

if __name__ == "__main__":
    main()