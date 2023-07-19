from .main import part1, part2


def test_part1():
    inputs = {
        "2x3x4": 58,
        "1x1x10": 43
    }

    for _input, expected in inputs.items():
        assert part1(_input) == expected


def test_part2():
    inputs = {
        "2x3x4": 34,
        "1x1x10": 14
    }

    for _input, expected in inputs.items():
        assert part2(_input) == expected
