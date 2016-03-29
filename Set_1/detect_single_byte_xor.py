import single_byte_xor_bf
import calc_frequency_score

f = open("detecting_single_byte_xor.txt","r")
possible = []
for line in f.read().split():
	possible.append(single_byte_xor_bf.bf_single_byte_xor(line))
scores = map(calc_frequency_score.get_score, possible)
print "single byte xor is " + str(scores.index(min(scores)))
print possible[scores.index(min(scores))]
print possible
