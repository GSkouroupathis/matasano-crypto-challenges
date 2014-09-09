# http://cryptopals.com/sets/1/challenges/1/
# George Skouroupathis

import base64

# Challenge 1
def hexToBase64(enc):
        str = ""
        for i in xrange(0, len(enc), 2):
                hexVal = enc[i:i+2]
                str += chr(int(hexVal, 16))
        return base64.b64encode(str)
                
# Challenge 2
def fixedXor(hex1, hex2):
        hexXored = ""
        for i in xrange(0, len(hex1), 2):
                hexVal1, hexVal2 = hex1[i:i+2], hex2[i:i+2]
                hexXored += hex(int(hexVal1, 16) ^ int(hexVal2, 16))[2:]
        return hexXored

# Challenge 3
