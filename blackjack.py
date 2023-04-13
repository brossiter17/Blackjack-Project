import random
import db as money

def get_deck():
    deck_of_cards = []
    suits = ['\u2660', '\u2661','\u2662','\u2663']
    ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    values = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    for suit in suits:
        for i, rank in enumerate(ranks):
            card = [rank, suit, values[i]]
            deck_of_cards.append(card)
    print(deck_of_cards)
    random.shuffle(deck_of_cards)
    #print(deck_of_cards)

    return deck_of_cards

def get_bet(player_money):
    print()
    print(f"Money: {player_money}")
    while True:
        try:
            bet_amount = float(input("Bet amount: "))
            if bet_amount < 5 or bet_amount > 1000:
                print("Invalid bet amount. Please enter a bet between $5 and $1000.")
            elif bet_amount > player_money:
                print(f"You don't have enough money.  You have ${player_money}.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")
    player_money -= bet_amount
    return bet_amount


def play_blackjack(player_money):
    calculate_hand = 0
    deck_of_cards = get_deck()
    bet_amount = get_bet(player_money)

    print(f"This is a test of the bet amount: {bet_amount}")
    print(f"This is the deck in the play BJ thing ==> {deck_of_cards}")

    dealer_hand = [deck_of_cards.pop(0), deck_of_cards.pop(0)]
    player_hand = [deck_of_cards.pop(0), deck_of_cards.pop(0)]

    print("\nDEALER's SHOW CARD")
    #for index in dealer_hand:
    #    print(index[i], index[0])

    for i in range(len(dealer_hand)):
        print(f"{dealer_hand[i][0]} {dealer_hand[i][1]}")



    print("\nYOUR CARDS")
    #print(player_hand)
    #print(f"Player hand:  {player_hand}")


    for card in player_hand:
        print(card[0], card[i])

    #for i in range(len(player_hand)):
    #    print(f"{player_hand[i][0]} {player_hand[i][1]}")


    while True:
        try:
            player_choice = input("\nDo you want to hit or stand? ")
            if player_choice.lower() == 'hit':
                player_hand.append(deck_of_cards.pop())
                print("Your hand: ", player_hand)
            if calculate_hand(player_hand) > 21:
                print("You bust! Dealer wins!")
                player_money -= bet_amount
            elif player_choice.lower() == 'stand':
                break
            else:
                print("Invalid input. Please enter hit or stand.")
        except ValueError:
            print("Invalid amount.  Please enter a number")



























def main():
    print()
    print("BLACKJACK!")
    print("Blackjack payout is 3:2")


    player_money = money.read_money()
    play_blackjack(player_money)




    #print()
    #print(f"This is a test of Player Money ++> {player_money}")








if __name__ == '__main__':
    main()
