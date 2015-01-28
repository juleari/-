import sys

def to16byte(s):
    return s + "0"*(32-len(s))


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

def rc4key(key):

    r = range(256)
    l = len(key)

    j = 0
    for i in range(256):
        j = (j + r[i] + key[ i % l ]) % 256
        r[i], r[j] = r[j], r[i]

    return r

def getNextByte(i, j, r):

    i = (i + 1) % 256
    j = (j + r[i]) % 256

    r[i], r[j] = r[j], r[i]

    return i, j, r

def encode(text, key):

    enctext = []
    a = b = 0

    for i in text:

        a, b, key = getNextByte(a, b, key)
        enctext.append( i ^ key[(key[a] + key[b]) % 256 ] )

    return enctext

def main():
    
    key  = rc4key( bytesfromstring( to16byte(sys.argv[1]) ) )
    text = bytesfromstring( sys.argv[2] )

    enctext = encode(text, key)
    print stringfrombytes(enctext)


    key     = rc4key( bytesfromstring( to16byte(sys.argv[1]) ) )
    dectext = encode(enctext, key)
    print stringfrombytes(dectext)

main()