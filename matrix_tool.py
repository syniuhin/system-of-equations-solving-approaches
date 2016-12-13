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
        return [item*scalar for item in matrix]

    @staticmethod
    def divide_by_scalar(matrix, scalar):
        return [item * 1. / scalar for item in matrix]

    @staticmethod
    def multiply(A, B):

        #Product condition is wrong
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