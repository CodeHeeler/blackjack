from blackjack import *

c = Card('SPADES', '4')
c1 = Card('spades', '4')
c2 = Card('Hearts', '5')
d = Deck()
d1 = Deck()
h = Hand()
h.add_card(c)


def test_card_init():
    my_card = Card('Spades', '4')


def test_card_values():
    assert c.values() == ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']


def test_card_suits():
    assert c.suits() == ['Hearts', 'Diamonds', 'Spades', 'Clubs']


def test_card_value():
    assert c.value == '4'


def test_card_compare():
    assert c.__eq__(c1) is True
    assert c.__eq__(c2) is False


def test_card_suit_compare():
    assert c.eq_suits(c1) is True
    assert c.eq_suits(c2) is False


def test_card_value_compare():
    assert c.eq_values(c1) is True
    assert c.eq_values(c2) is False


def test_card_repr():
    assert c.__repr__() == '4S'


def test_card_str():
    assert c.__str__() == '4 of Spades'


def test_deck_init():
    my_deck = Deck()


def test_deck_deal():
    assert (d.deal()).__repr__() == 'KC'


def test_hand_init():
    my_hand = Hand()


# def test_hand_add():
#     assert h == ['4S']
