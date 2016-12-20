import time

from matrix_tool import print_matrix, print_vector, append_column, multiply
from check import check_roots
import gauss_klassisch as gk


def solve(A, b):
  S = append_column(A, b)
  for i in xrange(len(S)):
    print("Choosing main for iteration #{}".format(i))
    choose_main(S, i)
    gk.forward(S, i)
  roots = []
  for i in xrange(len(S) - 1, -1, -1):
    roots.append(gk.backward_right(S, i))
  roots.reverse()
  return roots


def swap_rows(A, lhs, rhs):
  row = A[lhs][:]
  A[lhs] = A[rhs]
  A[rhs] = row


def choose_main(A, row):
  max_elem, max_row = A[row][row], row
  for i in xrange(row + 1, len(A)):
    if A[i][row] > max_elem:
      max_elem, max_row = A[i][i], i
  if max_row != row:
    print("Swapping {} and {}".format(row, max_row))
    swap_rows(A, row, max_row)
  else:
    print("No swap, good to go!")


def main():
  from constants import A2_21 as A, b2_21 as b
  start_time = time.time()
  x = solve(A, b)
  solve_time = time.time()
  print("Roots:")
  print_vector(x)
  check_roots(A, x, b)
  det = gk.determinant(A)
  det_time = time.time()
  print
  print("Determinant: {}".format(det))
  print
  inversed = gk.inverse(A)
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