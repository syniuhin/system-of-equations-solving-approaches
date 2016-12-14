# this is QR decomposition approach with using Householder reflection

from methods.i.gauss_klassisch import backward
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



n = len(A)
Q = m.eye(n)
R = A
householders_reflections = []
params_matrix_list = [R]

for i in xrange(n-1):
    col = m.transpose([m.get_column(R, i)[i:]])
    h_i = m.get_householder_reflection_matrix(col)
    print len(h_i)
    if (i != 0):
        for j in xrange(i):
            h_i = m.extend_householder_matrix(h_i)
    print params_matrix_list[0]
    R = m.multiply(h_i, params_matrix_list[0])
    householders_reflections.append(h_i)
    params_matrix_list.insert(0, R)
    print
    print
#
for i in householders_reflections:
    Q = m.multiply(Q, i)

R = m.get_triangle_matrix(R)
y = m.multiply(m.transpose(Q), b)
y = m.transpose(y)

for i in xrange(len(R)):
    R[i].append(y[0][i])

roots = [backward(R, i) for i in xrange(len(R) - 1, -1, -1)]
roots.reverse()


print m.multiply(A, m.transpose([roots]))
