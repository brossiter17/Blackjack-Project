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
    # print(deck_of_cards)

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
            print("Invalid bet. Please enter another bet.")
    player_money -= bet_amount
    return bet_amount


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

            if player_hand_total > 21:
                print("Sorry.  You lose.")
                player_money -= bet_amount
                print(f"Money: {player_money}")
                money.write_money(player_money)
                break

        elif player_choice.lower() == "stand":
            break


def dealer_turn(deck_of_cards, player_hand_total, dealer_hand, dealer_hand_total, player_money, bet_amount):
    i = 1

    print(f"This is a test of the deck of cards ==> {deck_of_cards}")

    if player_hand_total <= 21:
        print("\nDEALER'S CARDS:")
        for card in dealer_hand:
            print(card[0], card[i])

        while dealer_hand_total <= 17:
            dealer_hand.append(deck_of_cards.pop(0))

            #for card in dealer_hand:
            #    print(card[0], card[i])

        print(f"\nYOUR POINTS: {player_hand_total:>8}")
        print(f"DEALER'S POINTS: {dealer_hand_total:>5}")

        if dealer_hand_total > 21:
            print("\nCongratulations.  You win!")
            player_money += bet_amount
            money.write_money(player_money)
            print(f"Money: {player_money}")
        elif dealer_hand_total > player_hand_total and dealer_hand_total <= 21:
            print("\nSorry.  You lose.")
            player_money -= bet_amount
            money.write_money(player_money)
            print(f"Money: {player_money}")
        elif player_hand_total > dealer_hand_total and player_hand_total <= 21:
            print("\nCongratulations.  You win!")
            player_money += bet_amount
            money.write_money(player_money)
            print(f"Money: {player_money}")
        elif player_hand_total == dealer_hand_total:
            print("\nIT'S A TIE!")
            player_money += bet_amount
            money.write_money(player_money)
            print(f"Money: {player_money}")


def check_for_blackjack(player_hand_total, dealer_hand_total, player_money, bet_amount):
    if player_hand_total == 21 and dealer_hand_total == 21:
        print("No winners, it's a push")
    elif player_hand_total == 21:
        print("\nCongratulations.  You win!")
        player_money += bet_amount
        money.write_money(player_money)
        print(f"Money: {player_money}")
    elif dealer_hand_total == 21:
        print("\nSorry.  You lose.")
        player_money -= bet_amount
        money.write_money(player_money)
        print(f"Money: {player_money}")


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


    #for card in dealer_hand:
    #    print(card[0], card[i])


    print("\nYOUR CARDS")
    for card in player_hand:
        print(card[0], card[i])


    check_for_blackjack(player_hand_total, dealer_hand_total, player_money, bet_amount)

    player_turn(deck_of_cards, player_hand, player_money, bet_amount)

    #while True:
    #    player_choice = input("\nHit or stand? (hit/stand): ")
    #    if player_choice.lower() == 'hit':
    #        player_hand.append(deck_of_cards.pop(0))
    #        print("\nYOUR CARDS")
    #        for card in player_hand:
    #            print(card[0], card[i])

    #        player_hand_total = get_hand_value(player_hand)

    ##        if player_hand_total > 21:
    #            print("Sorry.  You lose.")
    #            player_money -= bet_amount
    #            print(f"Money: {player_money}")
    #            player_money = money.write_money(player_money)
    #            #print(f"Money: {player_money}")
    #            break
    #        continue
    #    elif player_choice.lower() == "stand":
    #        break


    #player_hand_total = get_hand_value(player_hand)
    #dealer_hand_total = get_hand_value(dealer_hand)

    dealer_turn(deck_of_cards, player_hand_total, dealer_hand, dealer_hand_total, player_money, bet_amount)

    #if player_hand_total <= 21:
    #    print("\nDEALER'S CARDS:")
    #    for card in dealer_hand:
    #        print(card[0], card[i])

    #while dealer_hand_total <= 17:
    #    dealer_hand.append(deck_of_cards.pop(0))

    #    for card in dealer_hand:
    #        print(card[0], card[i])

    #    print(f"\nYOUR POINTS: {player_hand_total:>8}")
    #    print(f"DEALER'S POINTS: {dealer_hand_total:>5}")

    #    if dealer_hand_total > 21:
    #        print("\nCongratulations.  You win!")
    #        player_money += bet_amount
    #        money.write_money(player_money)
    #        print(f"Money: {player_money}")
    #    elif dealer_hand_total > player_hand_total and dealer_hand_total <= 21:
    #        print("\nSorry.  You lose.")
    #        player_money -= bet_amount
    #        money.write_money(player_money)
    #        print(f"Money: {player_money}")
    #    elif player_hand_total > dealer_hand_total and player_hand_total <= 21:
    #        print("\nCongratulations.  You win!")
    #        player_money += bet_amount
    #        money.write_money(player_money)
    #        print(f"Money: {player_money}")
    #    elif player_hand_total == dealer_hand_total:
    #        print("\nIT'S A TIE!")
    #        player_money += bet_amount
    #        money.write_money(player_money)
    #        print(f"Money: {player_money}")



def main():
    print()
    print("BLACKJACK!")
    print("Blackjack payout is 3:2")

    play_again = "y"
    while play_again.lower() == "y":
        player_money = money.read_money()
        play_blackjack(player_money)
        print()

        play_again = input("Play again (y/n): ")
        print()

    print("Come back Soon!")
    print("Bye!")


if __name__ == '__main__':
    main()
