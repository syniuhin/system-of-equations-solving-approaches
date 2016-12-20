#!/usr/bin/env python
# -*- coding: utf-8 -*-
# this is QR decomposition approach with using Householder reflection

from gauss_klassisch import backward_left
from matrix_tool import divide_by_scalar, transpose, multiply, eye, multiply, \
get_householder_reflection_matrix, extend_householder_matrix, print_matrix, get_row, zeros

from check import check_roots

#Немного теории по поводу нахождения детерминанта
#Так как Q - ортогональная, а L - нижне треугольная, то детерминант матрицы А - произведение детерминантов матриц L * Q
#соответсвенно, где det Q = (-1)^k, k - число рефлексий Хаусхолдера, det L   равен произведению элементов диагонали матрицы (треугольная)
#
#
#Информация, касающаяся поиска обратной матрицы
# inv(A) = inv(L) * inv(Q) = inv(L) * Q' (транспонированая)


def get_determinant(k, L):
  detR = 1
  for i in xrange(len(L)):
    detR *= L[i][i]
  return (-1)**k * detR


def get_invariant(L, Q):
  invL = inverse_triangle_left(L)
  invQ = transpose(Q)
  return multiply(invQ, invL)


def inverse_triangle_left(L):
  n = len(L)
  T = zeros(n, n)
  for i in xrange(n-1, -1, -1):
    T[i][i] = 1. / L[i][i]
    for j in xrange(i-1, -1, -1):
      for k in xrange(n-1, j, -1):
        T[i][j] -= T[i][k] * L[k][j]
      T[i][j] /= L[j][j]
  return T


from constants import A1_30 as A, B1_30 as B
n = len(A)
Q = eye(n)
L = multiply(Q, A)

householders_reflections = []
params_matrix_list = [L]

for i in xrange(n - 1):
  col = transpose([get_row(L, i)[i:]])
  H = get_householder_reflection_matrix(col)
  if (i != 0):
    for j in xrange(i):
      H = extend_householder_matrix(H)
  L = multiply(L, H)
  Q = multiply(H, Q)
  householders_reflections.append(H)
  params_matrix_list.append(L)

C = []
for i in xrange(len(L)):
  C.append(L[i] + [B[i][0]])

print_matrix(C, round_elem=True)
y = transpose([[backward_left(C, i) for i in xrange(len(C))]])
x = multiply(transpose(Q), y)
print_matrix(x)

check_roots(A, [xi[0] for xi in x], B)

print "\ndetA = detQ * detL = " + str(
    get_determinant(len(householders_reflections), L))
print "\ninv(A) = inv(L) * inv(Q) = inv(L) * Q' (транспонированая) = "
inversed = get_invariant(L, Q)
print_matrix(inversed)
print("Check inverse matrix:")
print_matrix(multiply(inversed, A))
