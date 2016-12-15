function B = forward(A)
  n = size(A, 1);
  B = A;
  for row = 1:n
    B(row, :) = B(row, :) ./ B(row, row);
    for i = row+1:n
      B(i, :) = B(i, :) - B(row, :) * B(i, row);
    end;
  end;
end;