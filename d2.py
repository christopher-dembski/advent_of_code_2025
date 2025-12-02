def parse_input(file_name):
    with open(file_name) as file:
        ranges = (pair.split('-') for pair in
                  file.read().strip().split(','))
        return tuple((int(n1), int(n2)) for n1, n2 in ranges)


def part_one(file_name):
    ranges = parse_input(file_name)
    total = 0
    for start, end in ranges:
        for n in range(start, end + 1):
            s = str(n)
            if len(s) % 2 == 0 and s[:len(s) // 2] == s[len(s) // 2:]:
                total += n
    return total


print(part_one('inputs/d2b.txt'))
