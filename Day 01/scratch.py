word_digits_dict = {'one': '1',
                    'two': '2',
                    'three': '3',
                    'four': '4',
                    'five': '5',
                    'six': '6',
                    'seven': '7',
                    'eight': '8',
                    'nine': '9'}

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