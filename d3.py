def parse_input(file_name):
    with open(file_name) as file:
        banks = file.read().strip().split()
        return tuple(tuple(int(n) for n in bank) for bank in banks)


def max_joltage(bank):
    max_digit_seen = 0
    max_value = 0
    for n in bank:
        max_value = max(max_value, max_digit_seen * 10 + n)
        max_digit_seen = max(max_digit_seen, n)
    return max_value


def part_one(file_name):
    banks = parse_input(file_name)
    return sum(max_joltage(bank) for bank in banks)


print(part_one('inputs/d3b.txt'))
