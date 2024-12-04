import re
from src.SortAlgo import SortAlgo

file = open("/app/2024/files/1.txt")
contents = file.read().split("\n")

left = []
right = []

for line in contents:
    numbers = re.findall(r'\d+', line)
    left.append(numbers[0])
    right.append(numbers[1])

left = SortAlgo.quick_sort(left)
right = SortAlgo.quick_sort(right)

sum = 0
for n in range(0, len(left)):
    sum += abs(int(right[n]) - int(left[n]))
    print(abs(int(right[n]) - int(left[n])))

print("Result: ", sum)