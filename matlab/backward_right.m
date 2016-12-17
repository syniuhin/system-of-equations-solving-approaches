function [B, x] = backward_right(A)
  n = size(A, 1);
  m = size(A, 2);
  x = [];
  B = A;
  for row = n:-1:1
    x = [(B(row, m) / B(row, row)) x];
    for i = row-1:-1:1
      B(i, :) = B(i, :) - B(row, :) * B(i, row) / B(row, row);
    end;
  end;
end;