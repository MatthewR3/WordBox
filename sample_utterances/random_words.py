# Generates sample utterances for WordWorks based on 1,000 of the most common words in the English language

with open("D:/Programming/WordBox/freq.txt", "r") as f:
	for line in f:
		# print line.strip()
		print "GetRhymeIntent rhyme for {" + line.strip() + "|Word}"
