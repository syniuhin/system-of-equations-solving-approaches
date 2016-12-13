from __future__ import print_function
from check import check
import gauss_klassisch as gk


def solve(A, b, forward_pass=True):
  S = gk.append_column(A, b)
  if forward_pass:
    for i in xrange(len(S)):
      print("Choosing main for iteration #{}".format(i))
      choose_main(S, i)
      gk.forward(S, i)
  roots = []
  for i in xrange(len(S) - 1, -1, -1):
    roots.append(gk.backward(S, i))
  roots.reverse()
  print("Roots: {}".format(roots))
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


A = [
    [188, -32, -9, 7, -61, 49, -53, 23, -31, 62],
    [-32, 101, 11, -32, -80, 1, 53, -7, 94, -109],
    [-9, 11, 231, 96, -62, -12, 72, -40, 72, -77],
    [7, -32, 96, 174, -37, -119, 19, 7, -27, 27],
    [-61, -80, -62, -37, 184, -34, -115, 45, -53, 46],
    [49, 1, -12, -119, -34, 182, 80, -56, -4, 18],
    [-53, 53, 72, 19, -115, 80, 231, -101, 70, -50],
    [23, -7, -40, 7, 45, -56, -101, 227, -10, 23],
    [-31, 94, 72, -27, -53, -4, 70, -10, 241, -155],
    [62, -109, -77, 27, 46, 18, -50, 23, -155, 212],
]

b = [
    [-44],
    [74],
    [87],
    [247],
    [-39],
    [168],
    [192],
    [-199],
    [-194],
    [243],
]

x = solve(A, b)
check(A, x, b)