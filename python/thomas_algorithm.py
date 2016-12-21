import time

from matrix_tool import print_vector, print_matrix
from check import check_roots

EPS = 5e-10


def solve(A, y):

  n = len(A)

  coeff = []
  det = 1
  alpha = 0
  beta = 0

  for i in xrange(n):
    b = (1. * A[i][i - 1]) if i - 1 >= 0 else 0.
    c = 1. * A[i][i]
    d = (1. * A[i][i + 1]) if i + 1 != n else 0.
    # Correctness check
    if abs(c + b * alpha) < EPS:
      print("Correctness failed")
      raise ValueError()
    det *= (c + b * alpha)
    alpha, beta = -d / (c + b * alpha), (y[i][0] - b * beta) / (c + b * alpha)
    # Stability check
    if abs(alpha) - 1. > EPS:
      print("UNSTABLE")
    coeff.append((alpha, beta))

  print("  alpha\t  beta")
  print_matrix([[a, b] for a, b in coeff])
  roots = [beta]

  for i in xrange(n - 2, -1, -1):
    alpha, beta = coeff[i]
    roots.insert(0, alpha * roots[0] + beta)

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