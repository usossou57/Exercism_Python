"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    value = 0
    set_1 = ("2","3","4","5","6","7","8","9", "10")
    set_2 = ("J","Q","K")
    
    if card in set_1:
        value = int(card)
    elif card in set_2:
        value = 10
    else:
        value = 1

    return value 


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    higher = ""
    value_1,value_2 = value_of_card(card_one),value_of_card(card_two)
    if value_1 < value_2:
        higher = card_two
    elif value_2 < value_1:
        higher = card_one
    else:
        higher = card_one,card_two

    return higher

def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for an upcoming ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    def new_value_card(card):
        
        value = 0
        set_1 = ("2","3","4","5","6","7","8","9", "10")
        set_2 = ("J","Q","K")
        
        if card in set_1:
            value = int(card)
        elif card in set_2:
            value = 10
        else:
            value = 11

        return value
    
    value_1,value_2 = new_value_card(card_one),new_value_card(card_two)
    sum = value_1 + value_2

    if sum < 11:
        return 11
    else:
        return 1


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """

    a = "A" in (card_one, card_two)
    b = card_one in ("J","Q","K","10")
    c = card_two in ("J","Q","K","10")
    d = b or c
    e = a and d
    return e


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """

    value_1,value_2 = value_of_card(card_one),value_of_card(card_two)
    return value_1 == value_2


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """
    
    value_1,value_2 = value_of_card(card_one),value_of_card(card_two)
    sum = value_1 + value_2

    return sum in (9, 10, 11)
