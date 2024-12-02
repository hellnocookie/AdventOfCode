import os

current_dir = os.path.dirname(os.path.abspath(__file__))
file = open(os.path.join(current_dir, 'files', '1-1.txt'))

content = file.read().split('\n')
first = content[0]
content.pop(0)
print(first)
count = 0

for line in content:
    if int(line) > int(first):
        count += 1
    first = int(line)

print(count)
