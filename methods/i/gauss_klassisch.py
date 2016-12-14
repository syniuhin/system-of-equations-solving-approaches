from __future__ import print_function
from check import check
from squared import ones


def solve(A, b):
  S = append_column(A, b)
  for i in xrange(len(S)):
    forward(S, i)
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
  I = ones(n)
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


def print_matrix(A):
  for row in A:
    for elem in row:
      print("{: 7.2f} ".format(elem), end="")
    print()


def print_matrix_precise(A):
  for row in A:
    for elem in row:
      print("{:9.6f}\t".format(elem), end="")
    print()


def append_column(A, x):
  S = []
  for i in xrange(len(A)):
    S.append(A[i][:])
    [S[i].append(xj) for xj in x[i]]
  return S


def main():
  from constants import A1, b1
  x = solve(A1, b1)
  print("Roots: {}".format(x))
  check(A1, x, b1)
  det = determinant(A1)
  print()
  print("Determinant: {}".format(det))
  print()
  inversed = inverse(A1)
  print("Inverse matrix:")
  print_matrix_precise(inversed)
