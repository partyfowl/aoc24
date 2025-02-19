import re


def check_result(result: int, values: list[int]):
    # Return the result if it is possible to make, else return 0
    num_operators = len(values[1:])
    combinations = pow(2, num_operators)
    for combo in range(combinations):
        value = values[0]
        # Binary format for operators here, where 0 is add, 1 is multiply
        operators = "{0:b}".format(combo).zfill(num_operators)
        for i in range(num_operators):
            if operators[i] == "0":
                value += values[i + 1]
            elif operators[i] == "1":
                value *= values[i + 1]
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

    total = 0

    for result, values in equations:
        total += check_result(result, values)

    print(total)


if __name__ == "__main__":
    main()
