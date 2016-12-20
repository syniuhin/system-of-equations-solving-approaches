A = [
    [-27, -93, -74, -45, 67, 74, 17, 96, -36],
    [59, 79, -66, 45, -90, 20, -58, -61, -62],
    [73, -82, -1, 9, -79, -27, 40, 26, 52],
    [-39, 91, -95, 80, 52, -26, -14, -10, -42],
    [-23, -64, -10, 61, -33, -98, -28, 12, 22],
    [17, 45, 23, 58, 27, -27, -78, 99, -64],
    [-39, 27, 6, -66, 87, 32, -15, -36, 82],
    [89, 40, -17, -44, -29, -31, 55, -52, 3],
    [81, -60, 86, 42, 43, 29, 95, -70, -26],
]

B = [
    [43],
    [84],
    [-7],
    [38],
    [59],
    [93],
    [-5],
    [73],
    [-10],
]

A =  [[1,2,3];[0,3,2];[2,0,1]]
B = [6;7;8]

n = size(A,1);
Q = eye(n);
L = eye(n) * A;

u = @(x) houseHolderVector(x);
hs = @(x) houseHolderMatrix(x);
extend = @(x) extend_householder(x);

ind = 0;
for i = 1:1:(n-1)
      a_i = L(i,i:size(L,1))';
      val = u(a_i);
      H = hs(val);
      if (ind ~= 0)
          for j = 1:1:ind
            H = extend(H);
          end
      end
      L = L * H;
      Q = H * Q;
      ind = ind + 1;
end;

C = [L,B];
disp(C);
[b,Y] = backward_left(C);
X = Q' * Y';

disp(X);

%determinant
disp('The determinant of A matrix equals');
disp((-1)^ind*prod(diag(L)));

%inv
disp('The invariant matrix for A is below:');
disp(L\Q');


