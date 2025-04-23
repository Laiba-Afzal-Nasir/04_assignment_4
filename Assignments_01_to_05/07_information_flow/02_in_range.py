def in_range(n, low, high):
    return low <= n <= high

def main():
    n = int(input("Enter a number to check (n): "))
    low = int(input("Enter the lower bound: "))
    high = int(input("Enter the upper bound: "))
    
    if high <= low:
        print("⚠️ Upper bound must be greater than lower bound.")
        return

    if in_range(n, low, high):
        print(f"✅ Yes, {n} is within the range {low} to {high}!")
    else:
        print(f"❌ Nope, {n} is outside the range {low} to {high}.")

if __name__ == "__main__":
    main()