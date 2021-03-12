morflist = []
with open("morphemes.txt") as morfile:
	for line in morfile:
		line = line.strip()
		morflist.append(line)

dictnouns = {}
with open("input.txt") as infile:
	for line in infile:
		line = line.strip().split(",")
		noun, freq = line
		dictnouns[noun] = freq

basemorf = ["a", "e", "o"]
with open("output.txt", "w") as outfile:
	for noun in dictnouns:
		for morf in morflist:
			if noun.endswith(morf): # ?botto-bottone, *infrastrutta-infrastruttura, stanza-stanzone
				base = noun[:-(len(morf))]
				for el in basemorf:
					maybe = base+el
					# print(maybe)
					if maybe in dictnouns:
						# print(noun, dictnouns[noun], maybe, dictnouns[maybe], "-"+morf)
						outfile.write(noun+" "+dictnouns[noun]+" "+maybe+" "+dictnouns[maybe]+" "+"-"+morf+"\r\n")
