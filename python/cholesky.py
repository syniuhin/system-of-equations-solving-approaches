from __future__ import print_function
import time

from math import sqrt
from matrix_tool import zeros, print_vector, print_matrix, append_column, multiply
import gauss_klassisch as gk
from check import check_roots


def solve(A, b):
  n = len(A)
  U = getU(A)
  print_matrix(U)
  Ut = transpose(U)

  y = []
  Utb = append_column(Ut, b)
  for row in xrange(n):
    y.append(gk.backward_left(Utb, row))
  print(y)
  Uy = append_column(U, [[e] for e in y])
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


def inverse_triangle_right(U):
  # T = U^-1
  n = len(U)
  T = zeros(n, n)
  for i in xrange(n):
    T[i][i] = 1. / U[i][i]
    for j in xrange(i + 1, n):
      for k in xrange(j):
        T[i][j] -= T[i][k] * U[k][j]
      T[i][j] /= U[j][j]
  return T


def inverse(A, U):
  n = len(U)
  T = inverse_triangle_right(U)
  print
  print("U^-1:")
  print_matrix(T)
  print("Check U^-1:")
  print_matrix(multiply(T, U))
  B = zeros(n, n)
  for i in xrange(n):
    for j in xrange(n):
      for k in xrange(min(i, j), n):
        B[i][j] += T[i][k] * T[j][k]
  return B


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


def main():
  from constants import A2_21 as A, b2_21 as b
  start_time = time.time()
  x, U = solve(A, b)
  solve_time = time.time()
  print("Roots:")
  print_vector(x)
  check_roots(A, x, b)
  det = determinant(U)
  det_time = time.time()
  print()
  print("Determinant: {}".format(det))
  print()
  inversed = inverse(A, U)
  inverse_time = time.time()
  print("Inverse matrix:")
  print_matrix(inversed, precision=8)
  print("Check inverse matrix:")
  print_matrix(multiply(inversed, A))

  print("Time elapsed: ")
  print(
      "\tSolution:\t{} ms\n\tDeterminant:\t{} ms\n\tInversion:\t{} ms\n\tOverall:\t{} ms".
      format((solve_time - start_time) * 1000, (det_time - solve_time) * 1000, (
          inverse_time - det_time) * 1000, (inverse_time - start_time) * 1000))


if __name__ == '__main__':
  main()
