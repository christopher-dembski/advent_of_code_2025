def parse_input(file_name):
    with open(file_name) as file:
        return tuple(tuple(int(n) for n in line.split(',')) for line in file.read().strip().split())


def euclidean_distance(a, b):
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2) ** 0.5


def build_pairs_sorted_by_distance(coordinates):
    pairs_with_distances = []
    for a in coordinates:
        for b in coordinates:
            if a >= b:  # only track connections one way, ex. (1, 2, 3) -> (4, 5, 6) but not (4, 5, 6) -> (1, 2, 3)
                continue
            distance = euclidean_distance(a, b)
            pairs_with_distances.append((distance, a, b))
    pairs_with_distances.sort()
    return [(a, b) for _, a, b in pairs_with_distances]


def find_circuit(position, circuits):
    for circuit in circuits:
        if position in circuit:
            return circuit
    return None


def build_circuits(coordinates, num_connections):
    pairs_sorted_by_distance = build_pairs_sorted_by_distance(coordinates)[:num_connections]
    circuits = set()
    for a, b in pairs_sorted_by_distance:
        circuit_a = find_circuit(a, circuits)
        circuit_b = find_circuit(b, circuits)
        if circuit_a and circuit_b and circuit_a != circuit_b:
            circuits.remove(circuit_a)
            circuits.remove(circuit_b)
            circuits.add((*circuit_a, *circuit_b))
        elif circuit_a and not circuit_b:
            circuits.remove(circuit_a)
            circuits.add((*circuit_a, b))
        elif circuit_b and not circuit_a:
            circuits.remove(circuit_b)
            circuits.add((*circuit_b, a))
        elif not circuit_a and not circuit_b:
            circuits.add((a, b))
    return circuits


def part_one(file_name, num_connections):
    coordinates = parse_input(file_name)
    circuits = build_circuits(coordinates, num_connections)
    circuits = sorted(circuits, key=len, reverse=True)
    return len(circuits[0]) * len(circuits[1]) * len(circuits[2])


print(part_one('inputs/d8a.txt', 10))
print(part_one('inputs/d8b.txt', 1000))
