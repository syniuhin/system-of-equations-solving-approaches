A = [
    [26, 65, -32, -35, 91, 70, 27, -96, 25],
    [-55, 88, -11, 71, -15, -18, -10, 29, -46],
    [-69, 12, -78, 52, -93, -77, -95, 3, -20],
    [-86, -11, -60, -83, -1, -39, 54, 13, 41],
    [-61, -22, 99, -56, -64, -79, -46, 53, -58],
    [41, -46, -18, 84, 69, 38, -71, -84, -26],
    [87, -14, -60, 40, 12, 13, -58, -18, -50],
    [93, -91, 65, -85, -26, -12, 91, 4, 58],
    [33, -34, -75, -72, -66, 15, 84, 11, -72],
];

b = [
    [-69],
    [1],
    [-45],
    [-79],
    [-97],
    [-72],
    [87],
    [44],
    [-15],
];

tic
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

[_, x] = backward_right([R (Q' * b)])

%determinant
disp('The determinant of A matrix equals');
disp((-1)^ind*prod(diag(R)));
toc

%inv
disp('The inverse matrix for A:');
disp(R\Q');
toc