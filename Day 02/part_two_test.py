import pytest

from part_two import find_minimum_cubes, calculate_power

class TestFindMinimumCubes:
    
    def test_first_example(self):
        line1 = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
        expected_output = {'red': 4, 'green': 2, 'blue': 6}
        actual_output = find_minimum_cubes(line1)
        assert actual_output == expected_output
        
class TestCalculatePower:
    
    def test_first_example(self):
        cubes_needed = {'red': 4, 'green': 2, 'blue': 6}
        expected_output = 4 * 2 * 6
        actual_output = calculate_power(cubes_needed)
        assert actual_output == expected_output