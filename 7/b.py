import re
from multiprocessing.pool import Pool
from timeit import timeit

from numpy import base_repr  # lazy


def check_result(result: int, values: list[int]):
    # Return the result if it is possible to make, else return 0
    num_operators = len(values[1:])

    combinations = [_ for _ in range(pow(3, num_operators))]

    # If the final value is not a factor of the result, 
    # then we can eliminate 1/3 of the combinations
    final_operator_can_be_multiplier = (result % values[-1]) == 0
    if not final_operator_can_be_multiplier:
        del combinations[1::3]

    for combo in combinations:
        value = values[0]
        # Ternary format for operators here, where 0 is add, 1 is multiply, 2 is concat
        operators = base_repr(combo, 3).zfill(num_operators)
        for i in range(num_operators):
            if operators[i] == "0":
                value += values[i + 1]
            elif operators[i] == "1":
                value *= values[i + 1]
            elif operators[i] == "2":
                value = int(str(value) + str(values[i + 1]))

            # Move on if the current value is greater than result
            # As there are only positive modifiers in use here
            if value > result:
                break
        if value == result:
            return result
    return 0


def main():
    result_re = re.compile(r"^(\d+):")
    values_re = re.compile(r" (\d+)")

    equations: list[tuple[int, list[int]]] = []

    with open("input.txt") as f:
        for line in f:
            match = result_re.match(line)
            result = int(match.group(1))
            values = [int(_) for _ in values_re.findall(line, pos=match.end(0))]
            equations.append((result, values))

    with Pool() as p:
        print(sum(p.starmap(check_result, equations)))


if __name__ == "__main__":
    print(timeit(main, number=1))
