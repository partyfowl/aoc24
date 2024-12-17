import re


def parse() -> tuple[int, int, int, list[int]]:
    regex = re.compile(
        r"Register A: (\d+)\nRegister B: (\d+)\nRegister C: (\d+)\n+Program: (\d(?:,\d+)*)"
    )

    with open("input.txt") as f:
        abc = regex.match(f.read())

    a, b, c = [int(_) for _ in abc.group(1, 2, 3)]
    instructions = [int(_) for _ in abc.group(4).split(",")]

    return a, b, c, instructions


def process_instructions(
    a: int, b: int, c: int, instructions: list[int]
) -> tuple[int, int, int, str]:
    i = 0

    output = []

    while i < len(instructions):
        goto: int | None = None
        try:
            instruction, literal = instructions[i : i + 2]
        except ValueError:
            break

        if literal == 4:
            combo = a
        elif literal == 5:
            combo = b
        elif literal == 6:
            combo = c
        else:
            combo = literal

        if instruction == 0:  # adv
            a //= 2**combo
        elif instruction == 1:  # bxl
            b ^= literal
        elif instruction == 2:  # bst
            b = combo % 8
        elif instruction == 3:  # jnz
            if a != 0:
                goto = literal
        elif instruction == 4:
            b ^= c
        elif instruction == 5:
            output.append(str(combo % 8))
        elif instruction == 6:
            b = a // 2**combo
        elif instruction == 7:
            c = a // 2**combo

        if goto is None:
            i += 2
        else:
            i = goto
    return a, b, c, ",".join(output)
