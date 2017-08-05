# Generates sample utterances for WordWorks based on 1,000 of the most common words in the English language

import os
with open(os.path.dirname(os.path.realpath(__file__)) + "/freq.txt", "r") as f:
	for line in f:
		print "GetRhymeIntent rhyme for {" + line.strip() + "|Word}"
