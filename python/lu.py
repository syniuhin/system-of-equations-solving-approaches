import time

from matrix_tool import append_column, print_matrix, print_vector, eye, zeros
import gauss_klassisch as gk
from check import check_roots

def solve(A, b):
  n = len(A)
  L, U = lu(A)
  y = []
  Lb = append_column(L, b)
  for row in xrange(n):
    y.append(gk.backward_left(Lb, row))
  Uy = append_column(U, [[e] for e in y])
  x = []
  for row in xrange(n - 1, -1, -1):
    x.append(gk.backward_right(Uy, row))
  x.reverse()
  return x

def lu(A):
  n = len(A)
  L = zeros(n, n)
  U = eye(n)
  for i in xrange(n):
    for j in xrange(0, i + 1):
      L[i][j] = A[i][j]
      for k in xrange(j):
        L[i][j] -= U[k][j] * L[i][k]
    for j in xrange(i + 1, n):
      U[i][j] = A[i][j]
      for k in xrange(i):
        U[i][j] -= U[k][j] * L[i][k]
      U[i][j] /= 1. * L[i][i]
  return L, U


def main():
  from constants import A2_21 as A, b2_21 as b
  start_time = time.time()
  x = solve(A, b)
  solve_time = time.time()
  print("Roots:")
  print_vector(x)
  check_roots(A, x, b)
  print("Time elapsed: ")
  print("\tSolution:\t{} ms".format((solve_time - start_time) * 1000))

if __name__ == '__main__':
  main()
