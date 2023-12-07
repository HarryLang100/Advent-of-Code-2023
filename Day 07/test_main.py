import pytest

from main import get_hand_type
from main import compare_hands_same_type
from main import compare_two_hands

class TestGetHandType:
    
    def test_problem_description_examples(self):
        """
        These are the examples from the problem description, not the
        example text file.
        """
        
        assert get_hand_type("AAAAA") == 7
        assert get_hand_type("AA8AA") == 6
        assert get_hand_type("23332") == 5
        assert get_hand_type("TTT98") == 4
        assert get_hand_type("23432") == 3
        assert get_hand_type("A23A4") == 2
        assert get_hand_type("23456") == 1
        
class TestCompareHandsSameType:
    
    def test_first_problem_description_example(self):
        # Both type 'four of a kind'
        hand1 = "33332" # Hand1 is stronger because first card is stronger
        hand2 = "2AAAA"
        assert compare_hands_same_type(hand1, hand2)
        assert compare_hands_same_type(hand2, hand1) == False
        
class TestCompareTwoHands:
    
    def test_general(self):
        assert compare_two_hands("AAAAA", "AA8AA")
        assert compare_two_hands("AAAAA", "32T3K")