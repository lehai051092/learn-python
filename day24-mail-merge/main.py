# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


def get_starting_letter():
    with open("Input/Letters/starting_letter.txt") as f:
        starting_letter = f.readlines()

    return starting_letter


def get_names():
    with open("Input/Names/invited_names.txt") as f:
        names = f.readlines()

    return names


def ready_to_send(name, letter):
    with open(f"Output/ReadyToSend/letter_for_{name}.txt", "w") as f:
        f.writelines(letter)


for name in get_names():
    letter = get_starting_letter()
    name = name.strip()
    letter[0] = letter[0].replace("[name]", name)
    ready_to_send(name, letter)
