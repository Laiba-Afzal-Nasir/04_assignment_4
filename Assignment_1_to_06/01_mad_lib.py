def mad_libs():
    print("Welcome to Mad Libs!")

    adj1 = input("Enter an adjective: ")
    noun1 = input("Enter a noun: ")
    verb1 = input("Enter a verb: ")
    place = input("Enter a place: ")

    story = f"Once upon a time, a {adj1} {noun1} loved to {verb1} in a {place}."
    print("\nHere's your Mad Libs story:\n", story)

if __name__ =="__main__":
    mad_libs()