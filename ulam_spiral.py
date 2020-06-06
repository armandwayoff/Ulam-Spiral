from math import floor, sqrt

spiralSize = 9  # odd number


def createEmptyMatrix(size):
    m = []
    for i in range(size):
        m.append([])
        for j in range(size):
            m[i].append([])
    return m


def direction(x):  # for more information see https://oeis.org/A063826
    return floor((sqrt(4 * x + 1) + 3) % 4 + 1)


matrix = createEmptyMatrix(spiralSize)

x = y = floor(spiralSize / 2)  # middle of the spiral
matrix[y][x] = 1

for n in range(spiralSize ** 2 - 1):
    if direction(n) == 1:
        x += 1  # move to the right
    elif direction(n) == 2:
        y -= 1  # move up
    elif direction(n) == 3:
        x -= 1  # move to the left
    else:
        y += 1  # move down
    matrix[y][x] = n + 2

for i in range(spiralSize):
    print(matrix[i])
