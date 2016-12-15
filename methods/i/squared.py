from __future__ import print_function
from math import sqrt
import gauss_klassisch as gk
from check import check


def solve(A, b):
  n = len(A)
  U = getU(A)
  gk.print_matrix(U)
  Ut = transpose(U)

  y = []
  Utb = gk.append_column(Ut, b)
  for row in xrange(n):
    y.append(gk.backward_left(Utb, row))
  Uy = gk.append_column(U, [[e] for e in y])
  x = []
  for row in xrange(n - 1, -1, -1):
    x.append(gk.backward_right(Uy, row))
  x.reverse()
  return x, U


# Ut * U = A => det(U)^2 = det(A)
def determinant(U):
  det = 1.
  for i in xrange(len(U)):
    det *= U[i][i]
  return det**2


def inverse(A, U):
  # T = U^-1
  n = len(U)
  T = zeros(n, n)
  for i in xrange(n):
    T[i][i] = 1. / U[i][i]
    for j in xrange(i+1, n):
      for k in xrange(j):
        T[i][j] -= T[i][k] * U[k][j]
      T[i][j] /= U[j][j]

  B = zeros(n, n)
  for i in xrange(n):
    for j in xrange(n):
      for k in xrange(min(i, j), n):
        B[i][j] += T[i][k] * T[j][k]
  return B


def zeros(n, m):
  return [[0.] * m for _ in xrange(n)]


def ones(n):
  res = zeros(n, n)
  for i in xrange(len(res)):
    res[i][i] = 1
  return res


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


def main():
  from constants import A2, b2
  x, U = solve(A2, b2)
  check(A2, x, b2)
  det = determinant(U)
  print()
  print("Determinant: {}".format(det))
  print()
  inversed = inverse(A2, U)
  print("Inverse matrix:")
  gk.print_matrix_precise(inversed)
