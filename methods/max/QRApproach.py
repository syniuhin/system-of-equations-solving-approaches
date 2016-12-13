#this is QR decomposition approach with using Householder reflection

from matrix_tool import MathHelper as m

a = [[1,0,2]]
b = [[2,3,5],[7,8,9]]

res =  m.transpose(b)

# print m.norm(a[0])
print m.get_householder_reflection_matrix(m.transpose(a),len(a[0]))



