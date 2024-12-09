import pandas

nato_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
dictionary_nato_alphabet = {item.letter:item.code for index, item in nato_alphabet.iterrows()}


def generate_phonetic():
    text = input("input your text: ").upper()

    try:
        result = [dictionary_nato_alphabet[char] for char in list(text)]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(f"result {result}")

generate_phonetic()