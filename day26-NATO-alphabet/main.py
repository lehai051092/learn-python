import pandas

nato_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
dictionary_nato_alphabet = {item.letter:item.code for index, item in nato_alphabet.iterrows()}

text = input("input your text: ").upper()
result = [dictionary_nato_alphabet[char] for char in list(text)]

print(f"result {result}")
