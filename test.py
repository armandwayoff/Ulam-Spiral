def createEmptyMatrix(size):
    m = []
    for i in range(size):
        m.append([])
        for j in range(size):
            m[i].append([])
    return m


def rotateMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(len(matrix)):
        for j in range(int(len(matrix) / 2)):
            matrix[i][j], matrix[i][len(matrix) - 1 - j] = matrix[i][len(matrix) - 1 - j], matrix[i][j]
    return matrix


def fillMatrix(matrix):
    n, size = 1, len(matrix)
    for i in range(size):
        matrix[0][i].append(n)
        n += 1
    rotateMatrix(matrix)
    for rotation in range(2 * size - 1):
        for i in range(1, size):
            matrix[0][i].append(n)
            n += 1
        for i in range(1, size - rotation + 1):
            matrix[0][i].append(n)
            n += 1
        rotateMatrix(matrix)
    return matrix


Matrix = createEmptyMatrix(3)
print(fillMatrix(Matrix))
