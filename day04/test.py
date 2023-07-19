from .main import part1, part2


def test_part1():
    inputs = {
        "abcdef": 609043,
        "pqrstuv": 1048970
    }

    for _input, expected in inputs.items():
        assert part1(_input) == expected


def test_part2():
    inputs = {
        "abcdef": 609043,
        "pqrstuv": 1048970
    }

    for _input, expected in inputs.items():
        assert part2(_input) == expected
