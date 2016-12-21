import time 

from matrix_tool import divide_by_scalar, transpose, multiply, eye, get_column,\
print_matrix, print_vector, append_column, norm, product_with_scalar, get_matrix_difference
from check import check_roots

from gauss_klassisch import forward, backward_right
from cholesky import inverse_triangle_right


def solve(Q, R, b):
  y = multiply(transpose(Q), b)
  C = append_column(R, y)

  x = [backward_right(C, i) for i in xrange(len(C) - 1, -1, -1)]
  x.reverse()
  return x

def decompose(A):
  n = len(A)
  Q = eye(n)
  R = A
  householders_reflections = []

  for i in xrange(n - 1):
    col = transpose([get_column(R, i)[i:]])
    H = get_householder_reflection_matrix(col)
    if (i != 0):
      for j in xrange(i):
        H = extend_householder_matrix(H)
    R = multiply(H, R)
    print("Iteration #{}".format(i + 1))
    print_matrix(R)
    print
    Q = multiply(Q, H)
    householders_reflections.append(H)
  return Q, R, householders_reflections


def determinant(k, R):
  detR = 1
  for i in xrange(len(R)):
    detR *= R[i][i]
  return (-1) ** k * detR


def inverse(Q, R):
  invR = inverse_triangle_right(R)
  invQ = transpose(Q)
  return multiply(invR, invQ)


def check_feasibility(A):
  print('Check if we can use QR on this matrix')
  S = []
  for row in A:
    S.append(row[:])
  for row in xrange(len(S)):
    forward(S, row)
    if S[row][row] == 0.:
      print('!!!BUSTED!!!')
      return False
  return True


def get_householder_reflection_vector(vector):
  res = vector[0][:]
  res[0] = res[0] + norm(res) if (res[0] > 0) else res[0] - norm(res)
  return [res]


def get_householder_reflection_matrix(column):
  a = transpose(column)
  param = 2.0 / (norm(get_householder_reflection_vector(a)[0])**2)
  u = [get_householder_reflection_vector(a)[0]]
  w = product_with_scalar(multiply(transpose(u), u), param)
  H = get_matrix_difference(eye(len(column)), w)
  return H


def extend_householder_matrix(matrix):
  n = len(matrix)
  first_row = [0 for _ in xrange(n + 1)]
  first_row[0] = 1
  for i in matrix:
    i.insert(0, 0)
  matrix.insert(0, first_row)
  return matrix


def main():
  from constants import A1_21 as A, b1_21 as b

  start_time = time.time()
  if not check_feasibility(A):
    print("Matrix has rank of {}, good to go!".format(len(A)))
  check_time = time.time()
  Q, R, hr = decompose(A)
  decomp_time = time.time()
  x = solve(Q, R, b)
  solve_time = time.time()
  print("Roots:")
  print_vector(x, precision=8)
  check_roots(A, x, b)
  det = determinant(len(hr), R)
  det_time = time.time()
  print
  print("Determinant: {}".format(det))
  print
  inversed = inverse(Q, R)
  inverse_time = time.time()
  print("Inverse matrix:")
  print_matrix(inversed, precision=8)
  print("Check inverse matrix:")
  print_matrix(multiply(inversed, A))

  print("Time elapsed: ")
  print(
      "\tSolution:\t{} ms\n\tDeterminant:\t{} ms\n\tInversion:\t{} ms\n\tOverall:\t{} ms".
      format((solve_time - check_time) * 1000, (det_time - solve_time) * 1000, (
          inverse_time - det_time) * 1000, (inverse_time - start_time) * 1000))

if __name__ == '__main__':
    main()