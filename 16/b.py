import sys
from collections import defaultdict
from timeit import timeit

sys.setrecursionlimit(20000)  # 141 * 141 = 19881


lowest_score_seen = {}
good_seats = defaultdict(set)


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
    max_score: int,
    score: int = 0,
) -> int | None:
    if score > max_score:
        return None
    if position in path_taken:
        return None

    path_taken.add(position)

    if position == end:
        good_seats[score].update(path_taken)
        return score

    if grid[int(position.real)][int(position.imag)] == "#":
        return None

    directional_position = (position, direction)
    if (
        directional_position in lowest_score_seen
        and score > lowest_score_seen[directional_position]
    ):
        # print(
        #     f"Current score {score} greater than {lowest_score_seen[directional_position]} for directional position {directional_position}, exiting"
        # )
        return None

    else:
        lowest_score_seen[directional_position] = score

    # forwards
    score_1 = solve_maze(
        grid=grid,
        position=position + direction,
        end=end,
        direction=direction,
        path_taken=path_taken.copy(),
        max_score=max_score,
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
        max_score=max_score,
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
        max_score=max_score,
        score=score + 1001,
    )

    scores = [_ for _ in (score_1, score_2, score_3) if _ is not None]

    return min(scores) if scores else None


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
        max_score=93436,  # part 1 answer
        path_taken=set(),
    )
    print(len(good_seats[score]))


if __name__ == "__main__":
    print(timeit(main, number=1))
    # 40.12468759700005 seconds
