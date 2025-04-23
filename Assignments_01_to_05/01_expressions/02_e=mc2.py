C = 299792458 #m/s

def main():
    m = int(input("\nEnter kilos of mass.. "))
    energy = m * C**2
    print("e = m * C^2")
    print(f"m = {m} kg")
    print(f"C = {C} m/s")
    print(f"\n{energy} joules of energy!\n")
    return energy
    

if __name__ == "__main__":
    main()