import sys, string
from Crypto.Cipher import DES as des

def toblocklen(s):
    return s + "0" * ( 16 - len(s) )

def bytesfromstring(s):
    b = ""
    for i in range(0, len(s), 2):
        b += chr( int( s[ i : i+2 ], 16 )) 
    return b

def madekey( number ):
    f = []
    b = format( number, "028b" )
    for i in range(4):
        f.append( b[ :7 ] )
        f[ -1 ] += str( ( f[-1].count('1') + 1 ) % 2 )
        b        = b[7:]
    return format( int( string.join( f, "" ), 2 ), "08x" )

class CryptKey( dict ):
    def __missing__( self, key ):
        return -1

class Des2middle( object ):
    def __init__( self, m1, m2 ):
        self.m1      = m1
        self.m2      = m2

    def get_encode( self, key ):
        cipher = des.new( b"\x01\x01\x01\x01" + key, 1)
        return cipher.encrypt( self.m1 )
    
    def get_decode( self, key ):
        cipher = des.new( b"\x01\x01\x01\x01" + key, 1)
        return cipher.decrypt( self.m2 )
    
    def decode_all( self ):
        LL28 = 2**28
        encodes = CryptKey()
    
        for i in range( LL28 ):
            encodes[ self.get_encode( bytesfromstring( madekey(i) )) ] = i
    
        for i in range( LL28 ):
            decode = self.get_decode( bytesfromstring( madekey(i) ))
            if encodes[ decode ] != -1:
                return madekey( encodes[ decode ] ), madekey(i)
        return "ff", "ff"

def main():
    m1 = bytesfromstring( toblocklen( sys.argv[1] ))
    m2 = bytesfromstring( toblocklen( sys.argv[2] ))
    
    des2 = Des2middle(m1, m2)
    
    print "01010101%s01010101%s" % des2.decode_all()
    
main()