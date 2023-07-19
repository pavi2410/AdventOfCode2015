from .main import part1, part2


def test_part1():
    inputs = {
        "turn on 0,0 through 999,999": 1000000,
        "toggle 0,0 through 999,0": 1000,
        "turn off 499,499 through 500,500": 0,
    }

    for _input, expected in inputs.items():
        assert part1(_input) == expected


def test_part2():
    inputs = {
        "turn on 0,0 through 0,0": 1,
        "toggle 0,0 through 999,999": 2000000,
    }

    for _input, expected in inputs.items():
        assert part2(_input) == expected
