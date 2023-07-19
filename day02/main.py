def parse_input(_input: str) -> tuple[int, ...]:
    return tuple(map(int, _input.split("x")))


def part1(_input: str) -> int:
    s = 0
    for line in _input.splitlines():
        l, w, h = parse_input(line)

        s += 2 * l * w + 2 * w * h + 2 * h * l + min(l * w, w * h, h * l)
    return s


def part2(_input: str) -> int:
    s = 0
    for line in _input.splitlines():
        l, w, h = parse_input(line)

        s += l * w * h + 2 * min(l + w, w + h, h + l)
    return s


if __name__ == "__main__":
    import os

    input_file = os.path.join(os.path.dirname(__file__), "input.txt")
    with open(input_file) as f:
        _input = f.read()
        print("Part 1 answer:", part1(_input))
        print("Part 2 answer:", part2(_input))
