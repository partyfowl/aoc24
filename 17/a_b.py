from common import parse, process_instructions


def main():
    a, b, c, instructions = parse()

    result = ",".join(str(_) for _ in process_instructions(a, b, c, instructions)[-1])

    print("Part 1:", result)

    a = 1

    len_instructions = len(instructions)

    while instructions != (output := process_instructions(a, b, c, instructions)[-1]):
        if len_instructions > len(output):
            # This adds a digit every multiple of 8
            a *= 8
        else:
            for i in range(len_instructions-1, -1, -1):
                if instructions[i] != output[i]:
                    # Use the fact that the digits correlate to base 8 to our advantage here
                    a += 8 ** i
                    break

    print("Part 2:", a)


if __name__ == "__main__":
    main()
