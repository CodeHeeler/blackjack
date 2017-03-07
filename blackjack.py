import random


class Card:
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

    def suits(self):
        return ['Hearts', 'Diamonds', 'Spades', 'Clubs']

    def values(self):
        return ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

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
        self.soft = 0
        self.hard = 0
        self.stand = False


    def add_card(self, card):
        self.cards_in_hand.append(card)
        self.sum_hand()

    # def remove_card(self, card):
    #     self.cards_in_hand.remove(card)

    def __repr__(self):
        return "{}".format(self.cards_in_hand)


    def __str__(self):
        return "{}".format(self.cards_in_hand)


    def sum_hand(self):
        for card in self.cards_in_hand:
            if card.value in ['Jack', 'Queen', 'King']:
                self.soft += 10
                self.hard += 10
            elif card.value == 'Ace':
                self.soft += 11
                self.hard += 1
            else:
                self.soft += int(card.value)
                self.hard += int(card.value)

    def is_loss(self):
        if self.soft > 21:
            if self.hard > 21:
                return True
        else:
            return False



def main():
    d = Deck()
    d.shuffle()
    dealer = Hand()
    temp = []
    dealer.add_card(d.deal())
    dealer.add_card(d.deal())
    temp.append(dealer.cards_in_hand[-1])
    player1 = Hand()
    player1.add_card(d.deal())
    player1.add_card(d.deal())
    print("Dealer has: {} ".format(temp))
    print("You have: {} \n\n".format(player1))

    while True:
        hit_or_stand = input("Would you like to hit or stand? (h/s) ")
        if hit_or_stand == 'h':
            player1.add_card(d.deal())
            if player1.is_loss():
                break
            else:
                print("Dealer has: {} ".format(temp))
                print("You have: {} \n\n".format(player1))
        else:
            player1.stand = True
            break

    while not dealer.is_loss() and not dealer.stand:
        dealer.add_card(d.deal())
        if dealer.soft >= 17 or dealer.hard >= 17:
            dealer.stand = True

    print("Final--")
    print("Dealer had: {} ".format(dealer))
    print("You had: {} \n\n".format(player1))
    if dealer.is_loss():
        if player1.is_loss():
            print("It was a tie or push.")
        elif dealer.is_loss():
            print("You won!")
    elif player1.is_loss():
        print("You lost.")
    elif dealer.hard == 21 or dealer.soft == 21 and player1.hard == 21 or player1.soft == 21:
        print("It was a tie or push.")
    elif dealer.hard == 21 or dealer.soft == 21:
        print("You lost.")
    elif player1.hard == 21 or player1.soft == 21:
        print("You won!")
    elif player1.hard > dealer.hard and player1.hard > dealer.soft or player1.soft > dealer.hard and player1.soft > dealer.soft:
        print("You won!")
    elif dealer.hard > player1.hard and dealer.hard > player1.soft or dealer.soft > player1.hard and dealer.soft > player1.soft:
        print("You lost.")
    else:
        print("It was a tie or push.")


if __name__ == "__main__":
    main()
