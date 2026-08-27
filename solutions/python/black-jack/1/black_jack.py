def value_of_card(card):
    if card == 'A':
        return 1
    if card in ["2", "3", "4", "5", "6", "7", "8", "9", "10"]:
        return int(card)
    if card == 'J' or 'K' or 'Q':
        return 10
    
def higher_card(card_one, card_two):
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)
    if value_one > value_two:
        return card_one
    if value_one < value_two:
        return card_two
    if value_one == value_two:
       return(card_one, card_two)
 
def value_of_ace(card_one, card_two):
    if card_one == 'A' or card_two == 'A':
        return 1
    total = value_of_card(card_one) + value_of_card(card_two)

    if total + 11 <= 21:
        return 11
    else:
        return 1
    if card_one == 'A' or card_two == 'A':
        return 1
    
def is_blackjack(card_one, card_two):
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)

    if (value_one == 10 and card_two == 'A') or (card_one == 'A' and value_two == 10):
        return True
    else:
        return False

        
def can_split_pairs(card_one, card_two):
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)

    if value_one == value_two or card_one == card_two:
        return True
    else:
        return False
        
        
"""Determine if a player can split their hand into two hands.

    Parameters:
        card_one (str): First card in the hand.
        card_two (str): Second card in the hand.

   Returns:
        bool: Can the hand be split into two pairs? (i.e. cards are of the same value).
    """



def can_double_down(card_one, card_two):
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)
    total = value_one + value_two

    if total in [9, 10, 11]:
        return True
    else:
        return False
    """Determine if a blackjack player can place a double down bet.

    Parameters:
        card_one (str): First card in the hand.
        card_two (str): Second card in the hand.

    Returns:
        bool: Can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """

