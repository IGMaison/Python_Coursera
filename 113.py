from sys import stdin
import copy


class Matrix:
    def __init__(self, m):
        self.list = copy.deepcopy(m)

    def __str__(self):
        rez = str()
        for i in self.list:
            for j in i:
                rez = rez + str(j) + "\t"
            rez = rez.strip() + "\n"
        rez = rez.strip()
        return rez

    def size(self):
        return len(self.list), len(self.list[0])

    def __add__(self, other):
        if len(self.list) != len(other.list) or \
                len(self.list[0]) != len(other.list[0]):
            raise MatrixError(self, other)
        else:
            newMatrix = []
            tempMatrix = []
            for i in range(len(self.list)):
                for j in range(len(self.list[i])):
                    tempMatrix.append(self.list[i][j] + other.list[i][j])
                newMatrix.append(tempMatrix)
                tempMatrix = []
            return Matrix(newMatrix)

    def __mul__(self, other):
        newMatrix = []
        for i in range(len(self.list)):
            tempMatrix = []
            for j in range(len(self.list[i])):
                tempMatrix.append(self.list[i][j] * other)
            newMatrix.append(tempMatrix)
        return Matrix(newMatrix)

    __rmul__ = __mul__

    def transpose(self):
        self.list = Matrix.transposed(self).list
        return self

    @staticmethod
    def transposed(matrix):
        return Matrix(list(zip(*matrix.list)))


class MatrixError(BaseException):

    def __init__(self, matrix1, matrix2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2


exec(stdin.read())



# Добавьте в программу из предыдущей задачи класс MatrixError, содержащий
# внутри self поля matrix1 и matrix2 — ссылки на матрицы.
#
# В класс Matrix внесите следующие изменения:
#
#     Добавьте в метод __add__ проверку на ошибки в размере входных данных,
# чтобы при попытке сложить матрицы разных размеров было выброшено исключение
# MatrixError таким образом, чтобы matrix1 поле MatrixError стало первым
# аргументом __add__ (просто self), а matrix2 — вторым (второй операнд для
# сложения).
#
#     Реализуйте метод transpose, транспонирующий матрицу и возвращающую
# результат (данный метод модифицирует экземпляр класса Matrix)
#
#     Реализуйте статический метод transposed, принимающий Matrix и
# возвращающий транспонированную матрицу. Пример статического метода.

# Входные данные:
# Task 3 check 1
# Check exception to add method
# m1 = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
# m2 = Matrix([[0, 1, 0], [20, 0, -1], [-1, -2, 0]])
# print(m1 + m2)
#
# m2 = Matrix([[0, 1, 0], [20, 0, -1]])
# try:
#     m = m1 + m2
#     print('WA\n' + str(m))
# except MatrixError as e:
#     print(e.matrix1)
#     print(e.matrix2)
#
# Вывод программы:
# 1	1	0
# 20	1	-1
# -1	-2	1
# 1	0	0
# 0	1	0
# 0	0	1
# 0	1	0
# 20	0	-1