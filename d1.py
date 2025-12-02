def parse_input(file_name):
    directions = []
    distances = []
    with open(file_name) as file:
        for line in file:
            directions.append(line[0])
            distances.append(int(line[1::]))
    return directions, distances


def part_one(file_name):
    directions, distances = parse_input(file_name)
    times_pointing_at_zero = 0
    position = 50
    for direction, distance in zip(directions, distances):
        if direction == 'R':
            position += distance
        else:  # direction == 'L'
            position -= distance
        position %= 100
        if position == 0:
            times_pointing_at_zero += 1
    return times_pointing_at_zero


def part_two(file_name):
    directions, distances = parse_input(file_name)
    times_passed_zero = 0
    position = 50
    for direction, distance in zip(directions, distances):
        old_position = position
        if direction == 'R':
            position += distance
        else:  # direction == 'L'
            position -= distance
        if old_position != 0 and position <= 0:
            times_passed_zero += 1
        times_passed_zero += abs(position) // 100
        position %= 100
    return times_passed_zero


print(part_one('inputs/d1b.txt'))
print(part_two('inputs/d1b.txt'))
