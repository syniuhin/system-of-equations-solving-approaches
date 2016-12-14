import gauss_klassisch as gk
import squared as sq
from check import check


def lu(A):
  n = len(A)
  L = sq.zeros(n, n)
  U = sq.ones(n)
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
  from constants import A2, b2
  n = len(A2)
  L, U = lu(A2)
  y = []
  Lb = gk.append_column(L, b2)
  for row in xrange(n):
    y.append(gk.backward_left(Lb, row))
  Uy = gk.append_column(U, [[e] for e in y])
  x = []
  for row in xrange(n - 1, -1, -1):
    x.append(gk.backward_right(Uy, row))
  x.reverse()
  check(A2, x, b2)
