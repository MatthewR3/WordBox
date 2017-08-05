# Generates sample utterances for WordWorks based on 1,000 of the most common words in the English language

import os


with open(os.path.dirname(os.path.realpath(__file__)) + "/freq.txt", "r") as f:
	all_words = [line.strip() for line in f]

intents = [
			("GetSynonymIntent", "a synonym for"),
			("GetAntonymIntent", "an antonym for"),
			("GetPOSIntent", "the part of speech for"),
			("GetRhymeIntent", "a rhyme for"),
			("GetDefinitionIntent", "the definition of"),
			("GetDefinitionIntent", "define"),
			("GetSyllablesIntent", "the syllables for"),
			("GetSyllablesIntent", "the syllables of"),
			("GetFrequencyIntent", "the frequency of"),
			("GetFrequencyIntent", ["how common", "is"]),
			("GetPronunciationIntent", "how to pronounce"),
			("GetPronunciationIntent", "pronunciation of")
]

with open(os.path.dirname(os.path.realpath(__file__)) + "/sample_utterances.txt", "w") as f:
	for intent, utterance in intents:
		for word in all_words:
			if isinstance(utterance, str):
				# print intent + " " + utterance + " {" + word + "|Word}"
				f.write(intent + " " + utterance + " {" + word + "|Word}" + "\n")
			elif isinstance(utterance, list):
				# print intent + " " + utterance[0] + " {" + word + "|Word} " + utterance[1]
				f.write(intent + " " + utterance[0] + " {" + word + "|Word} " + utterance[1] + "\n")
