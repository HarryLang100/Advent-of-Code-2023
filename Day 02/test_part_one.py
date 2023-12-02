import pytest

from part_one import check_line, main

class TestCheckLine:
    
    def test_example_lines(self):
        line1 = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
        line2 = "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green,"\
            " 1 blue"
        line3 = "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; "\
            "5 green, 1 red"
        line4 = "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, "\
            "15 blue, 14 red"
        line5 = "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
        
        assert check_line(line1) == 1
        assert check_line(line2) == 2
        assert check_line(line3) == 0
        assert check_line(line4) == 0
        assert check_line(line5) == 5
        
class TestMain:
    
    def test_example(self):
        expected_outcome = 8
        actual_outcome = main("Inputs/example.txt")
        assert actual_outcome == expected_outcome