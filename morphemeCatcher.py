morflist = []
with open("morphemes.txt") as morfile:
	for line in morfile:
		line = line.strip()
		morflist.append(line)
print("read morpheme list")

nounlist = []
with open("input_cleaner.txt") as cleanfile:
	for line in cleanfile:
		line = line.strip()
		nounlist.append(line)
print("read WordNet noun list")

dictnouns = {}
with open("input.txt") as infile:
	for line in infile:
		line = line.strip().split(" ")
		noun, freq = line
		dictnouns[noun] = freq
print("read full noun list")

basemorf = ["a", "e", "o"]
with open("output.txt", "w") as outfile:
	for noun in dictnouns:
		if (int(dictnouns[noun]) > 10) and (noun.isalpha()):
			for morf in morflist:
				if noun.endswith(morf): # ?botto-bottone, *infrastrutta-infrastruttura, stanza-stanzone
					base = noun[:-(len(morf))]
					for el in basemorf:
						maybe = base+el
						# print(maybe)
						if maybe in dictnouns:
							print(noun, dictnouns[noun], maybe, dictnouns[maybe], "-"+morf)
							outfile.write(noun+" "+dictnouns[noun]+" "+maybe+" "+dictnouns[maybe]+" "+"-"+morf+"\r\n")
