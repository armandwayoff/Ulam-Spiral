import sys
import sympy
from math import floor, sqrt

spiralSize = 17  # odd number
centralNumber = 1  # strictly positive


def createEmptyMatrix(size):
    m = []
    for i in range(size):
        m.append([])
        for j in range(size):
            m[i].append([])
    return m


def move(x):  # for more information see https://oeis.org/A063826
    return floor((sqrt(4 * x + 1) + 3) % 4 + 1)


if spiralSize % 2 == 1 and centralNumber >= 1:
    matrix = createEmptyMatrix(spiralSize)
else:
    sys.exit("Error")

x = y = floor(spiralSize / 2)  # middle of the spiral

for n in range(centralNumber, spiralSize ** 2 + centralNumber):
    if sympy.isprime(n):
        matrix[y][x] = '⭕'
    else:
        matrix[y][x] = ''
    if move(n - centralNumber) == 1:
        x += 1  # move to the right
    elif move(n - centralNumber) == 2:
        y -= 1  # move up
    elif move(n - centralNumber) == 3:
        x -= 1  # move to the left
    else:
        y += 1  # move down

# Formatting
s = [[str(e) for e in row] for row in matrix]
lens = [max(map(len, col)) for col in zip(*s)]
fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
table = [fmt.format(*row) for row in s]
print('\n'.join(table))
