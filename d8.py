def parse_input(file_name):
    with open(file_name) as file:
        return tuple(tuple(int(n) for n in line.split(',')) for line in file.read().strip().split())


def euclidean_distance(a, b):
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2) ** 0.5


def build_pairs_sorted_by_distance(boxes):
    pairs_distances = []
    for box_a in boxes:
        for box_b in boxes:
            if box_a >= box_b:  # only track connections one way, ex. (1, 2, 3) -> (4, 5, 6) not (4, 5, 6) -> (1, 2, 3)
                continue
            distance = euclidean_distance(box_a, box_b)
            pairs_distances.append((distance, box_a, box_b))
    pairs_distances.sort()  # sort by distance
    return [(a, b) for _, a, b in pairs_distances]  # do not need to keep distance


def find_circuit(box, circuits):
    for circuit in circuits:
        if box in circuit:
            return circuit
    return None


def update_circuits(box_a, box_b, circuits):  # connect junction box a to junction box b (mutates circuits)
    circuit_a = find_circuit(box_a, circuits)
    circuit_b = find_circuit(box_b, circuits)
    if circuit_a and circuit_b and circuit_a != circuit_b:
        circuits.remove(circuit_a)
        circuits.remove(circuit_b)
        circuits.add((*circuit_a, *circuit_b))
    elif circuit_a and not circuit_b:
        circuits.remove(circuit_a)
        circuits.add((*circuit_a, box_b))
    elif circuit_b and not circuit_a:
        circuits.remove(circuit_b)
        circuits.add((*circuit_b, box_a))
    elif not circuit_a and not circuit_b:
        circuits.add((box_a, box_b))


def build_circuits(boxes, num_connections):
    pairs_sorted_by_distance = build_pairs_sorted_by_distance(boxes)[:num_connections]
    circuits = {(box,) for box in boxes}
    for box_a, box_b in pairs_sorted_by_distance:
        update_circuits(box_a, box_b, circuits)
    return circuits


def connect_all(boxes):
    pairs_sorted_by_distance = build_pairs_sorted_by_distance(boxes)
    circuits = {(box,) for box in boxes}
    for box_a, box_b in pairs_sorted_by_distance:
        update_circuits(box_a, box_b, circuits)
        if len(circuits) == 1:
            return box_a[0] * box_b[0]


def part_one(file_name, num_connections):
    box_coordinates = parse_input(file_name)
    circuits = sorted(build_circuits(box_coordinates, num_connections), key=len, reverse=True)
    return len(circuits[0]) * len(circuits[1]) * len(circuits[2])


def part_two(file_name):
    box_coordinates = parse_input(file_name)
    return connect_all(box_coordinates)


print(part_one('inputs/d8b.txt', 1000))
print(part_two('inputs/d8b.txt'))
