import pytest

from part_two import check_string, get_first_digit, \
    get_last_digit

class TestCheckString:
    
    def test_one(self):
        assert check_string("hello harry", "hello") == True
    
    def test_two(self):
        assert check_string("bye harry", "hello") == False
        
class TestGetFirstDigit:
    
    def test_one(self):
        assert get_first_digit("two1nine") == "2"
    
    def test_two(self):
        assert get_first_digit("abcone2threexyz") == "1"

class TestGetLastDigit:
    
    def test_one(self):
        assert get_last_digit("two1nine") == "9"
        
    def test_two(self):
        assert get_last_digit("eightwothree") == "3"