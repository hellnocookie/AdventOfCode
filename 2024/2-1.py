import re

file = open("/app/2024/files/2.txt")

def compare(no1: int, no2: int, increase: bool = True) -> bool:
    return ((no1 > no2 and not increase) or (no1 < no2 and increase)) and 1 <= abs(no1 - no2) <= 3

reports = []
for line in file:
    level = re.findall(r'\d+', line)
    safe = True

    increase = True
    if int(level[0]) > int(level[1]):
        increase = False
    elif int(level[0]) == int(level[1]):
        continue
    for n in range(0, len(level) - 1):
        if not compare(int(level[n]), int(level[n+1]), increase):
            safe = False
            break
    if safe:
        reports.append(level)

print("Result: ", len(reports))


