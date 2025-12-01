import re

with open("/app/2024/files/3.txt") as file:
    result = 0
    enabled = True
    for line in file:
        found = re.findall(r'\b(?:do\(\)|don\'t\(\)|mul\(\d+,\d+\))', line)
        for command in found:
            # print(command)
            if command == "don't()":
                enabled = False
            elif command == "do()":
                enabled = True
            else:
                if enabled:
                    numbers = re.findall(r'\d+', command)
                    result += int(numbers[0]) * int(numbers[1])

print("Result: ", result)