import pytest

from main import parse_line

example_line_1 = "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"

class TestParseLine:
    
    def test_example_line_1(self):
        expected_output = (["41", "48", "83", "86", "17"],
                           ["83", "86", "6", "31", "17", "9", "48", "53"])
        actual_output = parse_line(example_line_1)
        assert actual_output == expected_output
