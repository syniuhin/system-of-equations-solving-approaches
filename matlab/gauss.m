A1 = [
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

b1 = [
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

function B = inverse(A)
  n = size(A, 1);
  I = eye(n);
  AE = [A, I]
  disp('Forward pass');
  AE = forward(AE)
  disp('Backward pass');
  AE = backward_right(AE)
  B = AE(:, n+1:2*n);
end;

tic
S = [A1 b1];
disp('Forward pass');
S = forward(S);
toc
disp('Backward pass');
[B, x] = backward_right(S);
B
x
toc

T = triangalize(A1);
det = determinant(T)
toc

[Inv, ] = inverse(A1)
toc

disp('Check inverse matrix');
Inv * A1
