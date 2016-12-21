from __future__ import print_function

import math
from itertools import product


def eye(n):
  a = [[0] * n for i in xrange(n)]
  for i in xrange(n):
    a[i][i] = 1
  return a


def ones(n, m):
  return [[1] * m for _ in xrange(n)]


def zeros(n, m):
  return [[0] * m for _ in xrange(n)]


def norm(vector):
  return math.sqrt(sum(map(lambda x: x * x, vector)))


def product_with_scalar(matrix, scalar):
  if (len(matrix) == 1):
    return [[item * scalar for item in matrix[0]]]
  else:
    return [[item * scalar for item in row] for row in matrix]


def divide_by_scalar(matrix, scalar):
  if (len(matrix) == 1):
    return [[item * 1. / scalar for item in matrix[0]]]
  else:
    return [[item * 1. / scalar for item in row] for row in matrix]


def get_row(matrix, index):
  return matrix[index]


def get_column(matrix, index):
  return [row[index] for row in matrix]


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


def dot_product(v1, v2):
  return sum(x * y for x, y in zip(v1, v2))


def transpose(matrix):
  if isinstance(matrix[0], (list, tuple)):
    return [get_column(matrix, i) for i in xrange(len(matrix[0]))]
  else:
    return [[i] for i in matrix]


def append_column(A, x):
  S = []
  for i in xrange(len(A)):
    S.append(A[i][:])
    [S[i].append(xj) for xj in x[i]]
  return S


def get_matrix_sum(A, B):
  for i in xrange(len(A)):
    for j in xrange(len(A[0])):
      A[i][j] = A[i][j] + B[i][j]
  return A


def get_matrix_difference(A, B):
  for i in xrange(len(A)):
    for j in xrange(len(A[0])):
      A[i][j] = A[i][j] - B[i][j]
  return A


def print_matrix(A, precision=2, plain=False, round_elem=False):
  for row in A:
    for elem in row:
      if plain:
        print("{: }\t".format(elem), end="")
      elif round_elem:
        print("{: 7.0f} ".format(round(elem)), end="")
      else:
        print("{2: {1}.{0}f} ".format(precision, precision + 5, elem), end="")
    print()


def print_vector(x, **kwargs):
  print_matrix([[xi] for xi in x], **kwargs)
