#!/usr/bin/env python
# -*- coding: utf-8 -*-
# this is QR decomposition approach with using Householder reflection

from methods.i.gauss_klassisch import backward_left
from methods.matrix_tool import MathHelper as m
from var30_constants import A1 as A, B1 as B


#Немного теории по поводу нахождения детерминанта
#Так как Q - ортогональная, а L - нижне треугольная, то детерминант матрицы А - произведение детерминантов матриц L * Q
#соответсвенно, где det Q = (-1)^k, k - число рефлексий Хаусхолдера, det L   равен произведению элементов диагонали матрицы (треугольная)
#
#
#Информация, касающаяся поиска обратной матрицы
# inv(A) = inv(L) * inv(Q) = inv(L) * Q' (транспонированая)

def get_determinant(k,L):
    detR = 1
    for i in xrange(len(L)):
        detR *= L[i][i]
    return (-1)**k * detR

def get_invariant(L,Q):
    detL = 1
    for i in xrange(len(L)):
        detL *= L[i][i]
    invL = m.divide_by_scalar(L,detL)
    invQ = m.transpose(Q)
    return m.multiply(invL,invQ)

n = len(A)
Q = m.eye(n)
L = m.multiply(Q,A)

householders_reflections = []
params_matrix_list = [L]

for i in xrange(n-1):
    col = m.transpose([m.get_row(L,i)[i:]])
    H = m.get_householder_reflection_matrix(col)
    if (i != 0):
        for j in xrange(i):
            H = m.extend_householder_matrix(H)
    L = m.multiply(L, H)
    Q = m.multiply(H, Q)
    householders_reflections.append(H)
    params_matrix_list.append(L)

C = []
for i in xrange(len(L)):
    C.append(L[i]+[B[i][0]])

m.show_matrix(C,to_round=True)
y = m.transpose([[backward_left(C, i) for i in xrange(len(C))]])
x = m.multiply(m.transpose(Q),y)
m.show_matrix(x,False)


print "\ndetA = detQ * detL = " + str(get_determinant(len(householders_reflections),L))
print "\ninv(A) = inv(L) * inv(Q) = inv(L) * Q' (транспонированая) = "
m.show_matrix(get_invariant(L,Q),False)

