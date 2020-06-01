""" This script adds data from the addendum folder to the dictionary


"""

import glob
import csv

lemmas = {}
fieldnames = []

with open("dictionnary.tsv") as f:
	reader = csv.DictReader(f, delimiter="\t")
	for line in reader:
		fieldnames = reader.fieldnames
		if (line["Lemma"], line["Nature"]) not in lemmas:
			lemmas[(line["Lemma"], line["Nature"])] = line

print(fieldnames)
before = len(lemmas)
print("{} actual lemmata.".format(len(lemmas)))

for file in glob.glob("addendum/*.tsv"):
	print(file)
	with open(file) as f:
		reader = csv.DictReader(f, delimiter="\t")
		for line in reader:
			print(line)
			if (line["Lemma"], line["Nature"]) not in lemmas:
				lemmas[(line["Lemma"], line["Nature"])] = line

print("{} new lemmata.".format(len(lemmas) - before))

with open("newdictionnary.tsv", "w") as f:
	writer = csv.DictWriter(f, fieldnames, extrasaction="ignore", delimiter="\t")
	f.write("lemma	Nature	POS	Code	Description	Variations\n")
	#writer.writeheader()
	for lemma in sorted(list(lemmas.keys()), key=lambda x: x[0].lower()+x[1]):
		writer.writerow(lemmas[lemma])