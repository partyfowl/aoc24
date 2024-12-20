import json
import re

regex = re.compile(r"(\d+)\|(\d+)")

page_ordering_rules: list[tuple[int, int]] = []
updates: list[list[int]] = []

perfect_order = []

total = 0

with open("input.txt") as f:
    while line := f.readline():
        if match := regex.match(line):
            page_ordering_rules.append((int(match.group(1)), int(match.group(2))))
        else:
            break

    while line := f.readline():
        updates.append(json.loads(f"[{line}]"))

bad_updates: list[list[int]] = []

for update in updates:
    for rule in page_ordering_rules:
        try:
            index0 = update.index(rule[0])
            index1 = update[:index0].index(rule[1])

            # This update breaks the rules, let's fix it
            bad_updates.append(update)

            break

        except ValueError:
            continue  # Rule not broken, go to next rule


faults_found = True
while faults_found:
    faults_found = False
    for update in bad_updates:
        for rule in page_ordering_rules:
            try:
                index0 = update.index(rule[0])
                index1 = update[:index0].index(rule[1])
                update[index0], update[index1] = update[index1], update[index0]
                faults_found = True
            except ValueError:
                continue  # Rule not broken, go to next rule

for update in bad_updates:
    assert len(update) % 2 == 1
    total += update[(len(update) - 1) // 2]

print(total)
