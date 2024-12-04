import re

with open("/app/2024/files/3.txt") as file:
    result = 0
    for line in file:
        mul = re.findall(r'mul\(\d+,\d+\)', line)
        for i in mul:
            numbers = re.findall(r'\d+', i)
            result += int(numbers[0]) * int(numbers[1])

print("Result: ", result)