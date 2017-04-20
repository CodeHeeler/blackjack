import random


class Card:

    suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']

    values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    def __init__(self, suit, value):
        self.suit = (suit.lower()).capitalize()
        self.value = (value.lower()).capitalize()

    def __repr__(self):
        if self.value == '10':
            return '{}{}'.format(self.value[:2], self.suit[:1])
        else:
            return '{}{}'.format(self.value[:1], self.suit[:1])

    def __str__(self):
        return '{} of {}'.format(self.value, self.suit)

    def __eq__(self, other):
        return (self.suit, self.value) == (other.suit, other.value)

    def eq_suits(self, other):
        return self.suit == other.suit

    def eq_values(self, other):
        return self.value == other.value


class Deck:
    def __init__(self):
        self.card_list = []
        for suit in ['Hearts', 'Diamonds', 'Spades', 'Clubs']:
          for value in range(1, 14):
              if value == 1:
                  self.card_list.append(Card(suit, 'Ace'))
              elif value == 11:
                  self.card_list.append(Card(suit, 'Jack'))
              elif value == 12:
                  self.card_list.append(Card(suit, 'Queen'))
              elif value == 13:
                  self.card_list.append(Card(suit, 'King'))
              else:
                  self.card_list.append(Card(suit, str(value)))


    def __repr__(self):
        return "{}".format(self.card_list)


    def __str__(self):
        return "{}".format(self.card_list)


    def deal(self):
        return self.card_list.pop()


    def shuffle(self):
        random.shuffle(self.card_list)



class Hand:
    def __init__(self):
        self.cards_in_hand = []

    def add_card(self, card):
        self.cards_in_hand.append(card)

    def __repr__(self):
        return "{}".format(self.cards_in_hand)

    def __str__(self):
        return "{}".format(self.cards_in_hand)

    def show_dealer_hand(self):
        return "{}".format(self.cards_in_hand[1:])

    def score_hand(self):
        aces = 0
        score = 0
        for card in self.cards_in_hand:
            if card.value in ['Jack', 'Queen', 'King']:
                score += 10
            elif card.value == 'Ace':
                score += 11
                aces +=1
            else:
                score += int(card.value)
        while score > 21 and aces > 0:
            score -= 10
            aces -= 1
        return score

    def bust(self):
        return self.score_hand() > 21

class Player:
    def __init__(self, hand):
        self.hand = hand

class Dealer(Player):
    def hit(self):
        return self.hand.score_hand() < 17

class HumanPlayer(Player):
    def hit(self):
        choice = input("Would you like to hit or stand (h/s)? ")
        if choice == "h":
            return True
        return False

def main():

    d = Deck()
    d.shuffle()
    dealer = Dealer(Hand())
    player = HumanPlayer(Hand())
    dealer.hand.add_card(d.deal())
    dealer.hand.add_card(d.deal())
    player.hand.add_card(d.deal())
    player.hand.add_card(d.deal())
    dealer_public = "\nDealer has: "
    dealer_public += dealer.hand.show_dealer_hand()
    print(dealer_public)
    print("You have: {} \n\n".format(player.hand))

    while not player.hand.bust() and player.hit():
        player.hand.add_card(d.deal())
        print("\nYou now have: {} \n\n".format(player.hand))

    if player.hand.bust():
        print("You busted, you lose.\n")
        return

    while dealer.hit() and not dealer.hand.bust():
        dealer.hand.add_card(d.deal())

    print("\nDealer now has {} \n".format(dealer.hand))
    if dealer.hand.bust():
        print("Dealer busted, you win.\n")
        return

    player_score = player.hand.score_hand()
    dealer_score = dealer.hand.score_hand()

    if player_score == dealer_score:
        print("It was a push.\n")
    elif player_score > dealer_score:
        print("You win!\n")
    else:
        print("You lose.\n")


if __name__ == "__main__":
    main()
