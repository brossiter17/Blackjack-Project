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
    random.shuffle(deck_of_cards)
    return deck_of_cards

def get_bet(player_money):
    print()
    print(f"Money: {player_money}")

    if player_money < 5:
        buy_chips = input("Minimum bet is $5.  Would you like to buy more chips (y/n): ")
        if buy_chips == "y":
            buy_chips(player_money)
        else:
            pass




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
            print("Invalid bet. Please enter another bet.")
    player_money -= bet_amount
    return bet_amount


def buy_chips(player_money):
    while True:
        try:
            amount_of_chips = float(input("How many chips would you like to buy: "))
            if amount_of_chips < 5:
                print("Minimum purchase is $5.")
            else:
                player_money += amount_of_chips
                money.write_money(money)
                print(f"Money: {player_money}")
                return player_money
        except ValueError:
            print("Invalid option. Please enter a number.")


def get_hand_value(card_hand):
    card_total = 0
    number_of_aces = 0
    for card in card_hand:
        card_total += card[2]
        if card[0] == 'Ace':
            number_of_aces += 1
    while card_total > 21 and number_of_aces > 0:
        card_total -= 10
        number_of_aces -= 1
    return card_total


def player_turn(deck_of_cards, player_hand, player_money, bet_amount):
    i = 1
    while True:
        player_choice = input("\nHit or stand? (hit/stand): ")
        if player_choice.lower() == 'hit':
            player_hand.append(deck_of_cards.pop(0))
            print("\nYOUR CARDS")
            for card in player_hand:
                print(card[0], card[i])

            player_hand_total = get_hand_value(player_hand)
            #while player_hand_total > 21:
            if player_hand_total > 21:
                print("Sorry.  You lose.")
                player_money = player_money - bet_amount
                money.write_money(player_money)
                break
            #break
        elif player_choice.lower() == "stand":
            break
    return player_money


def dealer_turn(deck_of_cards, player_hand_total, dealer_hand, dealer_hand_total, player_money, bet_amount, player_hand):
    i = 1

    player_hand_total = get_hand_value(player_hand)
    if player_hand_total <= 21:
        print("\nDEALER'S CARDS:")
        for card in dealer_hand:
            print(card[0], card[i])

    while dealer_hand_total <= 17:
        dealer_hand.append(deck_of_cards.pop(0))
        dealer_hand_total = get_hand_value(dealer_hand)

        for card in dealer_hand:
            print(card[0], card[i])



    if dealer_hand_total > 21:
        print("\nCongratulations.  You win!")
        player_money += bet_amount
        for card in dealer_hand:
            print(card[0], card[i])
    elif dealer_hand_total > player_hand_total and dealer_hand_total <= 21:
        print("\nSorry.  You lose.")
        player_money -= bet_amount
    elif player_hand_total > dealer_hand_total and player_hand_total <= 21:
        print("\nCongratulations.  You win!")
        player_money += bet_amount
    elif player_hand_total == dealer_hand_total:
        print("\nIT'S A TIE!")
        player_money += bet_amount

    money.write_money(player_money)

    print(f"\nYOUR POINTS: {player_hand_total:>8}")
    print(f"DEALER'S POINTS: {dealer_hand_total:>5}")


def check_for_blackjack(player_hand_total, dealer_hand_total, player_money, bet_amount):
    blackjack_check = 0
    if player_hand_total == 21 and dealer_hand_total == 21:
        print("No winners, it's a push")
    elif player_hand_total == 21:
        print("\nCongratulations.  You win!")
        player_money += round(bet_amount * 1.5)
        blackjack_check = 1
    elif dealer_hand_total == 21:
        print("\nSorry.  You lose.")
        player_money -= bet_amount
        blackjack_check = 1
    money.write_money(player_money)
    return blackjack_check


def play_blackjack(player_money):
    i = 1
    deck_of_cards = get_deck()
    bet_amount = get_bet(player_money)
    dealer_hand = [deck_of_cards.pop(0), deck_of_cards.pop(0)]
    player_hand = [deck_of_cards.pop(0), deck_of_cards.pop(0)]
    player_hand_total = get_hand_value(player_hand)
    dealer_hand_total = get_hand_value(dealer_hand)

    print("\nDEALER's SHOW CARD")
    print(dealer_hand[0][0], dealer_hand[0][1])
    print("\nYOUR CARDS")
    for card in player_hand:
        print(card[0], card[i])
    blackjack_check = check_for_blackjack(player_hand_total, dealer_hand_total, player_money, bet_amount)
    while blackjack_check == 1:
        break
    player_money = player_turn(deck_of_cards, player_hand, player_money, bet_amount)

    print(f"test for player hand value in play blackjact +++> {player_money}")

    dealer_turn(deck_of_cards, player_hand_total, dealer_hand, dealer_hand_total, player_money, bet_amount, player_hand)


def main():
    print()
    print("BLACKJACK!")
    print("Blackjack payout is 3:2")
    play_again = "y"
    while play_again.lower() == "y":
        player_money = money.read_money()
        play_blackjack(player_money)
        play_again = input("\nPlay again (y/n): ")
    print("Come back Soon!")
    print("Bye!")


if __name__ == '__main__':
    main()
