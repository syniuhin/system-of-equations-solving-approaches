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
    alpha = 0;
    beta = 0;

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

        det *= (c + b * alpha);

        if c + b * alpha == 0
            disp('Correctness failed');
        end;
        tmp = -d / (c + b * alpha);
        if abs(tmp) > 1
            disp('UNSTABLE');
        end;
        beta = (y(i, 1) - b * beta) / (c + b * alpha);
        alpha = tmp;

        coeff(i, :) = [alpha, beta];
    end;

    coeff
    roots = [beta];

    for i = n - 1:-1:1
        alpha = coeff(i, 1);
    	beta = coeff(i, 2);
        roots = [alpha * roots(1) + beta, roots];
    end;
end;

tic
[roots, det] = thomas(A, y)
toc
