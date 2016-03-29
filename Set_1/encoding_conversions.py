
BASE64_VALUES = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/='


def hex_to_byte_data(hex_string):
	if len(hex_string) % 2:
		raise Exception("Hex String has an odd number of characters")
	hex_bytes = []
	for i in xrange(0, len(hex_string), 2):
		hex_bytes.append(hex_string[i] + hex_string[i+1])
	byte_data = []
	for x in hex_bytes:
		byte_data.append(int(x, 16))
	return byte_data

def ascii_to_byte_data(ascii_string):
	byte_data = []
	for char in ascii_string:
		byte_data.append(ord(char))
	return byte_data
	
def byte_data_to_ascii(byte_data):
	ascii_string = ""
	for byte in byte_data:
		ascii_string += chr(byte)
	return ascii_string	

def byte_data_to_hex(byte_data):
	hex_string = ""
	for byte in byte_data:
		hex_byte = hex(byte)[2:]
		if len(hex_byte) != 2:
			hex_byte = "0" + hex_byte
		hex_string += hex_byte
	return hex_string

def byte_data_to_base64(byte_data):
	base64string = ""
	padding = [0, 2, 1][len(byte_data) % 3]
	for pad in xrange(padding):
		byte_data.append(0)
	for i in xrange(0, len(byte_data), 3):
		bit_string = ""
		for j in xrange(3):
			bit_string += byte_to_bit_string(byte_data[i + j])
		for k in xrange(4):
			base64string += BASE64_VALUES[int(bit_string[6*k:6*(k+1)], 2)]
	if padding:
		base64string = base64string[:-padding] + ("=" * padding)
	return base64string
			
def byte_to_bit_string(byte):
	bit_string = bin(byte)[2:]
	while len(bit_string) != 8:
		bit_string = '0' + bit_string
	return bit_string
	
def ascii_to_base64(ascii_string):
	return byte_data_to_base64(ascii_to_byte_data(ascii_string))
	
def hex_to_base64(hex_string):
	return byte_data_to_base64(hex_to_byte_data(hex_string))
	
def hex_to_ascii(hex_string):
	return byte_data_to_ascii(hex_to_byte_data(hex_string))

def ascii_to_hex(ascii_string):
	return byte_data_to_hex(ascii_to_byte_data(ascii_string))
	
	
if __name__ == "__main__":
	assert hex_to_base64("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d") == "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
	
