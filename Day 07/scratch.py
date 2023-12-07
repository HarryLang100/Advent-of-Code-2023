from main import compare_two_hands

initial_hands_bid_list = [['32T3K', 765], 
                          ['T55J5', 684], 
                          ['KK677', 28], 
                          ['KTJJT', 220], 
                          ['QQQJA', 483]]

proper_order_hands_bid_list = [['32T3K', 765],
                               ['KTJJT', 220],
                               ['KK677', 28],
                               ['T55J5', 684],
                               ['QQQJA', 483]]

def sort_hands_bid_list(hands_bid_list):
    """
    Returns the list sorted from weakest to strongest hand.
    """

    number_hands = len(hands_bid_list)
    swaps = True
    
    while swaps:
        swaps = False
        for i in range(number_hands - 1):
            if compare_two_hands(hands_bid_list[i][0], 
                                     hands_bid_list[i + 1][0]):
                temp = hands_bid_list[i]
                hands_bid_list[i] = hands_bid_list[i + 1]
                hands_bid_list[i + 1] = temp
                swaps = True
                
    return hands_bid_list

print(sort_hands_bid_list(initial_hands_bid_list))