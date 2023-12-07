def count_character_frequencies(hand):
    frequencies = {}
    for character in hand:
        if character in frequencies:
            frequencies[character] += 1
        else:
            frequencies[character] = 1
    
    return frequencies

def get_hand_type_part_2(hand):
    """
    7 for 'Five of a kind'
    6 for 'Four of a kind'
    5 for 'Full house'
    4 for 'Three of a kind'
    3 for 'Two pair'
    2 for 'One pair'
    1 for 'High card'
    """
    
    character_frequencies = count_character_frequencies(hand)
    max_frequency = max(character_frequencies.values())
    max_frequency += character_frequencies.get("J", 0)
    if max_frequency >= 5:
        result = 7  # 'Five of a kind'
    elif max_frequency == 4:
        result = 6  # 'Four of a kind'
    elif max_frequency == 3 and 2 in character_frequencies.values():
        result = 5  # 'Full house'
    elif max_frequency == 3:
        result = 4  # 'Three of a kind'
    elif sorted(list(character_frequencies.values())) == [1, 2, 2]:
        result = 3  # 'Two pair'
    elif sorted(list(character_frequencies.values())) == [1, 1, 1, 2]:
        result = 2  # 'One pair'
    elif sorted(list(character_frequencies.values())) == [1, 1, 1, 1, 1]:
        result = 1  # 'High card'
    else:
        raise Exception(f"Hand {hand} does not seem to match a type.")
    
    return result


def compare_hands_same_type_part_2(hand1, hand2):
    """
    Returns True if hand1 is stronger False otherwise.

    """
    
    card_strengths = {"A": 13,
                      "K": 12,
                      "Q": 11,
                      "T": 9,
                      "9": 8,
                      "8": 7,
                      "7": 6,
                      "6": 5,
                      "5": 4,
                      "4": 3,
                      "3": 2,
                      "2": 1,
                      "J": 0}
    
    result = False  # Assume False. Set to True if it turns out
    # hand1 is stronger.
    for index in range(len(hand1)):
        current_hand1_card = hand1[index]
        current_hand2_card = hand2[index]
        if current_hand1_card == current_hand2_card:
            pass
        elif card_strengths[current_hand1_card] > card_strengths[current_hand2_card]:
            result = True
            break
        elif card_strengths[current_hand1_card] < card_strengths[current_hand2_card]:
            result = False
            break
        else:
            raise Exception(f"Can't compare cards {current_hand1_card} and {current_hand2_card}.")
        
    return result

def compare_two_hands(hand1, hand2):
    # Return True if hand1 is stronger than hand2, False otherwise.
    if get_hand_type_part_2(hand1) > get_hand_type_part_2(hand2):
        result = True
    elif get_hand_type_part_2(hand1) < get_hand_type_part_2(hand2):
        result = False
    else:
        result = compare_hands_same_type_part_2(hand1, hand2)
        
    return result
    

def parse_input(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    hands_bids_list = []
    for line in lines:
        hands_bids_list.append([line.split()[0], int(line.split()[1])])
    return hands_bids_list


def sort_hands_bid_list(hands_bid_list):
    """
    Returns the list sorted from weakest to strongest hand.
    """

    number_hands = len(hands_bid_list)
    swaps = True
    
    while swaps:
        swaps = False
        for i in range(number_hands - 1):
            if compare_two_hands_part_2(hands_bid_list[i][0], 
                                        hands_bid_list[i + 1][0]):
                temp = hands_bid_list[i]
                hands_bid_list[i] = hands_bid_list[i + 1]
                hands_bid_list[i + 1] = temp
                swaps = True
                
    return hands_bid_list
    

def part_two_main(filename):
    
    # Setup
    hands_bid_list = parse_input(filename)
    
    hands_bid_list_ordered = sort_hands_bid_list(hands_bid_list)
    
    rank_bid_list = []
    
    for index in range(len(hands_bid_list_ordered)):
        rank_bid_list.append([index + 1, hands_bid_list_ordered[index][1]])
    
    running_total = 0
    for pair in rank_bid_list:
        running_total += pair[0]*pair[1]
    
                
    return running_total
    