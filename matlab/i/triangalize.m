function B = triangalize(A)
  n = size(A, 1);
  B = A;
  for row = 1:n-1
    for i = row+1:n
      B(i, :) = B(i, :) - B(row, :) * B(i, row) / B(row, row);
    end;
  end;
end;