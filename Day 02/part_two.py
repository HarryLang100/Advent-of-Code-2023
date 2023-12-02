def read_file(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines

def find_minimum_cubes(line):
    """
    Return the minimum numbers of cubes required to play the game.
    Format (red, blue, green)
    """
    line_split_by_shown = line[line.find(":") + 1:].split(";")
    current_minimums = {'red': 0,
                        'blue': 0,
                        'green': 0}
    for current_showing in line_split_by_shown:
        for cubes_shown in current_showing.split(","):
            cubes_shown = cubes_shown.strip()
            colour = cubes_shown.split(" ")[1]
            number = int(cubes_shown.split(" ")[0])
            if current_minimums[colour] < number:
                current_minimums[colour] = number
    return current_minimums

def calculate_power(minimum_cubes_needed):
    return minimum_cubes_needed['red'] * \
        minimum_cubes_needed['blue'] * \
        minimum_cubes_needed['green']
        
def main(filename):
    lines = read_file(filename)
    running_power_sum = 0
    for current_line in lines:
        running_power_sum += calculate_power(find_minimum_cubes(current_line))
    return running_power_sum

if __name__ == "__main__":
    answer = main("Inputs/input.txt")
    print(answer)