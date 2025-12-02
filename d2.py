def parse_input(file_name):
    with open(file_name) as file:
        ranges = (pair.split('-') for pair in
                  file.read().strip().split(','))
        return tuple((int(n1), int(n2)) for n1, n2 in ranges)


def solve(file_name, part):
    ranges = parse_input(file_name)
    validator = valid_part_one if part == 1 else valid_part_two
    total = 0
    for start, end in ranges:
        for n in range(start, end + 1):
            if validator(n):
                total += n
    return total


def valid_part_one(n):
    string = str(n)
    return len(string) % 2 == 0 and string[:len(string) // 2] == string[len(string) // 2:]


def valid_part_two(n):
    string = str(n)
    length = len(string)
    for num_splits in range(2, length + 1):
        split_size = length // num_splits
        sub_strings = {string[start_index:start_index + split_size]
                       for start_index in range(0, length, split_size)}
        if len(sub_strings) == 1:
            return True
    return False


print(solve('inputs/d2b.txt', part=1))
print(solve('inputs/d2b.txt', part=2))
