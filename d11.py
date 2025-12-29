def parse_input(file_name):
    with open(file_name) as file:
        lines = file.read().strip().split('\n')
    outgoing_edges = {}
    for line in lines:
        node, neighbours = line.split(':')
        neighbours = set(neighbours.strip().split())
        outgoing_edges[node] = neighbours
    return outgoing_edges


def incoming_edges_from_outgoing_edges(outgoing_edges):
    incoming_edges = {node: set() for node in (*outgoing_edges.keys(), 'out')}
    for node, neighbours in outgoing_edges.items():
        for neighbour in neighbours:
            incoming_edges[neighbour].add(node)
    return incoming_edges


def num_paths(start, destintion, incoming_edges):
    memo = {start: 1}

    def num_paths_recurse(destination):
        if destination in memo:
            return memo[destination]
        num = sum(num_paths_recurse(incoming) for incoming in incoming_edges[destination])
        memo[destination] = num
        return num

    return num_paths_recurse(destintion)


def part_one(file_name):
    outgoing_edges = parse_input(file_name)
    incoming_edges = incoming_edges_from_outgoing_edges(outgoing_edges)
    return num_paths('you', 'out', incoming_edges)


def part_two(file_name):
    outgoing_edges = parse_input(file_name)
    incoming_edges = incoming_edges_from_outgoing_edges(outgoing_edges)
    svr_fft = num_paths('svr', 'fft', incoming_edges)
    fft_dac = num_paths('fft', 'dac', incoming_edges)
    dac_fft = num_paths('dac', 'fft', incoming_edges)
    dac_out = num_paths('dac', 'out', incoming_edges)
    return svr_fft * (fft_dac if fft_dac > 0 else dac_fft) * dac_out


print(part_one('inputs/d11b.txt'))
print(part_two('inputs/d11b.txt'))
