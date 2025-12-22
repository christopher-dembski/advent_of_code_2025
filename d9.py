import itertools as it


def parse_input(file_name):
    with open(file_name) as file:
        return tuple(tuple(int(n) for n in line.split(','))
                     for line in file.read().strip().split())


def area(corner_1, corner_2):
    x_dim = abs(corner_1[0] - corner_2[0]) + 1
    y_dim = abs(corner_1[1] - corner_2[1]) + 1
    return x_dim * y_dim


# colour the path with green sqaures and
# adjacent squares just outside the enclosed shape white
def colour_path_and_adjacent(reds):
    greens = set()
    whites = set()
    reds_offset_by_one = (*reds[1::], reds[0])
    for (x1, y1), (x2, y2) in zip(reds, reds_offset_by_one):
        if x1 == x2:  # vertical
            if y1 < y2:  # moving down
                for y in range(y1, y2 + 1):
                    current = (x1, y)
                    if current not in reds:
                        greens.add(current)
                    adjacent_right = (x1 + 1, y)
                    if adjacent_right not in greens and adjacent_right not in reds:
                        whites.add(adjacent_right)
            else:  # moving up
                for y in range(y1, y2 - 1, -1):
                    current = (x1, y)
                    if current not in reds:
                        greens.add(current)
                    adjacent_left = (x1 - 1, y)
                    if adjacent_left not in greens and adjacent_left not in reds:
                        whites.add(adjacent_left)
        else:  # horizontal
            if x1 < x2:  # moving right
                for x in range(x1, x2 + 1):
                    current = (x, y1)
                    if current not in reds:
                        greens.add(current)
                    adjacent_above = (x, y1 - 1)
                    if adjacent_above not in greens and adjacent_above not in reds:
                        whites.add(adjacent_above)
            else:  # moving left
                for x in range(x1, x2 - 1, -1):
                    current = (x, y1)
                    if current not in reds:
                        greens.add(current)
                    adjacent_below = (x, y1 + 1)
                    if adjacent_below not in greens and adjacent_below not in reds:
                        whites.add(adjacent_below)
    whites -= greens  # some get coloured white that should be green
    return greens, whites


# trace paths between corners
# if encounter white, know outside the enclosed shape, so invalid rectangle
def valid_rectangle(x1, y1, x2, y2, whites):
    # ensure (x1, y1) top left and (x2, y2) bottom right
    # this rectangle covers the same squares as the original
    x1, x2 = sorted([x1, x2])
    y1, y2 = sorted([y1, y2])
    # move horizontal then vertical
    if any((x, y1) in whites for x in range(x1 + 1, x2 + 1)):
        return False
    if any((x2, y) in whites for y in range(y1 + 1, y2 + 1)):
        return False
    # move vertical then horizontal
    if any((x1, y) in whites for y in range(y1 + 1, y2 + 1)):
        return False
    if any((x, y2) in whites for x in range(x1 + 1, x2 + 1)):
        return False
    # did not encounter white space on either path
    return True


# helper function for debugging
def display_grid(reds, greens, whites):
    max_x = max(x for x, y in it.chain(reds, greens, whites))
    max_y = max(y for x, y in it.chain(reds, greens, whites))
    for y in range(0, max_y + 1):
        for x in range(0, max_x + 1):
            p = (x, y)
            symbol = 'R' if p in reds else 'G' if p in greens else 'W' if p in whites else '.'
            print(symbol, end='')
        print()
    print()


def part_one(file_name):
    positions = parse_input(file_name)
    return max(area(corner_1, corner_2) for corner_1 in positions for corner_2 in positions)


def part_two(file_name):
    reds = parse_input(file_name)
    greens, whites = colour_path_and_adjacent(reds)
    whites -= greens
    mx = 0
    for red_1 in reds:
        for red_2 in reds:
            if valid_rectangle(*red_1, *red_2, whites):
                mx = max(mx, area(red_1, red_2))
    return mx


print(part_two('inputs/d9a.txt'))
print(part_two('inputs/d9b.txt'))
