import numpy as np


def part1(_input: str) -> int:
    grid = np.zeros((1000, 1000), dtype=np.int8)
    for line in _input.splitlines():
        if line.startswith("turn on"):
            _, _, start, _, end = line.split()
            x1, y1 = map(int, start.split(","))
            x2, y2 = map(int, end.split(","))
            grid[x1:x2 + 1, y1:y2 + 1] = 1
        elif line.startswith("turn off"):
            _, _, start, _, end = line.split()
            x1, y1 = map(int, start.split(","))
            x2, y2 = map(int, end.split(","))
            grid[x1:x2 + 1, y1:y2 + 1] = 0
        elif line.startswith("toggle"):
            _, start, _, end = line.split()
            x1, y1 = map(int, start.split(","))
            x2, y2 = map(int, end.split(","))
            grid[x1:x2 + 1, y1:y2 + 1] = 1 - grid[x1:x2 + 1, y1:y2 + 1]
    return grid.sum()


def part2(_input: str) -> int:
    grid = np.zeros((1000, 1000), dtype=np.int8)
    for line in _input.splitlines():
        if line.startswith("turn on"):
            _, _, start, _, end = line.split()
            x1, y1 = map(int, start.split(","))
            x2, y2 = map(int, end.split(","))
            grid[x1:x2 + 1, y1:y2 + 1] += 1
        elif line.startswith("turn off"):
            _, _, start, _, end = line.split()
            x1, y1 = map(int, start.split(","))
            x2, y2 = map(int, end.split(","))
            grid[x1:x2 + 1, y1:y2 + 1] = np.maximum(grid[x1:x2 + 1, y1:y2 + 1] - 1, 0)
        elif line.startswith("toggle"):
            _, start, _, end = line.split()
            x1, y1 = map(int, start.split(","))
            x2, y2 = map(int, end.split(","))
            grid[x1:x2 + 1, y1:y2 + 1] += 2
    return grid.sum()


if __name__ == "__main__":
    import os

    input_file = os.path.join(os.path.dirname(__file__), "input.txt")
    with open(input_file) as f:
        _input = f.read()
        print("Part 1 answer:", part1(_input))
        print("Part 2 answer:", part2(_input))
