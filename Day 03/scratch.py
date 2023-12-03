from part_one import read_file
from part_one import check_whether_part_number

filename = "Inputs/example.txt"

schematic = read_file(filename)
line = schematic[0]

def process_line(line_index, schematic):
    part_number_running_total = 0
    current_line = schematic[line_index]
    #for index in range(len(current_line)):
    index = 0
    while index < len(current_line):
        if current_line[index].isdigit():
            first_index = index
            last_index = index
            while current_line[last_index + 1].isdigit():
                last_index += 1
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
        
assert process_line(0, schematic) == 467