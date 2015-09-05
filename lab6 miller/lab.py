import numpy, fractions
import sys
 
def miller(p, t):
    # p - 1 = u * 2**r
    r = 0
    u = p - 1

    if p % 2 == 0:
        return False

    while u % 2 == 0:
        u  = u / 2
        r += 1
 
    for i in range(t):

        a = int(numpy.random.uniform(1, p-1))
        if fractions.gcd(a, p) != 1:
            return False
        pow_u  = pow(a, u, p)
        pow_iu = map(lambda i: pow(a, u*2**i, p), range(1, r))
        if pow_u != 1 and pow_u != p-1 and p-1 not in pow_iu:
            return False
    return True

def nextPrim(p):
    t = 5
    if p % 2 == 0:
        p += 1

    while True: 

        if miller(p, t):
            return p
        p += 2
        print p

def prim(n):

    while True:
        a = 1 + 2 * int(numpy.random.uniform(2**(n-2), 2**(n-1)))
        if miller(a, 5):
            return a

def main():
    p = int(sys.argv[1])
    n = int(sys.argv[2])

    print nextPrim(p), prim(n)

main()