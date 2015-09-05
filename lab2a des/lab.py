import sys, string

def to64bite(s):
    return s + "0"*(16-len(s))


def bytesfromstring(s):
    b = []
    
    for i in range(0, len(s), 2):
        b.append(int(s[i:i+2], 16))

    return b

def stringfrombytes(bytes):
    s = ""

    for b in bytes:
        s += str(hex(b))[2:]

    return s

def madekey(number):

    f = ["00000001", "00000001", "00000001", "00000001", "00000001", "00000001", "00000001", "00000001"]
    b = bin(number)[2:]

    for i in range(4):

        if len(b):
            f[7 - i] = string.zfill(b[-7:], 7)
            f[7 - i] += str( (f[7 - i].count('1') + 1) % 2 )
            b = b[:-7]

    return int(string.join(f, ""), 2)


def main():
    
    m = bin(int( to64bite( sys.argv[1] ), 16))
    c = bin(int(  sys.argv[2] , 16))

    print m, c

    k = []

    for i in range(2**28):
        k.append(madekey(i))
        if not i % 10000000:
            print hex(k[i]), i

main()