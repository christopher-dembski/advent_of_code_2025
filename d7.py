def parse_input(file_name):
    with open(file_name) as file:
        return tuple(tuple(line) for line in file.read().strip().split())


def draw_beams(grid):
    grid = [list(row) for row in grid]
    positions = ((r, c) for r in range(1, len(grid)) for c in range(len(grid[0])))
    for r, c in positions:
        symbol = grid[r][c]
        symbol_above = grid[r - 1][c]
        if symbol_above in ('S', '|'):
            if symbol == '.':
                grid[r][c] = '|'
            elif symbol == '^':
                grid[r][c - 1] = '|'
                grid[r][c + 1] = '|'
    return grid


def count_splits(grid):
    return sum(grid[r][c] == '^' and grid[r - 1][c] == '|'
               for r in range(1, len(grid))
               for c in range(len(grid[0])))


def part_one(file_name):
    grid = parse_input(file_name)
    grid = draw_beams(grid)
    return count_splits(grid)


print(part_one('inputs/d7b.txt'))
