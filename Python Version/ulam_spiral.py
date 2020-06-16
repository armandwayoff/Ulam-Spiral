from sympy import isprime
from math import floor, sqrt

spiralSize = 15  # odd number
centralNumber = 1


def move(x):  # for more information see https://oeis.org/A063826
    return floor((sqrt(4 * x + 1) + 3) % 4 + 1)


matrix = [[[] for col in range(spiralSize)] for row in range(spiralSize)]  # Create an empty matrix
x = y = floor(spiralSize / 2)  # middle of the spiral

for n in range(centralNumber, spiralSize ** 2 + centralNumber):
    matrix[y][x] = n if isprime(n) else ''

    if move(n - centralNumber) == 1:
        x += 1  # move to the right
    elif move(n - centralNumber) == 2:
        y -= 1  # move up
    elif move(n - centralNumber) == 3:
        x -= 1  # move to the left
    else:
        y += 1  # move down


for i in range(len(matrix)):
    for j in range(len(matrix)):
        print(matrix[i][j], end="\t")
    print()
