word_digits_dict = {'one': '1',
                    'two': '2',
                    'three': '3',
                    'four': '4',
                    'five': '5',
                    'six': '6',
                    'seven': '7',
                    'eight': '8',
                    'nine': '9'}

def read_file(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    return lines

def check_string(string, word):
    """ Tests to see if 'string' begins with 'word'.
    E.g. check_string("hello harry", "hello") = True
    But check_string("bye harry") = False
    """
    
    word_match = False
    try:
        if string[:len(word)] == word:
            word_match = True
    except:
        pass
    return word_match


def get_first_digit(line):
    digit_found = False
    for index, character in enumerate(line):
        if not digit_found:
            if character.isdigit():
                digit_found = True
                result_digit = character
            else:
                for digit_word in word_digits_dict.keys():
                    if check_string(line[index:], digit_word):
                        result_digit = word_digits_dict[digit_word]
                        digit_found = True
    if not digit_found:
        raise Exception(f"No digit found in {line}.")
    return result_digit

def get_last_digit(line):
    digit_found = False
    for index, character in enumerate(line[::-1]):
        if not digit_found:
            if character.isdigit():
                digit_found = True
                result_digit = character
            else:
                for digit_word in word_digits_dict.keys():
                    if check_string(line[len(line)-index-1:], digit_word):
                        result_digit = word_digits_dict[digit_word]
                        digit_found = True
    if not digit_found:
        raise Exception(f"No digit found in {line}.")
    return result_digit
    
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
    part_two_example_result = main("Inputs/part_two_example.txt")
    if part_two_example_result == 281:
        print("Example check passed.")
        print(f'Calculated answer: {main("Inputs/input.txt")}')
    else:
        print("Example check failed.")
        print(f'Produced {part_two_example_result} instead of 281.')
