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
];

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
];

function swap_rows(A, l, r)
  tmp = A(l, :);
  A(l, :) = A(r, :);
  A(r, :) = tmp;
end;

function [B, p] = forward_colmain(A)
  n = size(A, 1);
  B = A;
  p = 0;
  for row = 1:n
    [_, mrow] = max(B(row:n, row));
    mrow = mrow + row - 1
    if mrow ~= row
      disp(sprintf('Swapping %d and %d\n', row, mrow));
      p = p + 1;
      B([row, mrow], :) = B([mrow, row], :);
    end;
    B(row, :) = B(row, :) ./ B(row, row);
    for i = row+1:n
      B(i, :) = B(i, :) - B(row, :) * B(i, row);
    end;
    B
  end;
end;


tic
S = [A b]
[S, p] = forward_colmain(S);
[B, x] = backward_right(S);
B
x
toc

T = triangalize(A)
det = determinant(T) * (-1)^p
