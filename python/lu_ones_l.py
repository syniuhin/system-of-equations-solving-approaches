from pprint import pprint
import matrix_tool  as m
from gauss_klassisch import backward_right, backward_left

def pivotize(m):
    """Creates the pivoting matrix for m."""
    n = len(m)
    ID = [[float(i == j) for i in xrange(n)] for j in xrange(n)]
    print ID
    for j in xrange(n):
        row = max(xrange(j, n), key=lambda i: abs(m[i][j]))
        print row
        if j != row:
            ID[j], ID[row] = ID[row], ID[j]
    print ID
    return ID


def get_det(U):
    det = 1
    for i in xrange(len(U)):
        det *= U[i][i]
    return det

def get_inv(L,U):
    detL, detU = 1, 1
    for i in xrange(len(U)):
        detL *= L[i][i]
        detU *= U[i][i]
    invL = m.divide_by_scalar(m.transpose(L),detL)
    invu = m.divide_by_scalar(m.transpose(U),detU)
    return m.multiply(invu,invL)

def lu(A):
    """Decomposes a nxn matrix A by PA=LU and returns L, U and P."""
    n = len(A)
    L = [[0.0] * n for i in xrange(n)]
    U = [[0.0] * n for i in xrange(n)]
    P = pivotize(A)
    A2 = m.multiply(P, A)
    for j in xrange(n):
        L[j][j] = 1.0
        for i in xrange(j + 1):
            s1 = sum(U[k][j] * L[i][k] for k in xrange(i))
            U[i][j] = A2[i][j] - s1
        for i in xrange(j, n):
            s2 = sum(U[k][j] * L[i][k] for k in xrange(j))
            L[i][j] = (A2[i][j] - s2) / U[j][j]
    return L, U, P

from var30_constants import A1 as A, B1 as B
L, U, P = lu(A)

D = m.multiply(P,B)
C = []
for i in xrange(len(L)):
    C.append(L[i]+[D[i][0]])
m.print_matrix(C)
y = m.transpose([[backward_left(C, i) for i in xrange(len(C))]])

C = []
for i in xrange(len(U)):
    C.append(U[i]+[y[i][0]])
x = [backward_right(C, i) for i in xrange(len(C) - 1, -1, -1)]
x.reverse()


m.print_matrix(m.multiply(A,m.transpose(x)))
m.print_matrix((get_inv(L,U)))

