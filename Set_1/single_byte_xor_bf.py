import calc_frequency_score
from encoding_conversions import *
import string

def single_byte_xor(byte_data, key): #key is int, message is hex string, returns hex_string
	xord_bytes = []
	for byte in byte_data:
		xord_bytes.append(byte ^ key)
	return xord_bytes
	
def bf_single_byte_xor(byte_data):
	possible = []
	for k in xrange(256):
		possible.append(byte_data_to_ascii(single_byte_xor(byte_data, k)))
	
					
		
	scores = map(calc_frequency_score.get_score, possible)
	return possible[scores.index(min(scores))]	
	
def bf_single_byte_xor_with_key(byte_data):
	possible = []
	for k in xrange(256):
		possible.append(byte_data_to_ascii(single_byte_xor(byte_data, k)))
	
					
		
	scores = map(calc_frequency_score.get_score, possible)
	return (possible[scores.index(min(scores))], scores.index(min(scores)))	
	
def bf_single_byte_xor_verbose(byte_data):
	possible = []
	for k in xrange(256):
		possible.append(byte_data_to_ascii(single_byte_xor(byte_data, k)))
	
					
		
	scores = map(calc_frequency_score.get_score, possible)
	print "key is " + str(scores.index(min(scores)))
	print "score is " + str(min(scores))
	return possible[scores.index(min(scores))]

if __name__ == "__main__":
	print bf_single_byte_xor(hex_to_byte_data("130e5a0d1b095a1b5a1e1b08115a1b141e5a090e150817035a14131d120e"))
