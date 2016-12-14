from __future__ import print_function
from check import check
import gauss_klassisch as gk


def solve(A, b):
  S = gk.append_column(A, b)
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
  from constants import A2, b2
  x = solve(A2, b2)
  print("Roots: {}".format(x))
  check(A2, x, b2)
  det = gk.determinant(A2)
  print("Determinant: {}".format(det))
