import re

file = open("/app/2024/files/1.txt")

left = []
right = []
for line in file:
    numbers = re.findall(r'\d+', line)
    left.append(numbers[0])
    right.append(numbers[1])

occurrences = {}
for n in right:
    if n in occurrences:
        occurrences[n] = occurrences[n] + 1
    else:
        occurrences[n] = 1

sum = 0
for n in left:
    sum += int(n) * int(occurrences.get(n, 0))

print("Result: ", sum)
