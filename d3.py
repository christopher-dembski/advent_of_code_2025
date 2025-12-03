def parse_input(file_name):
    with open(file_name) as file:
        banks = file.read().strip().split()
        return tuple(tuple(int(n) for n in bank) for bank in banks)


def max_joltage_part_one(bank):
    max_digit_seen = 0
    max_value = 0
    for n in bank:
        max_value = max(max_value, max_digit_seen * 10 + n)
        max_digit_seen = max(max_digit_seen, n)
    return max_value


def max_joltage_part_two(bank):
    maxes = [0 for _ in range(13)]  # maxes[i] = max value that can be made with i digits
    for i, n in enumerate(bank):
        for num_digits in range(min(i + 1, 12), 0, -1):
            maxes[num_digits] = max(maxes[num_digits], maxes[num_digits - 1] * 10 + n)
    return maxes[12]


def solve(file_name, part):
    banks = parse_input(file_name)
    max_joltage = max_joltage_part_one if part == 1 else max_joltage_part_two
    return sum(max_joltage(bank) for bank in banks)


print(solve('inputs/d3b.txt', 1))
print(solve('inputs/d3b.txt', 2))
