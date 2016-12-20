from __future__ import print_function
import time

from matrix_tool import print_matrix, print_vector, eye, append_column, multiply
from check import check_roots


def solve(A, b):
  S = append_column(A, b)
  for i in xrange(len(S)):
    forward(S, i, verbose=False)
    if S[i][i] == 0.:
      print('!!!BUSTED!!!')
      return None

  roots = []
  for i in xrange(len(S) - 1, -1, -1):
    roots.append(backward_right(S, i))
  roots.reverse()
  return roots


def forward(A, row, verbose=True):
  a = A[row][row]
  n = len(A)
  m = len(A[row])
  for j in xrange(row, m):
    A[row][j] /= 1. * a
  for i in xrange(row + 1, n):
    ai = A[i][row]
    for j in xrange(row, m):
      A[i][j] -= ai * A[row][j]
  if verbose:
    print("Forward for row #{}".format(row))
    print_matrix(A)
    print()


def backward_right(A, row):
  m = len(A[row])
  res = A[row][m - 1] * 1. / A[row][row]
  for i in xrange(row - 1, -1, -1):
    ai = A[i][row] * 1. / A[row][row]
    for j in xrange(row, m):
      A[i][j] -= ai * A[row][j]
  print("Backward for row #{}".format(row))
  print_matrix(A)
  print()
  return res


def backward_left(A, row):
  n = len(A)
  m = len(A[row])
  res = A[row][m - 1] * 1. / A[row][row]
  for i in xrange(row + 1, n):
    ai = A[i][row] * 1. / A[row][row]
    for j in xrange(row + 1):
      A[i][j] -= ai * A[row][j]
    A[i][m - 1] -= ai * A[row][m - 1]
  print("Backward for row #{}".format(row))
  print_matrix(A)
  print()
  return res


def triangalize(A0):
  n = len(A0)
  m = len(A0[0])
  A = []
  for row in xrange(n):
    A.append(A0[row][:])
  for row in xrange(n):
    a0 = A[row][row]
    for i in xrange(row + 1, n):
      ai = A[i][row]
      for j in xrange(row, m):
        A[i][j] -= ai * A[row][j] / a0
  return A


def determinant(A):
  tr = triangalize(A)
  print("Triangalized matrix:")
  print_matrix(tr)
  det = 1.
  for i in xrange(len(tr)):
    det *= tr[i][i]
  return det


def inverse(A):
  n = len(A)
  m = len(A[0])
  I = eye(n)
  AE = append_column(A, I)
  for row in xrange(n):
    forward(AE, row, verbose=False)
  print("Forward pass:")
  print_matrix(AE)
  print()
  # 'Inverse' forward
  for row in xrange(n - 1, -1, -1):
    for i in xrange(row - 1, -1, -1):
      ai = AE[i][row] * 1. / AE[row][row]
      for j in xrange(row, len(AE[row])):
        AE[i][j] -= ai * AE[row][j]
  print("Backward pass:")
  print_matrix(AE)
  print()
  E = []
  for i in xrange(n):
    E.append(AE[i][n:])
  return E


def main():
  from constants import A1_21 as A, b1_21 as b
  start_time = time.time()
  x = solve(A, b)
  if x is None:
    return
  solve_time = time.time()
  print("Roots:")
  print_vector(x, precision=8)
  check_roots(A, x, b)
  det = determinant(A)
  det_time = time.time()
  print()
  print("Determinant: {}".format(det))
  print()
  inversed = inverse(A)
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
