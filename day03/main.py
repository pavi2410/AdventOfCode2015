def solve(_input: str):
    visited = set[tuple[int, int]]()
    x = 0
    y = 0
    visited.add((x, y))
    for c in _input:
        match c:
            case "^":
                y += 1
            case "v":
                y -= 1
            case ">":
                x += 1
            case "<":
                x -= 1
            case _:
                pass
        visited.add((x, y))
    return visited


def part1(_input: str) -> int:
    visited = solve(_input)

    return len(visited)


def part2(_input: str) -> int:
    santa_visited = solve(_input[::2])  # even
    robo_santa_visited = solve(_input[1::2])  # odd

    visited = santa_visited | robo_santa_visited

    return len(visited)


if __name__ == "__main__":
    import os

    input_file = os.path.join(os.path.dirname(__file__), "input.txt")
    with open(input_file) as f:
        _input = f.read()
        print("Part 1 answer:", part1(_input))
        print("Part 2 answer:", part2(_input))
