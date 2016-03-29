import string

frequency_file = open("letter_frequency_as_percent.txt", "r")
frequency_file_list = frequency_file.read().split()
frequencies = {}
for x in xrange(0, len(frequency_file_list), 2):
	frequencies[frequency_file_list[x]] = float(frequency_file_list[x+1])
	
def get_score(text):
	if not (len(text)):
		return 999999999
	text_frequencies = {}
	for c in string.lowercase:
		text_frequencies[c] = 0
	for c in text.lower():
		if c in string.lowercase:
			text_frequencies[c] += 1
	score = 0
	for c in frequencies:
		expected_count = len(text) * (frequencies[c]/100.0)
		score += pow(text_frequencies[c] - expected_count, 2) / expected_count
	return score
	

		
