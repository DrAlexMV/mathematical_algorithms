USAGE:

In a python file named g_elim.py, type:


import gaussian_pp as g

## Any matrix M + B you wish to solve for 

m = [[-1, 2, 3], [4, -2, 8], [2, 1, 8]]
b = [0, 22, 36]
x = g.gauss_pp(m, b)
print x ## Will print the solutions
