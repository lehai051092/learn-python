# logo
# Compare A: name, a job, from ...
# logovs
# Against B: name, a job, from ...
# Who has more followers: Type 'A' or 'B':
#
# if wrong: Sorry, that's wrong. Final score: 0
# if true: You're right! Current score: 1.
# if input invalid: Sorry, that's wrong. Final score: 1
import random

from art import logo, vs
from game_data import data


def handle_compare_choice(answered_list, question_list):
    return random.choice(question_list)


def handle_against_choice(compare_choice, question_list, answered_list):
    against_choice = random.choice(question_list)
    if compare_choice == against_choice:
        against_choice = random.choice(question_list)
    elif len(answered_list) > 0:
        against_choice = answered_list[-1]

    return against_choice


def handle_display(score, compare_choice, against_choice):
    print(logo)
    if score > 0:
        print(f"You're right! Current score: {score}.")
    print(
        f"Compare A: {compare_choice['name']}, a {compare_choice['description']}, from {compare_choice['country']}")
    print(vs)
    print(
        f"Against B: {against_choice['name']}, a {against_choice['description']}, from {against_choice['country']}")


def start_game():
    is_completed = False
    score = 0
    answered_list = []
    question_list = data.copy()

    while not is_completed:
        try:
            compare_choice = handle_compare_choice(answered_list, question_list)
            against_choice = handle_against_choice(compare_choice, question_list, answered_list)

            handle_display(score, compare_choice, against_choice)

            answer = input("Who has more followers: Type 'A' or 'B':").lower()
            compare_follower_count = compare_choice["follower_count"]
            against_follower_count = against_choice["follower_count"]

            if answer == "a" and compare_follower_count > against_follower_count:
                score += 1
                answered_list.append(compare_choice)
                question_list.pop(question_list.index(compare_choice))
            elif answer == "b" and compare_follower_count < against_follower_count:
                score += 1
                answered_list.append(against_choice)
                question_list.pop(question_list.index(against_choice))
            else:
                print(f"Sorry, that's wrong. Final score: {score}")
                is_completed = True

        except:
            print(f"Sorry, that's wrong. Final score: {score}")
            is_completed = True


start_game()
