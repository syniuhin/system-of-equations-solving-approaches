def check(A, x, b):
  X = []
  for i in xrange(len(A)):
    X.append(A[i][:])
    for j in xrange(len(A[i])):
      X[i][j] *= x[j]
  ans = [0] * len(X)
  for i in xrange(len(X)):
    ans[i] = sum(X[i])
  print("Found:\t{}".format(ans))
  print("Errors:\t{}".format([abs(f[0]-s[0]) for (f, s) in zip([[a] for a in ans], b)]))