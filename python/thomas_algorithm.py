import time

from matrix_tool import print_matrix, print_vector
from check import check_roots


def solve(A, y):
  n = len(A)

  coeff = []
  det = 1
  sigma = 0
  lamb = 0

  for i in xrange(n):
    b = (1. * A[i][i - 1]) if i - 1 >= 0 else 0.
    c = 1. * A[i][i]
    d = (1. * A[i][i + 1]) if i + 1 != n else 0.
    det *= (c + b * sigma)
    sigma, lamb = -d / (c + b * sigma), (y[i][0] - b * lamb) / (c + b * sigma)
    coeff.append((sigma, lamb))

  roots = [lamb]

  for i in xrange(n - 2, -1, -1):
    sigma, lamb = coeff[i]
    roots.insert(0, sigma * roots[0] + lamb)

  return roots, det


def main():
  from constants import A3_21 as A, b3_21 as b
  start_time = time.time()
  x, det = solve(A, b)
  solve_time = time.time()
  print("Roots:")
  print_vector(x)
  check_roots(A, x, b)
  print
  print("Determinant: {}".format(det))

  print("Time elapsed: ")
  print("\tSolution:\t{} ms".format((solve_time - start_time) * 1000))


if __name__ == '__main__':
  main()