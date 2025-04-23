STARTING_SENTENCE = "\nCode in place is fun. I Learned to program and used Python to make my "
def main():
    adjective = input("Please type an adjective and press enter ")
    noun = input("Please type a noun and press enter ")
    verb = input("Please type a verb and press enter ")

    ending_sentence = f"{adjective} {noun} {verb}.\n"
    sentence = STARTING_SENTENCE + ending_sentence
    print(sentence)

if __name__ == "__main__":
    main()