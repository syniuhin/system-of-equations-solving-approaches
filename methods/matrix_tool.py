import math
from itertools import product

class MathHelper:

    @staticmethod
    def eye(n):
        a = [[0] * n for i in xrange(n)]
        for i in xrange(n):
            a[i][i] = 1
        return a

    @staticmethod
    def ones(n,m):
        return [[1] * m for _ in xrange (n)]

    @staticmethod
    def zeros(n,m):
        return [[0] * m for _ in xrange(n)]

    @staticmethod
    def norm(vector):
        return math.sqrt(sum(map(lambda x: x*x,vector)))

    @staticmethod
    def sum(vector):
        return sum(vector)

    @staticmethod
    def product_with_scalar(matrix, scalar):
        if (len(matrix)==1):
            return [[item * scalar for item in matrix[0]]]
        else:
            return [[item*scalar for item in row] for row in matrix]
    @staticmethod
    def divide_by_scalar(matrix, scalar):
        if (len(matrix)==1):
            return [[item * 1. / scalar  for item in matrix[0]]]
        else:
            return [[item * 1. / scalar for item in row] for row in matrix]

    @staticmethod
    def get_row(matrix, index):
        return matrix[index]

    @staticmethod
    def get_column(matrix, index):
        return [row[index] for row in matrix]

    @staticmethod
    def multiply(A, B):

        # #Product condition is wrong
        if len(A[0]) != len(B):
            raise Exception

        #TODO: B vector has one column case
        rows, cols = len(B), len(B[0])
        resRows = xrange(len(A))
        rMatrix = [[0] * cols for _ in resRows]
        for idx in resRows:
            for j, k in product(xrange(cols), xrange(rows)):
                rMatrix[idx][j] += A[idx][k] * B[k][j]
        return rMatrix

    @staticmethod
    def dot_product(v1, v2):
        return sum(x * y for x, y in zip(v1, v2))

    @staticmethod
    def transpose(matrix):
        if isinstance(matrix[0], (list, tuple)):
            return [MathHelper.get_column(matrix, i) for i in xrange(len(matrix[0]))]
        else:
            return [[i] for i in matrix]



    @staticmethod
    def get_householder_reflection_vector(vector):
        res = [item for item in vector[0]]
        res[0] = res[0] + MathHelper.norm(res) \
                                if (res[0] > 0) \
                                else res[0] - MathHelper.norm(res)
        return [res]

    @staticmethod
    def get_matrix_sum(A,B):
        for i in xrange(len(A)):
            for j in xrange(len(A[0])):
                A[i][j] = A[i][j] + B[i][j]
        return A

    @staticmethod
    def get_matrix_difference(A, B):
        for i in xrange(len(A)):
            for j in xrange(len(A[0])):
                A[i][j] = A[i][j] - B[i][j]
        return A

    @staticmethod
    def get_householder_reflection_matrix(column):
        a = MathHelper.transpose(column)
        param = 2.0/(MathHelper.norm(MathHelper.get_householder_reflection_vector(a)[0]) ** 2)
        u = [MathHelper.get_householder_reflection_vector(a)[0]]
        w = MathHelper.product_with_scalar(MathHelper.multiply(MathHelper.transpose(u),u), param)
        H = MathHelper.get_matrix_difference(MathHelper.eye(len(column)),w)
        return H

    @staticmethod
    def extend_householder_matrix(matrix):
        n = len(matrix)
        first_row = [0 for _ in xrange(n+1)]
        first_row[0] = 1
        for i in matrix:
            i.insert(0,0)
        matrix.insert(0,first_row)
        return matrix

    @staticmethod
    def show_matrix(A, to_round):
        for row in A:
            print [round((i)) for i in row] if to_round else row