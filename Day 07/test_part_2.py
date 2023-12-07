import pytest

from part_two_main import get_hand_type

class TestGetHandType:
    
    def test_problem_description_examples(self):
        
        assert get_hand_type("32T3K") == 2  # one pair
        assert get_hand_type("KK677") == 3  # two pair
        assert get_hand_type("T55J5") == 6  # four of a kind
        assert get_hand_type("KTJJT") == 6  # four of a kind
        assert get_hand_type("QQQJA") == 6  # four of a kind
    
    def test_more_examples(self):
        # Examples I've come up with myself.
        assert get_hand_type("AJJJJ") == 7  # 5 of a kind
        assert get_hand_type("AAJJJ") == 7  # 5 of a kind
        assert get_hand_type("AAAJJ") == 7  # 5 of a kind
        assert get_hand_type("AABJJ") == 6  # 4 of a kind
        assert get_hand_type("AABBJ") == 5  # Full house