#!/usr/bin/env python
# -*- coding: utf-8 -*-
# this is QR decomposition approach with using Householder reflection

from methods.i.gauss_klassisch import backward_right
from methods.matrix_tool import MathHelper as m
from var30_constants import A1 as A, B1 as B

# Немного теории по поводу нахождения детерминанта
# Так как Q - ортогональная, а R - верхняя треугольная, то детерминант матрицы А - произведение детерминантов матриц Q *  R
# соответсвенно, где det Q = (-1)^k, k - число рефлексий Хаусхолдера, det R равен произведению элементов диагонали матрицы (треугольная)
#
#
# Информация, касающаяся поиска обратной матрицы
# inv(A) = inv(R) * inv(Q) = inv(R) * Q' (транспонированая)

def get_determinant(k, R):
    detR = 1
    for i in xrange(len(R)):
        detR *= R[i][i]
    return (-1) ** k * detR


def get_invariant(Q, R):
    detR = 1
    for i in xrange(len(R)):
        detR *= R[i][i]
    invR = m.divide_by_scalar(R, detR)
    invQ = m.transpose(Q)
    return m.multiply(invR, invQ)

n = len(A)
Q = m.eye(n)
R = A
householders_reflections = []
params_matrix_list = [R]

for i in xrange(n - 1):
    col = m.transpose([m.get_column(R, i)[i:]])
    H = m.get_householder_reflection_matrix(col)
    if (i != 0):
        for j in xrange(i):
            H = m.extend_householder_matrix(H)
    R = m.multiply(H, R)
    Q = m.multiply(Q, H)
    householders_reflections.append(H)
    params_matrix_list.append(R)

y = m.multiply(m.transpose(Q), B)
y = m.transpose(y)
m.show_matrix(R, True)
C = []
for i in xrange(len(R)):
    C.append(R[i] + [y[0][i]])

x = [backward_right(C, i) for i in xrange(len(C) - 1, -1, -1)]
x.reverse()
x = m.transpose([x])
m.show_matrix(x,False)
print "\ndetA = detQ * detR = " + str(get_determinant(len(householders_reflections),R))
print "\ninv(A) = inv(R) * inv(Q) = inv(R) * Q' (транспонированая) = "
m.show_matrix(get_invariant(Q,R),False)
