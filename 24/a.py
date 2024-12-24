import re
from collections import deque


def main():
    states_re = re.compile(r"(\w{3}): ([01])")
    gates_re = re.compile(r"(\w{3}) (\w+) (\w{3}) -> (\w{3})")

    states: dict[str, int] = {}
    instructions: deque[tuple[str, str, str, str]] = deque()

    with open("input.txt") as f:
        while line := f.readline():
            if match := states_re.match(line):
                k, v = match.groups()
                states[k] = int(v)
            else:
                break
        while line := f.readline():
            if match := gates_re.match(line):
                instructions.append(match.groups())

    while instructions:
        instruction = instructions.popleft()
        state1, operator, state2, target = instruction

        if state1 in states and state2 in states:
            match operator:
                case "AND":
                    states[target] = states[state1] and states[state2]
                case "XOR":
                    states[target] = states[state1] ^ states[state2]
                case "OR":
                    states[target] = states[state1] or states[state2]
        else:
            instructions.append(instruction)

    output = ""

    for k, v in sorted((k, v) for k, v in states.items() if k.startswith("z")):
        output = str(v) + output

    print(int(output, 2))


if __name__ == "__main__":
    main()
