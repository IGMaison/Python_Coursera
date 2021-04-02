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
        tempMatrix = []
        for i in range(len(self.list)):
            for j in range(len(self.list[i])):
                tempMatrix.append(self.list[i][j] * other)
            newMatrix.append(tempMatrix)
            tempMatrix = []
        return Matrix(newMatrix)

    __rmul__ = __mul__


exec(stdin.read())

#
# Добавьте в предыдущий класс следующие методы:
#
#     __add__, принимающий вторую матрицу того же размера и возвращающий сумму матриц.
#
#     __mul__, принимающий число типа int или float и возвращающий матрицу, умноженную на скаляр.
#
#     __rmul__, делающий то же самое, что и __mul__. Этот метод будет вызван в том случае, аргумент
# находится справа. Для реализации этого метода в коде класса достаточно написать __rmul__ = __mul__.
