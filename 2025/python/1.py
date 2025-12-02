


def move(direction, start_pos, steps):
    pos = int(start_pos)
    if direction == 'L':
        pos = pos - int(steps)
        if pos < 0:
            return move(direction, 100, abs(pos))
    elif direction == 'R':
        pos = pos + int(steps)
        if pos > 100:
            return move(direction, 0, pos - 100)
    
    return int(pos)



position = 50
total_zeros = 0

with open('../files/1.txt', 'r') as f:
    for line in f:
        line = line.strip()
        direction = line[:1]
        steps = line[1:]

        position = move(direction, position, steps)
    
        if position == 0 or position == 100:
            total_zeros += 1
        
        if position == 100:
            position = 0
    print("Total zeros:", total_zeros)



print("--------------------------------")
print("Test 1")
res = move('L', 50, 68)
print("res", res)
res = move('L', res, 30)
print("res", res)
res = move('R', res, 48)
print("res", res)
res = move('L', res, 5)
print("res", res)
res = move('R', res, 60)
print("res", res)
res = move('L', res, 55)
print("res", res)
res = move('L', res, 1)
print("res", res)
res = move('L', res, 99)
print("res", res)
res = move('R', res, 14)
print("res", res)
res = move('L', res, 82)
print("res", res)

print("--------------------------------")

res = move('L', 50, 50)
print("res", res)
res = move('R', res, 100)
print("res", res)