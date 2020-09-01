""" This script adds data from the addendum folder to the dictionary


"""

import glob
import csv

lemmas = {}
fieldnames = []
HEADER = "lemma	Nature	POS	Description	Variation	Code".split("\t")

with open("dictionary.tsv") as f:
	reader = csv.DictReader(f, delimiter="\t")
	for line in reader:
		fieldnames = reader.fieldnames
		if (line["lemma"], line["Nature"]) not in lemmas:
			lemmas[(line["lemma"], line["Nature"])] = line

print(fieldnames)
before = len(lemmas)
print("{} actual lemmata.".format(len(lemmas)))

for file in glob.glob("addendum/latin-tardif.tsv"):
	print(file)
	with open(file) as f:
		reader = csv.DictReader(f, delimiter="\t")
		for line in reader:
			line["lemma"] = line["lemma"].replace("v", "u").replace("V", "U").replace("J", "I").replace("j", "i")
			if (line["lemma"], line["Nature"]) not in lemmas:
				lemmas[(line["lemma"], line["Nature"])] = line

print("{} new lemmata.".format(len(lemmas) - before))

with open("dictionary.tsv", "w") as f:
	writer = csv.DictWriter(f, HEADER, extrasaction="ignore", delimiter="\t", lineterminator="\n")
	writer.writeheader()
	for lemma in sorted(list(lemmas.keys()), key=lambda x: x[0].lower()+x[1]):
		writer.writerow(lemmas[lemma])