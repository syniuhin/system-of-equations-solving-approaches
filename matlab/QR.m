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

n = size(A,1);
Q = eye(n);
R = A;

function [B, T] = inverse(Q, R)
  n = size(R, 1);
  T = zeros(n, n);
  for i = 1:n
    T(i, i) = 1 / R(i, i);
    for j = i+1:n
      T(i, j) = -sum(T(i, 1:j-1) .* R(1:j-1, j)') / R(j, j);
    end;
  end;

  B = T * Q';
end;

tic
ind = 0;
for i = 1:(n-1)
  a_i = R(i:n,i);
  val = houseHolderVector(a_i);
  H = houseHolderMatrix(val);
  for j = 1:i-1
    H = extend_householder(H);
  end;
  R = H * R
  Q = Q * H;
  ind = ind + 1;
end;


[a, x] = backward_right([R Q' * b]);
x
%determinant
disp('The determinant of A matrix equals');
det = (-1)^ind * prod(diag(R))
toc

%inv
disp('The inverse matrix for A:');
% inversed = R\Q'
[inversed, T] = inverse(Q, R)
toc

disp('Check inversed');
inversed * A
