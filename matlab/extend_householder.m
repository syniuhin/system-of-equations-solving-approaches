function y = extend_householder(x)
    first_row = zeros(1,size(x,2)+1); 
    first_row(1) = 1;
    y = cat(2, zeros(size(x,1),1), x);
    y = [first_row; y];
end

