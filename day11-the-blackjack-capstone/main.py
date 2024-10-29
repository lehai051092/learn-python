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

    for card in cards:
        if card['value'] in ['J', 'Q', 'K']:
            score += 10
        elif card['value'] == 'A':
            if score >= 11:
                score += 1
            else:
                score += 11
        else:
            score += int(card['value'])

    return score


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

        print(f"Player cards: {player_hand}, current score: {player_score}")
        print(f"Dealer cards: {dealer_hand[0]}, Hidden")

        if player_score == 21 or dealer_score == 21 or player_score > 21 or dealer_score > 21:
            is_complete = True
            break

        is_another_card = input("Type 'y' to get another card, type 'n' to pass:")
        if is_another_card.lower() in ['y', 'n']:
            if is_another_card.lower() == 'y':
                player_hand.append(deck.pop())
            else:
                for card in range(random.randint(1, len(player_hand) - 1)):
                    dealer_hand.append(deck.pop())

                is_complete = True
        else:
            print("invalid input")
            is_complete = True
            break

    if is_complete:
        print(f"Player cards: {player_hand}, current score: {player_score}")
        print(f"Dealer cards: {dealer_hand}, current score: {dealer_score}")

        if player_score == 21 and dealer_score < 21:
            print("Opponent went over. You win 😁")
        elif dealer_score == 21 and player_score < 21:
            print("You lose 😤")
        elif player_score > 21 >= dealer_score:
            print("You lose 😤")
        elif dealer_score > 21 >= player_score:
            print("Opponent went over. You win 😁")
        elif player_score > dealer_score:
            print("Opponent went over. You win 😁")
        elif dealer_score > player_score:
            print("You lose 😤")
        else:
            print("Draw 😤")


is_playing = True

while is_playing:
    is_play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n':")
    if is_play_game.lower() == 'y':
        start_game()
    else:
        is_playing = False
