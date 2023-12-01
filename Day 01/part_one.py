def read_file(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    return lines

def get_first_digit(line):
    digit_found = False
    for character in line:
        if character.isdigit():
            digit_found = True
            break
    if not digit_found:
        raise Exception(f"No digit found in {line}.")
    return character


def get_last_digit(line):
    digit_found = False
    for character in line[::-1]:
        if character.isdigit():
            digit_found = True
            break
    if not digit_found:
        raise Exception(f"No digit found in {line}.")
    return character

def get_calibration_value(line):
    first_digit = get_first_digit(line)
    last_digit = get_last_digit(line)
    combined_number = first_digit + last_digit # This is a string.
    return int(combined_number)
    
def main(filename):
    running_total = 0
    lines = read_file(filename)
    for current_line in lines:
        running_total += get_calibration_value(current_line)
    return running_total

if __name__ == "__main__":
    if main("Inputs/example.txt") == 142:
        print("Example check passed.")
        print(f'Calculated answer: {main("Inputs/input.txt")}')
    else:
        print("Example check failed.")
        print(f'Produced {main("Inputs/example.txt")} instead of 142.')
        