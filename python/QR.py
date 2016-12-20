#!/ur/bin/env python
# -*- coding: utf-8 -*-
# this is QR decomposition approach with using Householder reflection

import time 

from matrix_tool import divide_by_scalar, transpose, multiply, eye, get_column,\
extend_householder_matrix, get_householder_reflection_matrix, \
print_matrix, print_vector
from check import check_roots

from gauss_klassisch import backward_right
from cholesky import inverse_triangle_right


def solve(Q, R, b):
  y = multiply(transpose(Q), b)
  y = transpose(y)
  print_matrix(R, round_elem=True)
  C = []
  for i in xrange(len(R)):
    C.append(R[i] + [y[0][i]])

  x = [backward_right(C, i) for i in xrange(len(C) - 1, -1, -1)]
  x.reverse()
  return x

def decompose(A):
  n = len(A)
  Q = eye(n)
  R = A
  householders_reflections = []
  params_matrix_list = [R]

  for i in xrange(n - 1):
    col = transpose([get_column(R, i)[i:]])
    H = get_householder_reflection_matrix(col)
    if (i != 0):
      for j in xrange(i):
        H = extend_householder_matrix(H)
    R = multiply(H, R)
    Q = multiply(Q, H)
    householders_reflections.append(H)
    params_matrix_list.append(R)
  return Q, R, householders_reflections


# Немного теории по поводу нахождения детерминанта
# Так как Q - ортогональная, а R - верхняя треугольная, то детерминант матрицы А - произведение детерминантов матриц Q *  R
# соответсвенно, где det Q = (-1)^k, k - число рефлексий Хаусхолдера, det R равен произведению элементов диагонали матрицы (треугольная)
#
#
# Информация, касающаяся поиска обратной матрицы
# inv(A) = inv(R) * inv(Q) = inv(R) * Q' (транспонированая)

def determinant(k, R):
  detR = 1
  for i in xrange(len(R)):
    detR *= R[i][i]
  return (-1) ** k * detR


def inverse(Q, R):
  invR = inverse_triangle_right(R)
  invQ = transpose(Q)
  return multiply(invR, invQ)


def main():
  from constants import A1_30 as A, B1_30 as b

  start_time = time.time()
  Q, R, hr = decompose(A)
  decomp_time = time.time()
  x = solve(Q, R, b)
  solve_time = time.time()
  print("Roots:")
  print_vector(x)
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
      format((solve_time - start_time) * 1000, (det_time - solve_time) * 1000, (
          inverse_time - det_time) * 1000, (inverse_time - start_time) * 1000))

if __name__ == '__main__':
    main()