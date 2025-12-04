DIRECTION_VECTORS = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))


def parse_input(file_name):
    with open(file_name) as file:
        return [list(line) for line in file.read().strip().split()]


def within_grid(grid, r, c):
    return 0 <= r < len(grid) and 0 <= c < len(grid[0])


def adjacent_rolls(grid, r, c):
    return tuple((r + dr, c + dc)
                 for dr, dc in DIRECTION_VECTORS
                 if within_grid(grid, r + dr, c + dc) and grid[r + dr][c + dc] == '@')


def can_remove(grid, r, c):
    return len(adjacent_rolls(grid, r, c)) < 4


def part_one(file_name):
    grid = parse_input(file_name)
    return sum(symbol == '@' and can_remove(grid, r, c) for r, row in enumerate(grid) for c, symbol in enumerate(row))


def part_two(file_name):
    grid = parse_input(file_name)
    rolls_to_remove = {(r, c) for r, row in enumerate(grid) for c, symbol in enumerate(row)
                       if symbol == '@' and can_remove(grid, r, c)}
    while rolls_to_remove:
        r, c = rolls_to_remove.pop()
        grid[r][c] = 'x'  # mark as removed
        rolls_to_remove.update((ar, ac) for ar, ac in adjacent_rolls(grid, r, c) if can_remove(grid, ar, ac))
    return sum(symbol == 'x' for row in grid for symbol in row)


print(part_one('inputs/d4b.txt'))
print(part_two('inputs/d4b.txt'))
