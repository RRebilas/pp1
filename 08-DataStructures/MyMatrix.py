from random import randint


class matrix():

    @staticmethod
    def create(x, y):
        return [[0 for a in range(x)] for b in range(y)]

    @staticmethod
    def create_unit(x):
        m = matrix.create(x, x)
        index = 0
        for i in m:
            i[index] = 1
            index += 1
        return m

    @staticmethod
    def print(matrix):
        for row in matrix:
            print(row)

    @staticmethod
    def fill_random(matrix, m, n):
        for i in matrix:
            for j in range(len(i)):
                i[j] = randint(m, n)
        return matrix

    @staticmethod
    def transpose(matrix):
        # Iterate through columns
        return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]


m = matrix.create(3, 5)
matrix.fill_random(m, 1, 9)
matrix.print(m)
print()
m = matrix.transpose(m)
matrix.print(m)