START_POSITION = 50
NUM_POSITIONS = 100

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
    position = START_POSITION
    for direction, distance in zip(directions, distances):
        if direction == 'R':
            position += distance
        else:  # direction == 'L'
            position -= distance
        position %= NUM_POSITIONS
        if position == 0:
            times_pointing_at_zero += 1
    return times_pointing_at_zero


if __name__ == '__main__':
    print(part_one('inputs/d1b.txt'))
