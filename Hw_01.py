# Задание
# Создайте класс Матрица. Добавьте методы для:
# ○ вывода на печать,
# ○ сравнения,
# ○ сложения,
# ○ *умножения матриц
import random

class Matrix:
    def __init__(self, rows: int = 2, columns: int = 2, matrix: list[list[int]] = None):
        """
        Make matrix with random values or check input matrix
        :param matrix:
        """
        if matrix is None:
            if rows > 1 and columns > 1:
                self.rows = rows
                self.columns = columns
                self.matrix = [[random.randint(0,100) for _ in range(columns)] for _ in range(rows)]
            else:
                raise ValueError
        else:
            if Matrix._check_matrix(matrix):
                self.matrix = matrix
                self.rows = len(matrix)
                self.columns = len(matrix[0])
            else:
                raise ValueError

    @staticmethod
    def _check_matrix(matrix: list[list[int]])->bool:
        return len(set(map(len,matrix))) == 1

    def __eq__(self, other):
        if Matrix._same_size(self, other):
            # return all([all([self.matrix[r][c] == other.matrix[r][c]
            #                 for c in range(self.columns)]) for r in range(self.rows)])
            return all(map(lambda x : x[0] == x[1], zip([c for r in self.matrix for c in r], [c for r in other.matrix for c in r])))
        else:
            raise ValueError

    def __str__(self):
        """
        Make a string of Matrix
        :return:
        """
        return '\n'.join(''.join([f'{x:^5}' for x in row]) for row in self.matrix) + '\n'
        # return '\n'.join(f'{str(row) for row in self.matrix}')

    @staticmethod
    def _same_size(matrix1, matrix2):
        return isinstance(matrix2, Matrix) and matrix1.rows == matrix2.rows and matrix1.columns == matrix2.columns

    def __add__(self, other):
        """
        Add matrixes
        :param other:
        :return:
        """
        if Matrix._same_size(self, other):
            return Matrix(
                matrix=[[self.matrix[i][j] + other.matrix[i][j]
                        for j in range(self.columns)]
                        for i in range(self.rows)]
                        )
        else:
            raise ValueError("Not the same size of Matrixes")

        result = [
            [self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[0]))]
            for i in range(len(self.matrix))
        ]
        return Matrix(result)

    def __mul__(self, other):
        if isinstance(other, Matrix):
            if self.columns == other.rows:
                new_matrix = [[0]* other.columns for _ in range(self.rows)]
                for i in range(self.rows):
                    for j in range(other.columns):
                        for k in range(other.rows):
                            new_matrix[i][j] += self.matrix[i][k] * other.matrix[k][j]
                return Matrix(matrix = new_matrix)
            else:
                raise ValueError
        elif isinstance(other, int | float):
            return Matrix(matrix=[[self.matrix[r][c]* other
                                    for c in range(self.columns)] for r in range(self.rows)])
        else:
            raise ValueError


    # def __mul__(self, other):
    #     # Умножение двух матриц
    #     if len(self.matrix[0]) != len(other.matrix):
    #         raise ValueError("Количество столбцов первой матрицы должно быть равно количеству строк второй матрицы")
    #
    #     result = [
    #         [
    #             sum(self.matrix[i][k] * other.matrix[k][j] for k in range(len(self.matrix[0])))
    #             for j in range(len(other.matrix[0]))
    #         ]
    #         for i in range(len(self.matrix))
    #     ]
    #     return Matrix(result)
matrix = None
a = Matrix()
b = Matrix(4, 5)
c = Matrix(matrix =[[1,2,3],[4,5,6],[7,8,9]])
d = Matrix(matrix =[[1,2,3],[4,5,6],[7,8,9]])

print(a)
print(b)
print(c)
print(c==d)
print(c+d)

e = c*d
print(e)