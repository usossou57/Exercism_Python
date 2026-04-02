"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """

    rounds = [i+number for i in range(3)]
    return rounds


def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """

    liste = rounds_1 + rounds_2
    return liste


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """

    verificateur = number in rounds
    return verificateur


def card_average(hand):
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """

    moyenne = sum(hand)/len(hand)
    return moyenne


def approx_average_is_average(hand):
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """

    vraie_moyenne = sum(hand)/len(hand)
    moy_alt_1 = (hand[0]+hand[-1])/2
    moy_alt_2 = hand[int((len(hand)//2))]
    verif_1 = vraie_moyenne == moy_alt_1
    verif_2 = vraie_moyenne == moy_alt_2
    verif = verif_1 or verif_2

    return verif
        


def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """

    moy_pair = sum(hand[::2])/len(hand[::2])
    moy_impair = sum(hand[1::2])/len(hand[1::2])
    verif = moy_impair == moy_pair

    return verif


def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """

    if hand[-1] == 11:
        hand[-1] = 22
    else:
        hand[-1] = hand[-1]

    return hand
