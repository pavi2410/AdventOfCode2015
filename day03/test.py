from .main import part1, part2


def test_part1():
    inputs = {
        ">": 2,
        "^>v<": 4,
        "^v^v^v^v^v": 2
    }

    for _input, expected in inputs.items():
        assert part1(_input) == expected


def test_part2():
    inputs = {
        "^>": 3,
        "^>v<": 3,
        "^v^v^v^v^v": 11
    }

    for _input, expected in inputs.items():
        assert part2(_input) == expected
