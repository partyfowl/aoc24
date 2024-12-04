import re

mul_regex = re.compile(r"mul\((\d+),(\d+)\)")
do_regex = re.compile(r"do\(\).*?don't\(\)", re.DOTALL)

do_chunks = do_regex.findall("do()" + open("input.txt").read() + "don't()")

total = 0

for chunk in do_chunks:
    matches = mul_regex.findall(chunk)

    for x, y in matches:
        total += int(x) * int(y)

print(total)
