function y = houseHolderVector(x)
y = x;
if (y(1)<0)
    y(1) = y(1) - norm(x);
else 
    y(1) = y(1) + norm(x);
end;