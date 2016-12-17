function det = determinant(A)
  n = size(A, 1);
  det = 1;
  for row = 1:n
    det = det * A(row, row);
  end;
end;