import calc_frequency_score
from encoding_conversions import *
import string

def single_byte_xor(hex_message, key): #key is int, message is hex string, returns hex_string
	xord_bytes = []
	for byte in hex_to_byte_data(hex_message):
		xord_bytes.append(byte ^ key)
	xord_hex = byte_data_to_hex(xord_bytes)
	return xord_hex
	
def bf_single_byte_xor(hex_message):
	possible = []
	for k in xrange(256):
		possible.append(hex_to_ascii(single_byte_xor(hex_message, k)))
	for p in xrange(256):
		for c in possible[p]:
			if c not in string.printable:
				possible[p] = ""
				break
					
		
	scores = map(calc_frequency_score.get_score, possible)
	print "key is " + str(scores.index(min(scores)))
	print "score is " + str(min(scores))
	return possible[scores.index(min(scores))]

if __name__ == "__main__":
	print bf_single_byte_xor("130e5a0d1b095a1b5a1e1b08115a1b141e5a090e150817035a14131d120e")
