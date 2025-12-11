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


def count_timelines(grid):
    grid = [list(row) for row in grid]
    positions = ((r, c) for r in range(1, len(grid)) for c in range(len(grid[0])))
    for r, c in positions:
        value = grid[r][c]
        if value != '|':
            continue
        value_above = grid[r - 1][c]
        value_above_left = grid[r - 1][c - 1] if c - 1 >= 0 else None
        value_above_right = grid[r - 1][c + 1] if c + 1 < len(grid[0]) else None
        value_left = grid[r][c - 1] if c - 1 >= 0 else None
        value_right = grid[r][c + 1] if c + 1 < len(grid[0]) else None
        grid[r][c] = 0
        if value_above == 'S':
            grid[r][c] += 1
            continue
        if type(value_above) is int:
            grid[r][c] += value_above
        if value_left == '^' and type(value_above_left) is int:
            grid[r][c] += value_above_left
        if value_right == '^' and type(value_above_right) is int:
            grid[r][c] += value_above_right
    last_row = grid[-1]
    return sum(n for n in last_row if type(n) is int)


def part_one(file_name):
    grid = parse_input(file_name)
    grid = draw_beams(grid)
    return count_splits(grid)


def part_two(file_name):
    grid = parse_input(file_name)
    grid = draw_beams(grid)
    return count_timelines(grid)


print(part_one('inputs/d7b.txt'))
print(part_two('inputs/d7b.txt'))
