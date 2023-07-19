from hashlib import md5


def part1(_input: str) -> int:
    i = 0
    while True:
        h = md5(f"{_input}{i}".encode()).hexdigest()
        if h.startswith('00000'):
            return i
        i += 1


def part2(_input: str) -> int:
    i = 0
    while True:
        h = md5(f"{_input}{i}".encode()).hexdigest()
        if h.startswith('000000'):
            return i
        i += 1


if __name__ == "__main__":
    _input = "ckczppom"
    print("Part 1 answer:", part1(_input))
    print("Part 2 answer:", part2(_input))
