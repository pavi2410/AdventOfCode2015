def part1(_input: str) -> int:
    return _input.count("(") - _input.count(")")


def part2(_input: str) -> int:
    floor = 0
    for i, c in enumerate(_input):
        floor += 1 if c == "(" else -1
        if floor == -1:
            return i + 1


if __name__ == "__main__":
    import os

    input_file = os.path.join(os.path.dirname(__file__), "input.txt")
    with open(input_file) as f:
        _input = f.read()
        print("Part 1 answer:", part1(_input))
        print("Part 2 answer:", part2(_input))
