from encoding_conversions import *
import itertools

def aes_word_addition(word_a, word_b): #words are arrays of four ints here
	word_c = []
	for byte_a, byte_b in itertools.izip(word_a, word_b):
		word_c.append(aes_bitwise_addition_with_bytes(byte_a, byte_b))
	return word_c
	
	
def aes_bitwise_addition_with_bytes(byte_a, byte_b):
	return byte_a ^ byte_b
	
def aes_bitwise_multiplication_with_bytes(byte_a, byte_b): # Multiply byte_a by byte_b
	byte_c = 0
	while byte_b:	

		byte_c <<= 1
		if byte_c >= 256:
			byte_c ^= 283
		if byte_b & 128:
			byte_c ^= byte_a
		byte_b <<= 1
		if byte_b & 256:
			byte_b -= 256
	
		
	return byte_c


if __name__ == "__main__":
	print aes_bitwise_multiplication("1010111","10000011")
	print aes_bitwise_multiplication_with_bytes(87, 131)
	
