A = [
        [1, 2, 3]
        [0, 3, 2]
        [2, 0, 1]
    ];

B = [6;7;8];
n = size(A,1);
Q = eye(n);
R = A;

u = @(x) houseHolderVector(x);
hs_m = @(x) houseHolderMatrix(x);
extend = @(x) extend_householder(x);

ind = 0;
for i = 1:1:(n-1)
      a_i = R(i:size(R,1),i);
      val = u(a_i);
      H = hs_m(val);
      if (ind ~= 0)
          for j = 1:1:ind
            H = extend(H);
          end
      end
      R = H * R;
      Q = Q * H;
      ind = ind + 1;
end;
disp(R);
y = Q' * R;
disp(y);

%determinant
disp((-1)^ind*prod(diag(R)));

%inv
disp(inv(R)*Q')
