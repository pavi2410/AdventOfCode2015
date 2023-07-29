from .main import part1, part2


def test_part1():
    inputs = r"""""
"abc"
"aaa\"aaa"
"\x27"
"""
    assert part1(inputs) == 12


def test_part2():
    inputs = r"""""
"abc"
"aaa\"aaa"
"\x27"
"""

    assert part2(inputs) == 19
