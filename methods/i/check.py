def check(A, x, b):
  X = []
  for i in xrange(len(A)):
    X.append(A[i][:])
    for j in xrange(len(A[i])):
      X[i][j] *= x[j]
  ans = [sum(row) for row in X]
  print("Found:\t{}".format(ans))
  print("Errors:\t{}".format([abs(f[0]-s[0]) for (f, s) in zip([[a] for a in ans], b)]))