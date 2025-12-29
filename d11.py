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
    incoming_edges = {node: set() for node in (*outgoing_edges, 'out')}
    for node, neighbours in outgoing_edges.items():
        for neighbour in neighbours:
            incoming_edges[neighbour].add(node)
    return incoming_edges


def num_paths(incoming_edges):
    paths_memo = {'you': 1}

    def num_paths_recurse(destination):
        if destination in paths_memo:
            return paths_memo[destination]
        num = sum(num_paths_recurse(incoming) for incoming in incoming_edges[destination])
        paths_memo[destination] = num
        return num

    return num_paths_recurse('out')


def part_one(file_name):
    outgoing_edges = parse_input(file_name)
    incoming_edges = incoming_edges_from_outgoing_edges(outgoing_edges)
    return num_paths(incoming_edges)


print(part_one('inputs/d11b.txt'))
