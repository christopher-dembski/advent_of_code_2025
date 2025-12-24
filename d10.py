import re


def parse_input(file_name):
    with open(file_name) as file:
        lines = file.read().strip().split('\n')
    lights_buttons = []
    for line in lines:
        match = re.fullmatch(r'\[(?P<lights>.+)](?P<buttons>.+)\{(?P<joltage>.+)}', line)
        lights = parse_lights(match.group('lights').strip())
        buttons = parse_buttons(match.group('buttons').strip())
        lights_buttons.append((lights, buttons))
    return lights_buttons


# '.###.#' -> 101110
def parse_lights(lights_string):
    lights = 0
    mask = 1
    for ch in lights_string:
        if ch == '#':
            lights |= mask
        mask <<= 1
    return lights


# [(0, 1, 3), ...] -> [001011, ...]
def parse_buttons(buttons_string):
    buttons = []
    for string in buttons_string.split():
        string = string.removeprefix('(').removesuffix(')')
        numbers = tuple(int(n) for n in string.split(','))
        button_mask = 0
        for n in reversed(numbers):
            button_mask |= (1 << n)
        buttons.append(button_mask)
    return buttons


def min_presses(lights, buttons):
    seen = {0}
    configs = {0}
    presses = 0
    while lights not in seen:
        prev_configs = configs
        configs = set()
        presses += 1
        for old_config in prev_configs:
            for button_mask in buttons:
                new_config = old_config ^ button_mask
                if new_config in seen:
                    continue
                seen.add(new_config)
                configs.add(new_config)
    return presses


def part_one(file_name):
    return sum(min_presses(lights, buttons) for lights, buttons in parse_input(file_name))


print(part_one('inputs/d10b.txt'))
