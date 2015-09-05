import sys
from oracle import oracle, hexfromstring

BLOCK_LENGTH = 32

def messagefrombytes(b):
    m = ""
    for i in b:
        m += chr(i)
    return m

def get_beat(pos, dec, a, hh):
    pos_st    = 64 - 2*pos if pos else 32
    decrypted = dec[:pos_st]

    roundk = pos if pos else 16

    for i in range(roundk):
        ai         = a[i - 1] if i else hh
        decrypted += format( int( dec[pos_st : pos_st+2], 16) ^ ai ^ pos, "02x")
        pos_st    += 2

    decrypted+= dec[pos_st:]

    return decrypted

def get_block(pos, dec, a):
    
    for hh in range(255, 0, -1):
    
        decrypted = get_beat(pos, dec, a, hh)
        
        if oracle(decrypted):
            return  get_block((pos + 1) % 16, dec, [hh] + a) if pos else\
                    messagefrombytes([hh] + a)
    
    return messagefrombytes(a)

def main():
    decrypted = sys.argv[1]

    print hexfromstring(get_block(1, decrypted[:32]+decrypted[:64], []) + get_block(1, decrypted, []))

main()