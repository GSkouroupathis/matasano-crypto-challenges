# http://cryptopals.com/sets/1/challenges/1/
# George Skouroupathis

import base64, string

# Converts Hex to String
def pretty(enc):
	strg=""
	for i in xrange(0, len(enc), 2):
		hexVal = enc[i:i+2]
		strg += chr(int(hexVal, 16))
	return strg
	
# Challenge 1
def hex_to_base64(enc):
	strg = ""
	for i in xrange(0, len(enc), 2):
		hexVal = enc[i:i+2]
		strg += chr(int(hexVal, 16))
	return base64.b64encode(strg)
                
# Challenge 2
def fixed_xor(hex1, hex2):
	hexXored = ""
	for i in xrange(0, len(hex1), 2):
		hexVal1, hexVal2 = hex1[i:i+2], hex2[i:i+2]
		hexXored += hex(int(hexVal1, 16) ^ int(hexVal2, 16))[2:]
	return hexXored

# Scores a Hex string using char frequencies
def freq_score(hexstr):
	alphaScores = {'41':8.12, '42':1.49, '43':2.71, '44':4.32, '45':12.02, \
	'46':2.3, '47':2.03, '48':5.92, '49':7.31, '4A':0.1, '4B':0.69, '4C':3.98, \
	'4D':2.61, '4E':6.95, '4F':7.68, '50':1.82, '51':0.11, '52':6.02, '53':6.28, \
	'54':9.1, '55':2.88, '56':1.11, '57':2.09, '58':0.17, '59':2.11, '5A':0.07, \
	'61':8.12, '62':1.49, '63':2.71, '64':4.32,	'65':12.02, '66':2.3, '67':2.03, \
	'68':5.92, '69':7.31,	'6A':0.1, '6B':0.69, '6C':3.98, '6D':2.61, '6E':6.95, \
	'6F':7.68, '70':1.82, '71':0.11, '72':6.02, '73':6.28, '74':9.1, '75':2.88, \
	'76':1.11, '77':2.09, '78':0.17, '79':2.11, '7A':0.07}
	
	score = 0
	for i in xrange(0, len(hexstr), 2):
		hx = hexstr[i:i+2]
		if hx in alphaScores.keys(): score += alphaScores[hx]
	return score

# Challenge 3
def single_xor(enc):	alphas = string.ascii_uppercase + string.ascii_lowercase
	greatestScore = 0
	greatestDec = None
	for alpha in alphas:
		alpha = hex(ord(alpha))[2:]
		key = ""
		for i in range(len(enc)/2):
			key += alpha
		dec = fixed_xor(enc, key)
		score = freq_score(dec)
		if score > greatestScore:
			greatestScore = score
			greatestDec = dec
	return (greatestScore, greatestDec)

 
 
 
 
 
 





