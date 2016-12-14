# this is QR decomposition approach with using Householder reflection

from methods.i.gauss_klassisch import backward
from methods.matrix_tool import MathHelper as m
#
# A = [
#         [-27,    -93,   -74,    -45,     67,    74,    17,   96,   -36  ],
#         [  59,    79,   -66,     45,    -90,    20,   -58,  -61,   -62  ],
#         [  73,   -82,   -1,      9,     -79,   -27,    40,   26,    52  ],
#         [ -39,    91,   -95,     80,     52,   -26,   -14,  -10,   -42, ],
#         [ -23,   -64,   -10,     61,    -33,   -98    -28,   12,    22, ],
#         [  17,    45,    23,     58,     27,   -27,   -78,   99,   -64, ],
#         [ -39,    27,     6,    -66,     87,    32,   -15,  -36,    82, ],
#         [  89,    40,   -17,    -44,    -29,   -31,    55,  -52,     3, ],
#         [  81,   -60,    86,     42,     43,    29,    95,  -70,   -26, ],
# ]
#
# B = [
#         [ 43 ],
#         [ 84 ],
#         [ -7 ],
#         [ -38 ],
#         [ -59 ],
#         [ 93 ],
#         [ -5 ],
#         [ 73 ],
#         [ -10 ],
# ]

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

B = [[-44],
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

A = [[1, 2, 3], [0, 3, 2], [2, 0, 1]]
n = len(A)
B = [[6], [7], [8]]
X = m.ones(n, 1)
print A
Q = m.eye(n)
R = A
householders_reflections = []
params_matrix_list = [R]

for i in xrange(n - 1):
    print 1
    col = m.transpose([m.get_column(R, i)[i:]])
    h_i = m.get_householder_reflection_matrix(col, len(col))
    if (i != 0):
        h_i = m.extend_householder_matrix(h_i)
    R = m.multiply(h_i, params_matrix_list[0])
    householders_reflections.append(h_i)
    params_matrix_list.insert(0, R)

for i in householders_reflections:
    Q = m.multiply(Q, i)

R = m.get_triangle_matrix(R)
y = m.multiply(m.transpose(Q), B)
y = m.transpose(y)

for i in xrange(len(R)):
    R[i].append(y[0][i])

roots = [backward(R, i) for i in xrange(len(R) - 1, -1, -1)]
roots.reverse()

print m.multiply(A, m.transpose([roots]))
