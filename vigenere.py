import string
import re
import caesar_solver


def shift_character(char, offset):
	offset = offset % 26
	if char in string.lowercase:
		alphabet = string.lowercase
	elif char in string.uppercase:
		alphabet = string.uppercase
	else:
		return char
	char = chr(ord(char) + offset)
	if char not in alphabet:
		char = chr(ord(char) - 26)
	return char

def vigenere_encrypt(message, key):
	encrypted = ""
	message = re.sub("[^a-zA-Z]+", "", message)
	key = key.lower()
	for index, char in enumerate(message):
		encrypted += shift_character(char, string.lowercase.index(key[index % len(key)]))
	return encrypted
	
def vigenere_decrypt(message, key_length):
	decrypted = ""
	message = re.sub("[^a-zA-Z]+", "", message)
	caesar_streams = [[] for i in xrange(key_length)]
	for i in xrange(0, len(message), key_length):
		for j in xrange(key_length):
			if i + j < len(message):
				caesar_streams[j].append(message[i + j])
	decoded_streams = []
	key = ""
	for stream in caesar_streams:
		decoded, k =  caesar_solver.solve_with_key(stream)
		decoded_streams.append(decoded)
		key += string.lowercase[26-k]
	cracked = ""
	for j in xrange(len(decoded_streams[0])):
		for stream in decoded_streams:
			if j < len(stream):
				cracked += stream[j]
	return (cracked, key)



def kasiski_method(message):
	pass



def find_distances_of_repeated_substrings(message):
	minimum_substring_length = 3
	sub_start = 0
	sub_end = minimum_substring_length
	substrings = {} #Format is {substring: [list of distances]} 
	
	while (True):
		if sub_end >= len(message):
			break
		sub = message[sub_start:sub_end]
		if message.find(sub, sub_end) != -1:
			while (True):
				sub_end += 1
				sub = message[sub_start:sub_end]
				if(message.find(sub, sub_end)) != -1:
					continue
				else:
					sub_end -= 1
					sub = message[sub_start:sub_end]
					repeat_start = message.find(sub, sub_end)
					print "Substring {} found at [{}:{}] and at [{}:{}]".format(sub, str(sub_start), str(sub_end), str(repeat_start), str(repeat_start + (sub_end - sub_start)))
					if sub in substrings:
						substrings[sub].append(repeat_start - sub_start)
					else:
						substrings[sub] = [repeat_start - sub_start]
					sub_start = sub_end
					sub_end = sub_start + minimum_substring_length
					break
		else:
			sub_start += 1
			sub_end += 1
		
	
	return substrings
			
	
	

if __name__ == "__main__":
	s = "two households both alike in dignity in fair verona where we lay our scene from ancient grudge break to new mutiny where civil blood makes civil hands unclean from forth the fatal loins of these two foes a pair of star crossd lovers take their l"
	c = vigenere_encrypt(s, "romeo")
	
	
	#find_distances_of_repeated_substrings(c)
	
	print vigenere_decrypt(c, 5)
