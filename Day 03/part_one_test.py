import pytest

from part_one import check_whether_symbol
from part_one import check_whether_part_number
from part_one import process_line
from part_one import main

example_schematic = ['467..114..',
                     '...*......',
                     '..35..633.',
                     '......#...',
                     '617*......',
                     '.....+.58.',
                     '..592.....',
                     '......755.',
                     '...$.*....',
                     '.664.598..']



class TestCheckWhetherSymbol:
    
    def test_multiple(self):
        
        assert check_whether_symbol(".") == False
        assert check_whether_symbol("5") == False
        assert check_whether_symbol("@") == True
        assert check_whether_symbol("$") == True

class TestCheckWhetherNumberPartNumber:
    
    def test_example_first_row_one(self):
        actual = check_whether_part_number({'row': 0,
                                                   'first_column': 0,
                                                   'last_column': 2},
                                                   example_schematic)
        expected = True  # Because it's adjacent to a symbol
        assert actual == expected
        
    def test_example_first_row_two(self):
        actual = check_whether_part_number({'row': 0,
                                                   'first_column': 5,
                                                   'last_column': 7},
                                                   example_schematic)
        expected = False  # Because it's not adjacent to a symbol
        assert actual == expected
        
    def test_example_third_row_one(self):
        actual = check_whether_part_number({'row': 2,
                                                   'first_column': 2,
                                                   'last_column': 3},
                                                  example_schematic)
        expected = True  # Because it's adjacent to a symbol
        assert actual == expected
        
class TestProcessLine:
    
    def test_example_line_0(self):
        actual = process_line(0, example_schematic)
        expected = 467
        assert actual == expected
        
    def test_example_line_1(self):
        actual = process_line(1, example_schematic)
        expected = 0
        assert actual == expected
        
    def test_example_line_2(self):
        actual = process_line(2, example_schematic)
        expected = 668  # 35 + 633
        assert actual == expected
        
    def test_example_line_3(self):
        actual = process_line(3, example_schematic)
        expected = 0
        assert actual == expected
        
    def test_example_line_4(self):
        actual = process_line(4, example_schematic)
        expected = 617
        assert actual == expected
        
    def test_example_line_5(self):
        actual = process_line(5, example_schematic)
        expected = 0
        assert actual == expected
        
    def test_example_line_6(self):
        actual = process_line(6, example_schematic)
        expected = 592
        assert actual == expected
        
    def test_example_line_7(self):
        actual = process_line(7, example_schematic)
        expected = 755
        assert actual == expected
                
    def test_example_line_8(self):
        actual = process_line(8, example_schematic)
        expected = 0
        assert actual == expected
        
    def test_example_line_9(self):
        actual = process_line(9, example_schematic)
        expected = 1262  # 664 + 598
        assert actual == expected
    
class TestMain:
    
    def test_example(self):
        actual = main("Inputs/example.txt")
        expected = 4361
        assert actual == expected
        