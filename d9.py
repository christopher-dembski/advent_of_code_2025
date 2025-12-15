def parse_input(file_name):
    with open(file_name) as file:
        return tuple(tuple(int(n) for n in line.split(','))
                     for line in file.read().strip().split())


def area(corner_1, corner_2):
    x_dim = abs(corner_1[0] - corner_2[0]) + 1
    y_dim = abs(corner_1[1] - corner_2[1]) + 1
    return x_dim * y_dim


def part_one(file_name):
    positions = parse_input(file_name)
    return max(area(corner_1, corner_2) for corner_1 in positions for corner_2 in positions)


print(part_one('inputs/d9b.txt'))
