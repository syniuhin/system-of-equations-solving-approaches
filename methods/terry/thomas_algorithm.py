A = [
    [1, 2, 0, 0],
    [2, -1, 1, 0],
    [0, 1, -1, 1],
    [0, 0, 1, 1]
]

y = [
    [5],
    [3],
    [3],
    [7]
]


def solve(A, y):
    n = len(A)

    sigma = -1. * A[0][1] / A[0][0]
    lamb = 1. * y[0][0] / A[0][0]
    coeff = [(sigma, lamb)]

    for i in xrange(1, n - 1):
        b = A[i][i - 1]
        c = A[i][i]
        d = A[i][i + 1]
        sigma, lamb = -d / (c + b * sigma), (y[i][0] - b * lamb) / (c + b * sigma)
        coeff.append((sigma, lamb))

    xn = (y[n - 1][0] - A[n - 1][n - 2] * lamb) / \
                       (A[n - 1][n - 1] + A[n - 1][n - 2] * sigma)
    roots = [xn]
    for i in xrange(n - 2, -1, -1):
        sigma, lamb = coeff[i]
        xn = sigma * xn + lamb
        roots.insert(0, xn)

    return roots

print solve(A, y)