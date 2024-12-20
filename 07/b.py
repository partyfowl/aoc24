import re
from itertools import product
from multiprocessing.pool import Pool
from timeit import timeit


def check_result_recursive(result: int, values: list[int]):
    # Return the result if it is possible to make, else return 0
    value = values.pop(0)

    # If all values have been operated on, return here
    if not values:
        return result if value == result else 0

    # Move on if the current value is greater than result
    # As there are only positive modifiers in use here
    if value > result:
        return 0

    # If there's more values, we need to add/multiply/concat them
    next_value = values.pop(0)

    for operator in ("+", "*", "||"):
        if operator == "+":
            operator_result = value + next_value
        elif operator == "*":
            operator_result = value * next_value
        elif operator == "||":
            operator_result = int(str(value) + str(next_value))

        new_values = [operator_result] + values  # Creates a new list
        if check_result_recursive(result, new_values):
            return result

    return 0


def check_result(result: int, values: list[int]):
    # Return the result if it is possible to make, else return 0
    num_operators = len(values[1:])

    # Ternary format for operators here, where 0 is add, 1 is multiply, 2 is concat
    combinations = [_ for _ in product(("+", "*", "||"), repeat=num_operators)]

    # If the final value is not a factor of the result,
    # then we can eliminate 1/3 of the combinations
    final_operator_can_be_multiplier = (result % values[-1]) == 0
    if not final_operator_can_be_multiplier:
        del combinations[1::3]

    for operators in combinations:
        value = values[0]
        for i in range(num_operators):
            if operators[i] == "+":
                value += values[i + 1]
            elif operators[i] == "*":
                value *= values[i + 1]
            elif operators[i] == "||":
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
        print(sum(p.starmap(check_result_recursive, equations)))


if __name__ == "__main__":
    print(timeit(main, number=1))
