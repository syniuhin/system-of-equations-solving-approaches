function y = houseHolderVector(x)
y = x;
if (x(1)<0)
    y(1) = y(1) - norm(x);
else 
    y(1) = y(1) + norm(x);
end;