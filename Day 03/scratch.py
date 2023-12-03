filename = "Inputs/example.txt"

def read_file(filename):
    with open(filename) as f:
        schematic = f.read().splitlines()
    return schematic

def check_whether_part_number(number_description,
                                     schematic):
    number_is_part_number = False  # Assume False, make true if adjacent to
                                   # a part number.
    for row_index in range(number_description['row'] - 1,
                           number_description['row'] + 2):
        for col_index in range(number_description['first_column'] - 1,
                               number_description['last_column'] + 2):
            if (row_index >= 0 and
                row_index <= len(schematic) - 1 and
                col_index >= 0 and
                col_index <= len(schematic[0]) - 1):
                    if check_whether_symbol(schematic[row_index][col_index]):
                        number_is_part_number = True
    return number_is_part_number
            
                        
    
def check_whether_symbol(character):
    """
    Returns True if the character is a symbol, False otherwise.
    A symbol is anything other than a period or a digit in 
    1 through 9.

    """
    not_characters = ['.', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    assert len(character) == 1, Exception(f"Character '{character}' not of "\
                                          f"length 1.")
    if character in not_characters:
        result = False
    else:
        result = True
        print(f"Found character!: {character}")
    return result

def process_line(line_index, schematic):
    part_number_running_total = 0
    current_line = schematic[line_index]
    #for index in range(len(current_line)):
    index = 0
    while index < len(current_line):
        if current_line[index].isdigit():
            first_index = index
            last_index = index
            try:
                while current_line[last_index + 1].isdigit():
                    last_index += 1
            except:
                pass
            if check_whether_part_number({'row': line_index,
                                          'first_column': first_index,
                                          'last_column': last_index},
                                         schematic):
                part_number = int(current_line[first_index:last_index + 1]) 
                part_number_running_total += part_number
                print(f"Found part number! {part_number}")
            index = last_index + 1
        else:
            index += 1
    return part_number_running_total

toy_schematic_1 = ['11.&.'] # Expected output 0

toy_schematic_2 = ['........',
                   '.24..4..',
                   '......*.'] # Expected output 4

schematic = toy_schematic_2

running_part_number_sum = 0
for index, line in enumerate(schematic):
    running_part_number_sum += process_line(index, schematic)
print(running_part_number_sum)

