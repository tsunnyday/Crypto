import string

frequency_file = open("letter_frequency_as_percent.txt", "r")
frequency_file_list = frequency_file.read().split()
expected_frequencies = {}
for x in xrange(0, len(frequency_file_list), 2):
	expected_frequencies[frequency_file_list[x]] = float(frequency_file_list[x+1])
	
def get_score(text):
	if not (len(text)):
		raise Exception("Text string was empty")
	text_frequencies = {}
	for c in text.lower():
		if c in text_frequencies:
			text_frequencies[c] += 1
		else:
			text_frequencies[c] = 1
			
	score = 0
	for c in text_frequencies:
		if c.lower() in string.lowercase:
			expected_count = len(text) * (expected_frequencies[c.lower()]/100.0)
			score += pow(text_frequencies[c] - expected_count, 2) / expected_count
		elif c in string.printable:
			score += text_frequencies[c] * 10
		else:
			score += text_frequencies[c] * 50
		#print "c:" + c + " expected:" + str(expected_count)
		
		
	return score

	

		
