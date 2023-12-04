  def parse_line(line):
    """
    Return tuple (list of winning numbers, list of your numbers)
    """
    winning_numbers_string, your_numbers_string = line.split(":")[1].split("|")
    winning_numbers = [num for num in winning_numbers_string.strip().split(" ") if num.isdigit()]
    your_numbers = [num for num in your_numbers_string.strip().split(" ") if num.isdigit()]
    
    return (winning_numbers, your_numbers)

def count_matches(winning_numbers, your_numbers):
    running_count = 0
    for number in your_numbers:
        if number in winning_numbers:
            running_count += 1
            
    return running_count
    
def main(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    running_total = 0
    for line in lines:
        number_matches = count_matches(*parse_line(line))
        if number_matches >= 1:
            running_total += 2**(number_matches - 1)
    
    return running_total

if __name__ == "__main__":
    result = main("Inputs/input.txt")
    print(result)