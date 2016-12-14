#!/usr/bin/env python
# -*- coding: utf-8 -*-
# this is QR decomposition approach with using Householder reflection

from methods.i.gauss_klassisch import backward_right
from methods.matrix_tool import MathHelper as m

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


#Немного теории по поводу нахождения детерминанта
#Так как Q - ортогональная, а R - верхняя треугольная, то детерминант матрицы А - произведение детерминантов матриц Q *  R
#соответсвенно, где det Q = (-1)^k, k - число рефлексий Хаусхолдера, det R равен произведению элементов диагонали матрицы (треугольная)
#
#
#Информация, касающаяся поиска обратной матрицы
# inv(A) = inv(R) * inv(Q) = inv(R) * Q' (транспонированая)

def get_determinant(k,R):
    detR = 1
    for i in xrange(len(R)):
        detR *= R[i][i]
    return (-1)**k * detR

def get_invariant(Q,R):
    detR = 1
    for i in xrange(len(R)):
        detR *= R[i][i]
    print detR
    invR = m.divide_by_scalar(R,detR)
    print invR
    invQ = m.transpose(Q)
    return m.multiply(invR,invQ)



n = len(A)
Q = m.eye(n)
R = A
householders_reflections = []
params_matrix_list = [R]

for i in xrange(n-1):
    col = m.transpose([m.get_column(R, i)[i:]])
    h_i = m.get_householder_reflection_matrix(col)
    if (i != 0):
        for j in xrange(i):
            h_i = m.extend_householder_matrix(h_i)
    print params_matrix_list[0]
    R = m.multiply(h_i, params_matrix_list[0])
    householders_reflections.append(h_i)
    params_matrix_list.insert(0, R)
#
for i in householders_reflections:
    Q = m.multiply(Q, i)

R = m.get_triangle_matrix(R)
y = m.multiply(m.transpose(Q), b)
y = m.transpose(y)

C = []
for i in xrange(len(R)):
    C.append(R[i]+[y[0][i]])


roots = [backward_right(C, i) for i in xrange(len(C) - 1, -1, -1)]
roots.reverse()

print m.multiply(A, m.transpose([roots]))
print "\ndetA = detQ * detR = " + str(get_determinant(len(householders_reflections),R))
print "\ninv(A) = inv(R) * inv(Q) = inv(R) * Q' (транспонированая) = "
m.show_matrix(get_invariant(Q,R))
