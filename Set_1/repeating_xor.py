from encoding_conversions import *

def repeating_xor(message_bytes, key_bytes): #everything is in bytes
	xord_bytes = []
	for i in xrange(0, len(message_bytes), len(key_bytes)):
		for x in xrange(0, len(key_bytes)):
			
			
			if(i + x < len(message_bytes)):
				xord_bytes.append(message_bytes[i + x] ^ key_bytes[x])
	
		
	return xord_bytes
	



if __name__ == "__main__":
	assert byte_data_to_hex(repeating_xor(ascii_to_byte_data("Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"), ascii_to_byte_data("ICE"))) == "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"

	
