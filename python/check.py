from matrix_tool import print_vector

def check_roots(A, x, b):
  X = []
  for i in xrange(len(A)):
    X.append(A[i][:])
    for j in xrange(len(A[i])):
      X[i][j] *= x[j]
  ans = [sum(row) for row in X]
  print("Found values:")
  print_vector(ans)
  print("Errors:")
  print_vector([abs(f[0] - s[0]) for (f, s) in zip([[a] for a in ans], b)], plain=True)
