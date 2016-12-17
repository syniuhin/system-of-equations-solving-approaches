function [roots, det] = thomas_algorithm(A, y)
	 n = size(A, 1);

    coeff = zeros(n, 2);
    det = 1;
    sigma = 0;
    lamb = 0;

    for i = 1:n
    	if(i - 1 > 0)
        	b = 1. * A(i, i - 1);
        else
        	b = 0.;
        endif

        c = 1. * A(i, i);
        
        if(i != n)
        	d = 1. * A(i, i + 1);
        else
        	d = 0.;
        endif

        det *= (c + b * sigma);

        tmp = -d / (c + b * sigma);
        lamb = (y(i, 1) - b * lamb) / (c + b * sigma);
        sigma = tmp;

        coeff(i, :) = [sigma, lamb];
    endfor

    roots = [lamb];

    for i = n - 1:-1:1
        sigma = coeff(i, 1);
    	lamb = coeff(i, 2);
        roots = [sigma * roots(1) + lamb, roots];
    endfor
endfunction