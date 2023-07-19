import string


def part1(_input: str) -> int:
    n = 0
    for line in _input.splitlines():
        if len([c for c in line if c in 'aeiou']) >= 3:
            if any([c1 == c2 for c1, c2 in zip(line, line[1:])]):
                if all([c not in line for c in ['ab', 'cd', 'pq', 'xy']]):
                    n += 1
    return n


def part2(_input: str) -> int:
    n = 0
    for line in _input.splitlines():
        if any([line.count(line[i:i+2]) >= 2 for i in range(len(line) - 1)]):
            if any([line[i] == line[i+2] for i in range(len(line) - 2)]):
                n += 1
    return n


if __name__ == "__main__":
    import os

    input_file = os.path.join(os.path.dirname(__file__), "input.txt")
    with open(input_file) as f:
        _input = f.read()
        print("Part 1 answer:", part1(_input))
        print("Part 2 answer:", part2(_input))
