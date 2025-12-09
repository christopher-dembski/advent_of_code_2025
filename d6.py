from functools import reduce
from operator import add, mul


def parse_input(file_name):
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


def solve(operands, operator_symbol):
    operator = add if operator_symbol == '+' else mul
    return reduce(operator, operands)


def part_one(file_name):
    problems = parse_input(file_name)
    return sum(solve(operands, operator_symbol) for operands, operator_symbol in problems)


print(part_one('inputs/d6b.txt'))
