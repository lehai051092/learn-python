from random import randint

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

chooses = [rock, paper, scissors]
your_chose_int = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if 0 <= your_chose_int <= 2:
    rock = chooses[0]
    paper = chooses[1]
    scissors = chooses[2]
    computer_chose_int = randint(0, len(chooses) - 1)
    your_chose = chooses[your_chose_int]
    computer_chose = chooses[computer_chose_int]

    print(f"Your chose:\n{your_chose}")
    print(f"Computer chose:\n{computer_chose}")

    if your_chose == computer_chose:
        print("It's a draw!")
    elif your_chose == rock:
        if computer_chose == paper:
            print("You lose!")
        else:
            print("You win!")
    elif your_chose == paper:
        if computer_chose == scissors:
            print("You lose!")
        else:
            print("You win!")
    else:
        if computer_chose == rock:
            print("You lose!")
        else:
            print("You win!")
else:
    print("You typed an invalid number. You lose!")
