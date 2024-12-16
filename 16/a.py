import sys
from timeit import timeit

sys.setrecursionlimit(20000)  # 141 * 141 = 19881


lowest_score_seen = {}


def turn_left(direction: complex):
    return direction * 1j


def turn_right(direction: complex):
    return direction * -1j


def solve_maze(
    grid: list[str],
    position: complex,
    end: complex,
    direction: complex,
    path_taken: set[complex],
    score: int = 0,
) -> int | None:
    if position == end:
        return score

    if grid[int(position.real)][int(position.imag)] == "#":
        return None

    if position in path_taken:
        return None

    if position in lowest_score_seen and score >= lowest_score_seen[position]:
        # print(f"Current score {score} greater than or equal to {lowest_score_seen[position]} for position {position}, exiting")
        return None

    else:
        lowest_score_seen[position] = score

    path_taken.add(position)

    # forwards
    score_1 = solve_maze(
        grid=grid,
        position=position + direction,
        end=end,
        direction=direction,
        path_taken=path_taken.copy(),
        score=score + 1,
    )

    # left turn
    left = turn_left(direction)
    score_2 = solve_maze(
        grid=grid,
        position=position + left,
        end=end,
        direction=left,
        path_taken=path_taken.copy(),
        score=score + 1001,
    )

    # right turn
    right = turn_right(direction)
    score_3 = solve_maze(
        grid=grid,
        position=position + right,
        end=end,
        direction=right,
        path_taken=path_taken.copy(),
        score=score + 1001,
    )

    scores = [_ for _ in (score_1, score_2, score_3) if _ is not None]

    if scores:
        score = min(scores)
        return score


def main():
    with open("input.txt") as f:
        grid = f.readlines()

    end = next(
        complex(y, line.index("E")) for y, line in enumerate(grid) if "E" in line
    )
    start = next(
        complex(y, line.index("S")) for y, line in enumerate(grid) if "S" in line
    )

    direction = 0 + 1j

    score = solve_maze(
        grid=grid,
        position=start,
        end=end,
        direction=direction,
        path_taken=set(),
    )
    print(score)


if __name__ == "__main__":
    print(timeit(main, number=1))
    # 96.33373117100018 seconds
