A = [
    [390, 201, 0, 0, 0, 0, 0, 0, 0, 0],
    [21, -135, -53, 0, 0, 0, 0, 0, 0, 0],
    [0, -271, 868, -203, 0, 0, 0, 0, 0, 0],
    [0, 0, -7, 596, 160, 0, 0, 0, 0, 0],
    [0, 0, 0, -47, -208, -96, 0, 0, 0, 0],
    [0, 0, 0, 0, -24, 347, -17, 0, 0, 0],
    [0, 0, 0, 0, 0, -96, 220, -40, 0, 0],
    [0, 0, 0, 0, 0, 0, 107, 546, -204, 0],
    [0, 0, 0, 0, 0, 0, 0, -301, -740, -364],
    [0, 0, 0, 0, 0, 0, 0, 0, 48, -154],
];

y = [
    [446],
    [62],
    [-783],
    [264],
    [-747],
    [-732],
    [-803],
    [-716],
    [-664],
    [-608],
];

function [roots, det] = thomas(A, y)
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
    end;

    roots = [lamb];

    for i = n - 1:-1:1
        sigma = coeff(i, 1);
    	lamb = coeff(i, 2);
        roots = [sigma * roots(1) + lamb, roots];
    end;
end;

tic
[roots, det] = thomas(A, y)
toc
