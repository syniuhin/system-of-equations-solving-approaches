 A = [[1, 2, 3]
     [0, 3, 2]
     [2, 0, 1]];

 B = [6;7;8];

% A = [
%         [188, -32, -9, 7, -61, 49, -53, 23, -31, 62]
%         [-32, 101, 11, -32, -80, 1, 53, -7, 94, -109]
%         [-9, 11, 231, 96, -62, -12, 72, -40, 72, -77]
%         [7, -32, 96, 174, -37, -119, 19, 7, -27, 27]
%         [-61, -80, -62, -37, 184, -34, -115, 45, -53, 46]
%         [49, 1, -12, -119, -34, 182, 80, -56, -4, 18]
%         [-53, 53, 72, 19, -115, 80, 231, -101, 70, -50]
%         [23, -7, -40, 7, 45, -56, -101, 227, -10, 23]
%         [-31, 94, 72, -27, -53, -4, 70, -10, 241, -155]
%         [62, -109, -77, 27, 46, 18, -50, 23, -155, 212]
% ];
% 
% B = [  -44;
%         74;
%         87;
%         247;
%         -39;
%         168;
%         192;
%         -199;
%         -194;
%         243;
%     ];


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


disp(L);




