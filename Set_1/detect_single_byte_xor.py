import single_byte_xor_bf
import string
import calc_frequency_score
from encoding_conversions import *

f = open("detecting_single_byte_xor.txt","r")
possible = []

for line in f.read().split():
	possible.append(single_byte_xor_bf.bf_single_byte_xor(hex_to_byte_data(line)))




scores = map(calc_frequency_score.get_score, possible)

print possible[scores.index(min(scores))]
