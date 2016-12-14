from __future__ import print_function
from check import check

def solve(A, b):
  S = append_column(A, b)
  for i in xrange(len(S)):
    forward(S, i)
  roots = []
  for i in xrange(len(S) - 1, -1, -1):
    roots.append(backward_right(S, i))
  roots.reverse()
  print("Roots: {}".format(roots))
  return roots


def forward(A, row):
  a = A[row][row]
  n = len(A)
  m = len(A[row])
  for j in xrange(row, m):
    A[row][j] /= 1. * a
  for i in xrange(row + 1, n):
    ai = A[i][row]
    for j in xrange(row, m):
      A[i][j] -= ai * A[row][j]
  print("Forward for row #{}".format(row))
  print_matrix(A)
  print()


def backward_right(A, row):
  m = len(A[row])
  res = A[row][m-1] * 1. / A[row][row]
  for i in xrange(row-1, -1, -1):
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
  res = A[row][m-1] * 1. / A[row][row]
  for i in xrange(row+1, n):
    ai = A[i][row] * 1. / A[row][row]
    for j in xrange(row+1):
      A[i][j] -= ai * A[row][j]
    A[i][m-1] -= ai * A[row][m-1]
  print("Backward for row #{}".format(row))
  print_matrix(A)
  print()
  return res


def print_matrix(A):
  for row in A:
    for elem in row:
      print("{:.1f}\t".format(elem), end="")
    print()


def append_column(A, x):
  S = []
  for i in xrange(len(A)):
    S.append([])
    S[i] = A[i][:]
    S[i].append(x[i][0])
  return S


def main():
  from constants import A1, b1
  x = solve(A1, b1)
  check(A1, x, b1)
