from Crypto.Cipher import AES

def bytesfromstring(s):
    b = ""
    for i in range(0, len(s), 2):
        b += chr(int(s[i:i+2], 16)) 
    return b

def hexfromstring(s):
    h = ""
    for i in s:
        h += format( ord(i), "02x" ) 
    return h

def checkpad(encoded):
    enc = hexfromstring(encoded)
    
    pad = enc[-2:]
    cnt = int(pad, 16) if int(pad, 16) else 16

    if cnt > 16: return False

    for hh in range(cnt - 1):
        enc = enc[:-2]
        if pad != enc[-2:]:
            return False

    return True

def oracle(decoded):
    key = bytesfromstring(hexfromstring("my key          "))
    iv  = bytesfromstring(decoded[:32])
    aes = AES.new(key, 2, iv)
    
    enc = aes.decrypt( bytesfromstring(decoded) )
    
    return checkpad(enc)