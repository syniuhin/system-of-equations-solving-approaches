from __future__ import print_function
from check import check

def solve(A, b, forward_pass=True):
  S = append_column(A, b)
  if forward_pass:
    for i in xrange(len(S)):
      forward(S, i)
  roots = []
  for i in xrange(len(S) - 1, -1, -1):
    roots.append(backward(S, i))
  roots.reverse()
  print("Roots: {}".format(roots))
  return roots


def forward(matrix, row):
  a = matrix[row][row]
  n = len(matrix)
  m = len(matrix[row])
  for j in xrange(row, m):
    matrix[row][j] /= 1. * a
  for i in xrange(row + 1, n):
    ai = matrix[i][row]
    for j in xrange(row, m):
      matrix[i][j] -= ai * matrix[row][j]
  print("Forward for row #{}".format(row))
  print_matrix(matrix)
  print()


def backward(matrix, row):
  m = len(matrix[row])
  res = matrix[row][m-1] / matrix[row][row]
  for i in xrange(row-1, -1, -1):
    ai = matrix[i][row] / matrix[row][row]
    for j in xrange(row, m):
      matrix[i][j] -= ai * matrix[row][j]
  print("Backward for row #{}".format(row))
  print_matrix(matrix)
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
  A = [
    [ 26,    65,   -32,   -35,    91,    70,    27,   -96,    25],
    [-55,    88,   -11,    71,   -15,   -18,   -10,    29,   -46],
    [-69,    12,   -78,    52,   -93,   -77,   -95,     3,   -20],
    [-86,   -11,   -60,   -83,    -1,   -39,    54,    13,    41],
    [-61,   -22,    99,   -56,   -64,   -79,   -46,    53,   -58],
    [ 41,   -46,   -18,    84,    69,    38,   -71,   -84,   -26],
    [ 87,   -14,   -60,    40,    12,    13,   -58,   -18,   -50],
    [ 93,   -91,    65,   -85,   -26,   -12,    91,     4,    58],
    [ 33,   -34,   -75,   -72,   -66,    15,    84,    11,   -72],
  ]

  b = [
    [-69],
    [  1],
    [-45],
    [-79],
    [-97],
    [-72],
    [ 87],
    [ 44],
    [-15],
  ]

  x = solve(A, b)
  check(A, x, b)

main()