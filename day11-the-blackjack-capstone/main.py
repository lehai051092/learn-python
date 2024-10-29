from art import logo
import random


def create_deck():
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    deck = [{'value': value, 'suit': suit} for value in values for suit in suits]
    random.shuffle(deck)
    return deck


def calculate_score(cards):
    score = 0
    aces = 0

    for card in cards:
        if card['value'] in ['J', 'Q', 'K']:
            score += 10
        elif card['value'] == 'A':
            aces += 1
            score += 11
        else:
            score += int(card['value'])

    while score > 21 and aces:
        score -= 10
        aces -= 1

    return score


def determine_winner(player_score, dealer_score):
    if player_score > 21:
        return "You went over. You lose 😤"
    elif dealer_score > 21:
        return "Opponent went over. You win 😁"
    elif player_score == dealer_score:
        return "Draw 😤"
    elif player_score == 21:
        return "Blackjack! You win 😁"
    elif dealer_score == 21:
        return "Dealer has Blackjack. You lose 😤"
    elif player_score > dealer_score:
        return "You win 😁"
    else:
        return "You lose 😤"


def start_game():
    print(logo)
    deck = create_deck()
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]
    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)

    is_complete = False

    while not is_complete:
        player_score = calculate_score(player_hand)
        dealer_score = calculate_score(dealer_hand)

        print(f"Your cards: {player_hand}, current score: {player_score}")
        print(f"Computer's first card: {dealer_hand[0]}")

        if player_score == 21 or dealer_score == 21 or player_score > 21 or dealer_score > 21:
            is_complete = True
        else:
            is_another_card = input("Type 'y' to get another card, type 'n' to pass:")
            if is_another_card.lower() in ['y', 'n']:
                if is_another_card.lower() == 'y':
                    player_hand.append(deck.pop())
                else:
                    is_complete = True
            else:
                print("invalid input")
                is_complete = True

    while dealer_score != 0 and dealer_score < 17:
        card = random.choice(deck)
        if card not in player_hand:
            dealer_hand.append(card)
            dealer_score = calculate_score(dealer_hand)

    print(f"Your final hand: {player_hand}, final score: {player_score}")
    print(f"Computer's final hand: {dealer_hand}, final score: {dealer_score}")
    print(determine_winner(player_score, dealer_score))


is_playing = True

while is_playing:
    is_play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if is_play_game == 'y':
        start_game()
        print("\n" * 20)
    elif is_play_game == 'n':
        is_playing = False
    else:
        print("Invalid input. Please type 'y' or 'n'.")