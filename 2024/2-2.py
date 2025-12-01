import re

file = open("/app/2024/files/2.txt")

def compare(no1: int, no2: int, increase: bool = True) -> bool:
    result = ((no1 > no2 and not increase) or (no1 < no2 and increase)) and 1 <= abs(no1 - no2) <= 3
    return result

reports = []
for line in file:
    level = re.findall(r'\d+', line)
    safe = True
    increase = int(level[0]) < int(level[1])

    for n in range(0, len(level) - 1):
        if not compare(int(level[n]), int(level[n+1]), increase):
            safe = False
            break

    if not safe:
        for m in range(0, len(level)):
            check_level = list(map(int, level[:m] + level[m+1:]))
            increase = int(check_level[0]) < int(check_level[1])
            safe = True
            for n in range(0, len(check_level) - 1):
                if not compare(int(check_level[n]), int(check_level[n + 1]), increase):
                    safe = False
                    break
            if safe:
                break
    if safe:
        reports.append(level)

print("Result: ", len(reports))


