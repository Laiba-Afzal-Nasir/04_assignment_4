def main():
    print("How old they are ?")

    anton : int = 21
    beth : int = 6 + anton
    chen : int = 20 + beth
    drew : int = chen + anton
    ethan : int = chen

    print(f"Anthon is {anton}")
    print(f"Beth is {beth}")
    print(f"Chen is {chen}")
    print(f"Drew is {drew}")
    print(f"Ethan is {ethan}")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()