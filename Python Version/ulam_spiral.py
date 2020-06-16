from sympy import isprime
from math import floor, sqrt

spiralSize = 15  # odd number
centralNumber = 1

matrix = [[[] for col in range(spiralSize)] for row in range(spiralSize)]  # create an empty matrix
x = y = floor(spiralSize / 2)

for n in range(centralNumber, spiralSize ** 2 + centralNumber):
    matrix[y][x] = n if isprime(n) else ''
    move = floor((sqrt(4 * (n - centralNumber) + 1) + 3) % 4 + 1)  # for more information see https://oeis.org/A063826
    if move == 1:
        x += 1  # move to the right
    elif move == 2:
        y -= 1  # move up
    elif move == 3:
        x -= 1  # move to the left
    else:
        y += 1  # move down

for i in range(spiralSize):
    for j in range(spiralSize):
        print(matrix[i][j], end="\t")
    print()
