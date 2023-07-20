def resolve_signal(wires, name):
    if name.isnumeric():
        return int(name)

    if name in wires:
        v = wires[name]

        if isinstance(v, int):
            return v

        wires[name] = v()
        return resolve_signal(wires, name)


def _not(wires, a, rhs):
    wires[rhs] = lambda: ~resolve_signal(wires, a) & 0xFFFF


def _and(wires, a, b, rhs):
    wires[rhs] = lambda: resolve_signal(wires, a) & resolve_signal(wires, b)


def _or(wires, a, b, rhs):
    wires[rhs] = lambda: resolve_signal(wires, a) | resolve_signal(wires, b)


def _lshift(wires, a, b, rhs):
    wires[rhs] = lambda: resolve_signal(wires, a) << resolve_signal(wires, b)


def _rshift(wires, a, b, rhs):
    wires[rhs] = lambda: resolve_signal(wires, a) >> resolve_signal(wires, b)


def _set(wires, a, rhs):
    wires[rhs] = lambda: resolve_signal(wires, a)


def part1(_input: str):
    wires = {}
    for line in _input.splitlines():
        lhs, rhs = line.split(" -> ")
        match lhs.split():
            case ["NOT", a]:
                _not(wires, a, rhs)
            case [a, "AND", b]:
                _and(wires, a, b, rhs)
            case [a, "OR", b]:
                _or(wires, a, b, rhs)
            case [a, "LSHIFT", b]:
                _lshift(wires, a, b, rhs)
            case [a, "RSHIFT", b]:
                _rshift(wires, a, b, rhs)
            case [a]:
                _set(wires, a, rhs)
    return wires


def part2(_input: str):
    b_ = str(resolve_signal(part1(_input), "a")) + " -> b"
    wires = part1(_input + b_)
    return wires


if __name__ == "__main__":
    import os

    input_file = os.path.join(os.path.dirname(__file__), "input.txt")
    with open(input_file) as f:
        _input = f.read()
        print("Part 1 answer:", resolve_signal(part1(_input), "a"))
        print("Part 2 answer:", resolve_signal(part2(_input), "a"))
