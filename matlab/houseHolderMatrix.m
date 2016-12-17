function y = houseHolderMatrix(x)
y = eye(size(x,1));
param = 2.0 / (norm(x)*norm(x));
w = x * x';
w = param * w;
y = y - w;
end
