from copy import deepcopy


class MatrixError(BaseException):
    def __init__(self, mat1, mat2):
        self.matrix1 = mat1
        self.matrix2 = mat2


class Matrix:
    def __init__(self, m):
        self.nLst = deepcopy(m)

    def __eq__(self, other):
        return self.nLst == other.nLst

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, line)) for line in self.nLst])

    def size(self):
        return len(self.nLst), len(self.nLst[0])

    def __add__(self, other):
        if len(self.nLst) == len(other.nLst):
            resul = []
            for i in range(len(self.nLst)):
                resul.append(map(sum, zip(self.nLst[i], other.nLst[i])))
        else:
            error = MatrixError(self, other)
            raise error
        return Matrix(resul)

    def transpose(self):
        t_mat = list(map(list, zip(*self.nLst)))
        self.nLst = t_mat
        return Matrix(t_mat)

    @staticmethod
    def transposed(self):
        return Matrix(list(map(list, zip(*self.nLst))))

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            resMul = []
            for i in range(len(self.nLst)):
                resMul.append(list(map(lambda x: x * other, self.nLst[i])))
            return Matrix(resMul)
        elif isinstance(other, Matrix) and len(self.nLst[0]) == len(other.nLst):
            temp = Matrix.transposed(other)
            rows = self.size()[0]
            cols = temp.size()[0]
            arr = [[0 for _ in range(cols)] for _ in range(rows)]
            for row in range(rows):
                for col in range(cols):
                    row_x_col = zip(self.nLst[row], temp.nLst[col])
                    arr[row][col] = sum(a * b for a, b in row_x_col)
            return Matrix(arr)
        else:
            error = MatrixError(self, other)
            raise error

    __rmul__ = __mul__


if __name__ == '__main__':
    from sys import stdin
    exec(stdin.read())
