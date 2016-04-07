from encoding_conversions import *
from single_byte_xor_bf import bf_single_byte_xor, bf_single_byte_xor_with_key
import calc_frequency_score

def get_hamming_weight(byte_data):
	bit_string = ""
	for byte in byte_data:
		bit_string += byte_to_bit_string(byte)
	hamming_weight = 0
	for bit in bit_string:
		if bit == "1":
			hamming_weight += 1
	return hamming_weight
	
def get_hamming_distance(bytes_a, bytes_b):
	assert len(bytes_a) == len(bytes_b)
	xord_bytes = []
	for i in xrange(len(bytes_a)):
		xord_bytes.append(bytes_a[i] ^ bytes_b[i])
	return get_hamming_weight(xord_bytes)
	
def get_key_length(byte_data, max_key=16):
	normalized_hamming_distances = []
	for k in xrange(1, max_key):
		blocks = []
		distances = 0
		a = len(byte_data) / max_key
		if a % 2:
			a -= 1
		for b in xrange(a):
			blocks.append(byte_data[b*k:(b+1)*k])
		for b in xrange(0, a, 2):
			distances += get_hamming_distance(blocks[b], blocks[b+1])
		distances = distances / float(a/2)	
		normalized_hamming_distances.append(distances / float(k))
	distance_sorted = sorted(normalized_hamming_distances)
	print "MOST LIKELY KEYS:"
	for k in xrange(10):
		print "KEYLENGTH: " + str(normalized_hamming_distances.index(distance_sorted[k]) + 1) + " SCORE: " + str(distance_sorted[k])
	
def crack_repeated_xor(byte_data, key_length):
	byte_data_streams = [[] for i in xrange(key_length)]
	for i in xrange(0, len(byte_data), key_length):
		for j in xrange(key_length):
			if i + j < len(byte_data):
				byte_data_streams[j].append(byte_data[i + j])
	decoded_streams = []
	for stream in byte_data_streams:
		decoded_streams.append(bf_single_byte_xor(stream))
	cracked = ""
	for j in xrange(len(decoded_streams[0])):
		for stream in decoded_streams:
			if j < len(stream):
				cracked += stream[j]
	return cracked
	
def crack_repeated_xor_with_key(byte_data, key_length):
	byte_data_streams = [[] for i in xrange(key_length)]
	for i in xrange(0, len(byte_data), key_length):
		for j in xrange(key_length):
			if i + j < len(byte_data):
				byte_data_streams[j].append(byte_data[i + j])
	decoded_streams = []
	key = ""
	for stream in byte_data_streams:
		decoded, k =  bf_single_byte_xor_with_key(stream)
		decoded_streams.append(decoded)
		key += chr(k)
	cracked = ""
	for j in xrange(len(decoded_streams[0])):
		for stream in decoded_streams:
			if j < len(stream):
				cracked += stream[j]
	return (cracked, key)
		
		

		
if __name__ == "__main__":
	base64_ciphertext = open("repeated_xor.txt", "r").read().replace("\n","")
	ciphertext = base64_to_byte_data(base64_ciphertext)
	#get_key_length(ciphertext, 40)
	
	print crack_repeated_xor_with_key(ciphertext, 29)
	#I went and grabbed an old repeated xor from PicoCTF 2014 to test this with also. It's in hex, and in encrypted.txt
	#hex_ciphertext = open("encrypted.txt", "r").read().replace("\n","")
	#ciphertext = hex_to_byte_data(hex_ciphertext)
	#get_key_length(ciphertext, 40)
	#print crack_repeated_xor(ciphertext, 8)

	
