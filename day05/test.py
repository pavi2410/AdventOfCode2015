from .main import part1, part2


def test_part1():
    inputs = {
        "ugknbfddgicrmopn": True,
        "aaa": True,
        "jchzalrnumimnmhp": False,
        "haegwjzuvuyypxyu": False,
        "dvszwmarrgswjxmb": False,
    }

    for _input, expected in inputs.items():
        assert part1(_input) == expected


def test_part2():
    inputs = {
        "qjhvhtzxzqqjkmpb": True,
        "xxyxx": True,
        "uurcxstgmygtbstg": False,
        "ieodomkazucvgmuy": False,
    }

    for _input, expected in inputs.items():
        assert part2(_input) == expected
