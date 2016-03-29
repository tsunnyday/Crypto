from encoding_conversions import hex_to_byte_data, byte_data_to_hex

def xor(hex_a, hex_b):
	bytes_a = hex_to_byte_data(hex_a)
	bytes_b = hex_to_byte_data(hex_b)
	if len(bytes_a) != len(bytes_b):
		raise Exception("Unequal Buffers")
	
	xord_bytes = []
	for i in xrange(len(bytes_a)):
		xord_bytes.append(bytes_a[i] ^ bytes_b[i])
	return byte_data_to_hex(xord_bytes)
	
if __name__ == "__main__":
	assert xor("1c0111001f010100061a024b53535009181c","686974207468652062756c6c277320657965") == "746865206b696420646f6e277420706c6179"
