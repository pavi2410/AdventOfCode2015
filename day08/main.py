from ast import literal_eval


def part1(_input: str) -> int:
    s = 0
    for line in _input.splitlines():
        if not line or not line.startswith('"'):
            pass

        k = literal_eval(line)
        s += len(line) - len(k)
    return s


def part2(_input: str) -> int:
    s = 0
    for line in _input.splitlines():
        if not line or not line.startswith('"'):
            pass

        k = 2
        k += line.count('\\')
        k += line.count('"')

        s += k
    return s


if __name__ == "__main__":
    import os

    input_file = os.path.join(os.path.dirname(__file__), "input.txt")
    with open(input_file) as f:
        _input = f.read()
        print("Part 1 answer:", part1(_input))
        print("Part 2 answer:", part2(_input))
