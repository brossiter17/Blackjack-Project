import random


def get_deck():
    deck_of_cards = []
    suits = ['\u2660', '\u2661','\u2662','\u2663']
    ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    values = {'Ace': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10}

    for suit in suits:
        for rank in ranks:
            card = [rank, suit, values[rank]]
            deck_of_cards.append(card)


    print(deck_of_cards)

    random.shuffle(deck_of_cards)
    print(deck_of_cards)

    return deck_of_cards


def main():
    print()
    print("BLACKJACK!")
    print("Blackjack payout is 3:2")


    get_deck()








if __name__ == '__main__':
    main()
