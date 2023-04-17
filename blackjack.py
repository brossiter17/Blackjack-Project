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
    while player_money < 5:
        need_chips = input("Minimum bet is $5.  Would you like to buy more chips (y/n): ")
        if need_chips.lower() == "y":
            player_money += buy_chips()
            money.write_money(player_money)
            print(f"\nMoney: {player_money}")
            break
        elif need_chips.lower() == "n":
            print("\nCome back Soon!")
            print("Bye!")
            exit()
        else:
            print("\nInvalid option. Yes or no (y/n) only.")
            continue
    while True:
        try:
            bet_amount = float(input("Bet amount: "))
            if bet_amount < 5 or bet_amount >= 1000:
                print("\nInvalid bet. Bet must be tween $5 and $1000.")
                continue
            elif bet_amount > player_money:
                print(f"\nInvalid bet. You have {player_money}")
                continue
            return bet_amount, player_money
        except ValueError:
            print("\nInvalid bet. Please enter another bet.")
            continue

def buy_chips():
    while True:
        try:
            amount_of_chips = float(input("How many chips would you like to buy: "))
            if amount_of_chips < 5:
                print("\nMinimum purchase is $5.")
                continue
            else:
                return amount_of_chips
        except ValueError:
            print("\nInvalid option. Please enter a number.")
            continue

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
                print("\nBUSTED! Sorry.  You lose.")
                player_money = player_money - bet_amount
                print(f"Money: {player_money}")
                return player_money, "game_over"
            else:
                continue
        elif player_choice.lower() == "stand":
            return player_money, "player_stand"
        else:
            print("\nInvalid option. Hit or stand only.")
            continue
def dealer_turn(deck_of_cards, dealer_hand, player_hand, player_money, bet_amount):
    i = 1
    player_hand_total = get_hand_value(player_hand)
    dealer_hand_total = get_hand_value(dealer_hand)
    if player_hand_total <= 21:
        print("\nDEALER'S CARDS:")
    while dealer_hand_total <= 17:
        dealer_hand.append(deck_of_cards.pop(0))
        dealer_hand_total = get_hand_value(dealer_hand)
    for card in dealer_hand:
        print(card[0], card[i])
    if dealer_hand_total > 21:
        print(f"\nYOUR POINTS:  {player_hand_total}")
        print(f"DEALER'S POINTS: {dealer_hand_total}")
        print("\nCongratulations.  You win!")
        player_money = player_money + bet_amount
    elif dealer_hand_total > player_hand_total and dealer_hand_total <= 21:
        print(f"\nYOUR POINTS:  {player_hand_total}")
        print(f"DEALER'S POINTS: {dealer_hand_total}")
        print("\nSorry.  You lose.")
        player_money = player_money - bet_amount
    elif player_hand_total > dealer_hand_total and player_hand_total <= 21:
        print(f"\nYOUR POINTS:  {player_hand_total}")
        print(f"DEALER'S POINTS: {dealer_hand_total}")
        print("\nCongratulations.  You win!")
        player_money = player_money + bet_amount
    elif player_hand_total == dealer_hand_total:
        print(f"\nYOUR POINTS:  {player_hand_total}")
        print(f"DEALER'S POINTS: {dealer_hand_total}")
        print("\nNo winners, it's a push")
    money.write_money(player_money)
    print(f"Money: {player_money}")
    return player_money

def check_for_blackjack(player_hand_total, dealer_hand_total, dealer_hand):
    i= 1
    if player_hand_total == 21 and dealer_hand_total == 21:
        print("\nNo winners, it's a push")
        return "no_win"
    elif player_hand_total == 21:
        print("\nDEALER's SHOW CARD")
        for card in dealer_hand:
            print(card[0], card[i])
        print("\nBlackjack! Congratulations.  You win!")
        return "player_win"
    elif dealer_hand_total == 21:
        print("\nDEALER's SHOW CARD")
        for card in dealer_hand:
            print(card[0], card[i])
        print("\nDealer has Blackjack!.  You lose.")
        return "dealer_win"


def play_blackjack():
    i = 1
    player_money = money.read_money()
    print(f"\nMoney: {player_money}")
    deck_of_cards = get_deck()
    bet_amount, player_money  = get_bet(player_money)
    dealer_hand = [deck_of_cards.pop(0), deck_of_cards.pop(0)]
    player_hand = [deck_of_cards.pop(0), deck_of_cards.pop(0)]
    player_hand_total = get_hand_value(player_hand)
    dealer_hand_total = get_hand_value(dealer_hand)
    print("\nDEALER's SHOW CARD")
    print(dealer_hand[0][0], dealer_hand[0][1])
    print("\nYOUR CARDS")
    for card in player_hand:
        print(card[0], card[i])
    blackjack_check = check_for_blackjack(player_hand_total, dealer_hand_total, dealer_hand)
    if blackjack_check == "no_win":
        pass
    elif blackjack_check == "dealer_win":
        player_money -= bet_amount
        money.write_money(player_money)
        return
    elif blackjack_check == "player_win":
        player_money += round(bet_amount * 1.5)
        money.write_money(player_money)
        return
    player_money, player_condition = player_turn(deck_of_cards, player_hand, player_money, bet_amount)
    if player_condition == "player_stand":
        player_money = dealer_turn(deck_of_cards, dealer_hand, player_hand, player_money, bet_amount)
    money.write_money(player_money)


def main():
    print()
    print("BLACKJACK!")
    print("Blackjack payout is 3:2")
    play_again = "y"
    while play_again.lower() == "y":
        play_blackjack()
        play_again = input("\nPlay again (y/n): ")
        if play_again.lower() == "n":
            break
        elif play_again.lower() == "y":
            continue
        else:
            print("Invalid option.  Try again")
        print()
        play_again = input("Do you want to play again (y/n)?: ")
    print("\nCome back Soon!")
    print("Bye!")


if __name__ == '__main__':
    main()
