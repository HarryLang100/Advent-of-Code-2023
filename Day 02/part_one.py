limit_dict = {'red': 12,
              'green': 13,
              'blue': 14}

def read_file(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines

def check_line(line):
    """
    If it is possible for this game to be shown, return the game ID.
    If not, return 0.
    """
    game_ID = int(line[5:line.find(":")])
    line_split_by_shown = line[line.find(":") + 1:].split(";")
    all_possible = True
    for current_showing in line_split_by_shown:
        for cubes_shown in current_showing.split(","):
            cubes_shown = cubes_shown.strip()
            colour = cubes_shown.split(" ")[1]
            number = int(cubes_shown.split(" ")[0])
            if number > limit_dict[colour]:
                all_possible = False
    result = game_ID if all_possible else 0
    return result
    
def main(filename):
    lines = read_file(filename)
    running_ID_sum = 0
    for current_line in lines:
        running_ID_sum += check_line(current_line)
    return running_ID_sum

if __name__ == "__main__":
    answer = main("Inputs/input.txt")
    print(answer)