import bisect


class MultiRange:
    def __init__(self, range_tuples):
        self.ranges = MultiRange.merge_ranges(range_tuples)

    def __contains__(self, n):
        # 0 is a dummy value to create a valid tuple, we search using the start value
        i = bisect.bisect_right(self.ranges, (n, 0))
        if i == 0:
            return False
        start, end = self.ranges[i - 1]
        return n <= end

    @staticmethod
    def merge_ranges(ranges):
        ranges = sorted(ranges)
        merged_ranges = [ranges[0]]
        for start, end in ranges:
            prev_start, prev_end = merged_ranges[-1]
            if start > prev_end:  # no overlap
                merged_ranges.append((start, end))
            elif end <= prev_end:  # fully contained
                continue
            else:  # start <= prev_end and end > prev_end
                merged_ranges.pop()
                merged_ranges.append((prev_start, end))
        return merged_ranges


def parse_input(file_name):
    with open(file_name) as file:
        ranges_text, ids_text = file.read().strip().split('\n\n')
        start_end_pairs = (line.split('-') for line in ranges_text.split())
        ranges = tuple((int(start), int(end)) for start, end in start_end_pairs)
        ids = tuple(int(n) for n in ids_text.split())
        return ranges, ids


def part_one(file_name):
    range_tuples, ingredient_ids = parse_input(file_name)
    multi_range = MultiRange(range_tuples)
    return sum(ingredient_id in multi_range for ingredient_id in ingredient_ids)


print(part_one('inputs/d5b.txt'))
