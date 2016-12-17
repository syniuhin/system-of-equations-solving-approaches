function [B, x] = backward_left(A)
  n = size(A, 1);
  m = size(A, 2);
  x = [];
  B = A;
  for row = 1:n
    x = [x (B(row, m) / B(row, row))];
    for i = row+1:n
      B(i, :) = B(i, :) - B(row, :) * B(i, row) / B(row, row);
    end;
  end;
end;