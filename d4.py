DIRECTION_VECTORS = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))


def parse_input(file_name):
    with open(file_name) as file:
        return tuple(tuple(line) for line in file.read().strip().split())


def within_grid(grid, r, c):
    return 0 <= r < len(grid) and 0 <= c < len(grid[0])


def adjacent_rolls(grid, r, c):
    return sum(within_grid(grid, r + dr, c + dc) and grid[r + dr][c + dc] == '@'
               for dr, dc in DIRECTION_VECTORS)


def part_one(file_name):
    grid = parse_input(file_name)
    return sum(symbol == '@' and adjacent_rolls(grid, r, c) < 4
               for r, row in enumerate(grid)
               for c, symbol in enumerate(row))


print(part_one('inputs/d4b.txt'))
