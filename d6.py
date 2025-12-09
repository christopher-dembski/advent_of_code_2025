from functools import reduce
from operator import add, mul
import re


def parse_input_part_one(file_name):
    with open(file_name) as file:
        lines = file.read().strip().split('\n')
    num_problems = len(lines[0].split())
    operator_symbols = lines[-1].split()
    operand_lists = [[] for _ in range(num_problems)]
    for line in lines[:-1]:
        numbers = line.split()
        for i, n in enumerate(numbers):
            operand_lists[i].append(int(n))
    return tuple(zip(operand_lists, operator_symbols))


def parse_input_part_two(file_name):
    columns = read_columns(file_name)
    num_problems = sum(column.endswith('+') or column.endswith('*') for column in columns)
    operand_lists = [[] for _ in range(num_problems)]
    operator_symbols = []
    problem_number = 0
    for c, column in enumerate(columns):
        match = re.fullmatch(r'\s*(?P<digits>\d+)?\s*(?P<operator>\+|\*)?', column)
        if operator := match.group('operator'):
            operator_symbols.append(operator)
        if digits := match.group('digits'):
            operand_lists[problem_number].append(int(digits))
        else:  # done parsing this problem (empty line)
            problem_number += 1
    return tuple(zip(operand_lists, operator_symbols))


def read_columns(file_name):
    with open(file_name) as file:
        rows = file.read().split('\n')
    length_longest_row = max(map(len, rows))
    return tuple(''.join(row.ljust(length_longest_row)[c] for row in rows) for c in range(length_longest_row))


def solve(operands, operator_symbol):
    operator = add if operator_symbol == '+' else mul
    return reduce(operator, operands)


def part_one_and_two(file_name, part):
    problems = parse_input_part_one(file_name) if part == 1 else parse_input_part_two(file_name)
    return sum(solve(operands, operator_symbol) for operands, operator_symbol in problems)


print(part_one_and_two('inputs/d6b.txt', part=1))
print(part_one_and_two('inputs/d6b.txt', part=2))
