f = open("encrypted", "r")
t = f.read()

class CryptKey(dict):
    def __missing__(self, key):
        return -1

enc = CryptKey()

LL28 = 2**26

for i in range(LL28):
    enc[ t[i*9:i*9+8] ] = i

f = open("decrypted", "r")
t = f.read()

for i in range(LL28):
    if enc[t[i*9:i*9+8]] != -1:
        print enc[t[:8]], i
        break

print "end", i