import re
import json

regex = re.compile(r"(\d+)\|(\d+)")

page_ordering_rules: tuple[int, int] = []

total = 0

with open("input.txt") as f:
    while line := f.readline():
        if match := regex.match(line):
            page_ordering_rules.append((int(match.group(1)), int(match.group(2))))
        else:
            break
    while line := f.readline():
        update: list[int] = json.loads(f"[{line}]")
        for rule in page_ordering_rules:
            try:
                index = update.index(rule[0])
                if rule[1] in update[:index]:
                    break  # This update breaks the rules, move on to next update
            except ValueError:
                continue  # Rule not broken, go to next rule
        else:  # nobreak
            assert len(update) % 2 == 1
            total += update[(len(update) - 1) // 2]

print(total)
