from .main import part1


def test_part1():
    inputs = {
        "(())": 0,
        "()()": 0,
        "(((": 3,
        "(()(()(": 3,
        "))(((((": 3,
        "())": -1,
        "))(": -1,
        ")))": -3,
        ")())())": -3
    }

    for _input, expected in inputs.items():
        assert part1(_input) == expected
