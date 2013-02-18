## Author: Alexander Ventura
## Date: February 17th, 2013
## Description: Simple Gaussian Elimination Algorithm 
## Enjoy!!

def row_swap(m, r1, ipk):
    for i in xrange(r1, len(m[0])):
        m[r1][i], m[ipk][i] = m[ipk][i], m[r1][i]

## Definition performs first part of loop on the matrix, storing multipliers and updating ip
def gauss_pp_m(m):
    ip = len(m) * [0]
    for k in xrange(0,len(m)):
        pivot = 0
        for r in xrange(k,len(m)):
            if abs(m[k][r]) > abs(pivot):
                pivot = m[k][r]
                ip[k] = r
        row_swap(m, k, ip[k])
        for i in xrange(k + 1, len(m)):
            m[i][k] = m[i][k]/float(m[k][k])
            for j in xrange(k + 1, len(m)):
                m[i][j] = m[i][j] - m[i][k]*m[k][j]
    ## Returns ip to be used in the second part of the algorithm
    return ip

def gauss_pp_b(m, b, ip):
    if len(m) != len(b):
        print "Matrix and B are not the same length"
        return
    x = len(m) * [0]
    for k in xrange(0, len(m)):
        b[k], b[ip[k]] = b[ip[k]], b[k]
        for i in xrange(k + 1, len(m)):
            b[i] = b[i] - m[i][k]*b[k]

    for i in xrange(len(m) - 1, -1, -1):
        for j in xrange(i + 1, len(m)):
            b[i] = b[i] - m[i][j]*x[j]
        x[i] = b[i] / float(m[i][i])
    return x

def gauss_pp(m, b):
    ip = gauss_pp_m(m)
    x = gauss_pp_b(m, b, ip)
    ## Add a statement here to print or do whaterver with M

    return x
