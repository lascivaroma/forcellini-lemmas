with open("lemmata.csv", "w") as out:
	data = []
	exists = []
	with open("source_lemmata.csv") as f:
		for line in f:
			exists.append(line.strip())
	with open("../dictionary.tsv") as f:
		first = False
		for line in f:
			if not first:
				first = True
				continue
			lemma =  data.append(line.split("\t")[0])

	data = set(data)
	exists = set(exists)

	tobe_added = data.difference(exists)

	missing = exists.difference(data)
	out.write("\n".join(sorted(list(set(tobe_added)))))
	
print("Missing in dictionary")
print(sorted(list(missing)))