from gensim.test.utils import datapath
from gensim import utils
import gensim.models
# from gensim.models import Word2Vec
from gensim.models import KeyedVectors

morflist = []
with open("morfemi.txt") as morfile:
	for line in morfile:
		line = line.strip()
		morflist.append(line)

dictnouns = {}
with open("nouns_itwac.txt") as infile:
	for line in infile:
		line = line.strip().split(",")
		noun, freq = line
		dictnouns[noun] = freq

basemorf = ["a", "e", "o"]
for noun in dictnouns:
	for morf in morflist:
		if noun.endswith(morf): # ?botto-bottone, *infrastrutta-infrastruttura, stanza-stanzone
			base = noun[:-(len(morf))]
			for el in basemorf:
				maybe = base+el
				# print(maybe)
				if maybe in dictnouns:
					print(noun, dictnouns[noun], maybe, dictnouns[maybe], "-"+morf)
