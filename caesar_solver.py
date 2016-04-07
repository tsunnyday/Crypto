import string
import calc_frequency_score
def solve(text):
	possible = []
	for k in xrange(26):
		shifted = ""
		for c in text:
			if c in string.lowercase:
				i = string.lowercase.index(c) + k
				if i < 26:
					s_c = string.lowercase[i]
				else:
					s_c = string.lowercase[i - 26]
				shifted += s_c
			elif c in string.uppercase:
				i = string.uppercase.index(c) + k
				if i < 26:
					s_c = string.uppercase[i]
				else:
					s_c = string.uppercase[i - 26]
				shifted += s_c
			else:
				shifted += c
			
		possible.append(shifted)
	scores = map(calc_frequency_score.get_score, possible)
	print "key is " + str(scores.index(min(scores)))
	return possible[scores.index(min(scores))]
	
def solve_with_key(text):
	possible = []
	for k in xrange(26):
		shifted = ""
		for c in text:
			if c in string.lowercase:
				i = string.lowercase.index(c) + k
				if i < 26:
					s_c = string.lowercase[i]
				else:
					s_c = string.lowercase[i - 26]
				shifted += s_c
			elif c in string.uppercase:
				i = string.uppercase.index(c) + k
				if i < 26:
					s_c = string.uppercase[i]
				else:
					s_c = string.uppercase[i - 26]
				shifted += s_c
			else:
				shifted += c
			
		possible.append(shifted)
	scores = map(calc_frequency_score.get_score, possible)
	return (possible[scores.index(min(scores))], scores.index(min(scores)))
	
if __name__ == "__main__":
	print solve("Cqn oxuuxfrwp cxxu juuxfb hxd cx nwlahyc j cngc frcq j brvyun xoobnc jupxarcqv - jubx twxfw jb Ljnbja lryqna. Ro hxd jan dbrwp 13 jb cqn tnh, cqn anbduc rb brvruja cx jw axc13 nwlahycrxw. ")
