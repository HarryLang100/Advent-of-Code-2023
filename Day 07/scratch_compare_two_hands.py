from main import get_hand_type, compare_hands_same_type

def compare_two_hands(hand1, hand2):
    # Return True if hand1 is stronger than hand2, False otherwise.
    breakpoint()
    if get_hand_type(hand1) > get_hand_type(hand2):
        result = True
    if get_hand_type(hand1) < get_hand_type(hand2):
        result = False
    else:
        result = compare_hands_same_type(hand1, hand2)
        
    return result

hand1 = "T55J5"  # 'three of a kind', 4
hand2 = "KTJJT"  # 'two pair', 3
# hand1 should be stronger than hand 3.

print(compare_two_hands(hand1, hand2))