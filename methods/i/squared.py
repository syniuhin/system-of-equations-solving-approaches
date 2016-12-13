from __future__ import print_function
from math import sqrt
import gauss_klassisch as gk
from check import check

def zeros(n, m):
  return [[0.] * m for _ in xrange(n)]


def getU(A):
  n = len(A)
  m = len(A[0])
  # TODO: Use util for this
  U = [[0.] * m for _ in xrange(n)]
  for i in xrange(n):
    # Plus here to preserve float
    U[i][i] += A[i][i]
    for k in xrange(i - 1, -1, -1):
      U[i][i] -= U[k][i] * U[k][i]
    U[i][i] = sqrt(U[i][i])
    for j in xrange(i + 1, m):
      # Plus here to preserve float
      U[i][j] += A[i][j]
      for k in xrange(i - 1, -1, -1):
        U[i][j] -= U[k][i] * U[k][j]
      U[i][j] /= U[i][i]
  return U


def transpose(U):
  n = len(U)
  m = len(U[0])
  Ut = zeros(m, n)
  for i in xrange(n):
    for j in xrange(m):
      Ut[j][i] = U[i][j]
  return Ut


def mul(A, B):
  n, m, k = len(A), len(A[0]), len(B[0])
  C = zeros(n, k)
  for i in xrange(n):
    for j in xrange(k):
      for d in xrange(m):
        C[i][j] += A[i][d] * B[d][j]
  return C


A = [
    [188, -32, -9, 7, -61, 49, -53, 23, -31, 62],
    [-32, 101, 11, -32, -80, 1, 53, -7, 94, -109],
    [-9, 11, 231, 96, -62, -12, 72, -40, 72, -77],
    [7, -32, 96, 174, -37, -119, 19, 7, -27, 27],
    [-61, -80, -62, -37, 184, -34, -115, 45, -53, 46],
    [49, 1, -12, -119, -34, 182, 80, -56, -4, 18],
    [-53, 53, 72, 19, -115, 80, 231, -101, 70, -50],
    [23, -7, -40, 7, 45, -56, -101, 227, -10, 23],
    [-31, 94, 72, -27, -53, -4, 70, -10, 241, -155],
    [62, -109, -77, 27, 46, 18, -50, 23, -155, 212],
]

b = [
    [-44],
    [74],
    [87],
    [247],
    [-39],
    [168],
    [192],
    [-199],
    [-194],
    [243],
]

U = getU(A)
gk.print_matrix(U)
Ut = transpose(U)

y = gk.solve(Ut, b)
x = gk.solve(U, [[e] for e in y], forward_pass=False)

check(A, x, b)
