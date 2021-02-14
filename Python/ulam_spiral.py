from math import floor, sqrt


def is_prime(num):
    if num > 1:
        for d in range(2, num):
            if num % d == 0:
                return False
        return True
    return False


spiral_size, central_number = 9, 1  # the size of the spiral must be an odd number
matrix = [[[] for col in range(spiral_size)] for row in range(spiral_size)]  # create an empty matrix
x = y = floor(spiral_size / 2)

for n in range(central_number, spiral_size ** 2 + central_number):
    matrix[y][x] = n if is_prime(n) else ''
    move = floor((sqrt(4 * (n - central_number) + 1) + 3) % 4 + 1)  # for more information see https://oeis.org/A063826
    if move == 1:
        x += 1  # move to the right
    elif move == 2:
        y -= 1  # move up
    elif move == 3:
        x -= 1  # move to the left
    else:
        y += 1  # move down

for i in range(spiral_size):
    for j in range(spiral_size):
        print(matrix[i][j], end="\t")
    print()
    
