A = [
    [5, -1, 0, 0],
    [2, 4.6, -1, 0],
    [0, 2, 3.6, -0.8],
    [0, 0, 3, 4.4]
]

y = [
    [2],
    [3.3],
    [2.6],
    [7.2]
]


def solve(A, y):
    n = len(A)

    coeff =[]
    det = 1
    sigma = 0
    lamb = 0

    for i in xrange(n):
        b = (1. * A[i][i - 1]) if i - 1 >= 0 else 0.
        c = 1. * A[i][i]
        d = (1. * A[i][i + 1]) if i + 1 != n else 0.
        det *= (c + b * sigma)
        sigma, lamb = -d / (c + b * sigma), (y[i][0] - b * lamb) / (c + b * sigma)
        coeff.append((sigma, lamb))

    roots = [lamb]

    for i in xrange(n - 2, -1, -1):
        sigma, lamb = coeff[i]
        roots.insert(0, sigma * roots[0] + lamb)

    return roots, det

if __name__ == '__main__':
    x, det = solve(A, y)
    print x
    print det