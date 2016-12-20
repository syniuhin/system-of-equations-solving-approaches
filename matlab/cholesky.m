A2 = [
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
];

b2 = [
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
];

function U = factorize(A)
  n = size(A, 1);
  U = zeros(n, n);
  for i = 1:n
    U(i, i) = realsqrt(A(i, i) - sum(U(1:i-1, i) .^ 2));
    for j = i+1:n
      U(i, j) = (A(i, j) - sum(U(1:i-1, i) .* U(1:i-1, j))) / U(i, i);
    end;
  end;
end;

function [B, T] = inverse(A, U)
  n = size(U, 1);
  T = zeros(n, n);
  for i = 1:n
    T(i, i) = 1 / U(i, i);
    for j = i+1:n
      T(i, j) = -sum(T(i, 1:j-1) .* U(1:j-1, j)') / U(j, j);
    end;
  end;

  B = zeros(n, n);
  for i = 1:n
    for j = 1:n
      k = min(i, j);
      B(i, j) = sum(T(i, k:n) .* T(j, k:n));
    end;
  end;
end;

tic
U = factorize(A2)
[_, y] = backward_left([U' b2])
[_, x] = backward_right([U y'])
toc
det = determinant(U) ^ 2
[B, T] = inverse(A2, U)
toc
