import math
size = 5  # odd number
x = y = math.floor(size / 2)


def createEmptyMatrix(s):
    m = []
    for i in range(s):
        m.append([])
        for j in range(s):
            m[i].append([])
    return m


def a(n):
    return math.floor((math.sqrt(4 * n + 1) + 3) % 4 + 1)


matrix = createEmptyMatrix(size)
for i in range(size):
    print(matrix[i])
moves = []

for n in range(size ** 2):
    if a(n) == 1:
        x += 1
    elif a(n) == 2:
        y -= 1
    elif a(n) == 3:
        x -= 1
    else:
        y += 1
    matrix[y][x].append(n + 1)
    moves.append(a(n))

print(moves)
for i in range(size):
    print(matrix[i])
