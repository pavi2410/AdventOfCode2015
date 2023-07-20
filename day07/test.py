from .main import part1, resolve_signal


def test_part1():
    instructions = """\
123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i"""

    wires = part1(instructions)

    inputs = {
        "d": 72,
        "e": 507,
        "f": 492,
        "g": 114,
        "h": 65412,
        "i": 65079,
        "x": 123,
        "y": 456,
    }

    for _input, expected in inputs.items():
        assert resolve_signal(wires, _input) == expected
