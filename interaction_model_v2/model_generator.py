# Generates the intent schema and sample utterances for WordBox based on 1,000 of the most common words in the English language


# Intent Schema
# {
#   "intents": [
#     {
#       "slots": [
#         {
#           "name": "Word",
#           "type": "AMAZON.LITERAL"
#         }
#       ],
#       "intent": "GetSynonymIntent"
#     },
#   ]
# }

# Sample Utterances
# GetSynonymIntent a synonym for {happy|Word}
# GetAntonymIntent a synonym for {evil|Word}

import os
import json


dev = 0

input_file = "freq_small.txt" if dev else "freq.txt"
schema_output_file = "intent_schema_small.json" if dev else "intent_schema.json"
utterances_output_file = "sample_utterances_small.txt" if dev else "sample_utterances.txt"

with open(os.path.dirname(os.path.realpath(__file__)) + "/" + input_file, "r") as f:
	all_words = list(set([line.strip() for line in f]))

custom_intents = [
	("GetSynonymIntent", ("a synonym for",)),
	("GetRandomSynonymIntent", ("a random synonym for",)),
	("GetAllSynonymsIntent", ("all synonyms for",)),
	("GetAntonymIntent", ("an antonym for",)),
	("GetRandomAntonymIntent", ("a random antonym for",)),
	("GetAllAntonymsIntent", ("all antonyms for",)),
	("GetPOSIntent", ("the part of speech for",)),
	("GetRhymeIntent", ("a rhyme for",)),
	("GetRandomRhymeIntent", ("a random rhyme for",)),
	("GetDefinitionIntent", ("the definition of",)),
	("GetDefinitionIntent", ("define",)),
	("GetRandomDefinitionIntent", ("a random definition for",)),
	("GetAllDefinitionsIntent", ("all definition for",)),
	("GetSyllablesIntent", ("the syllables for",)),
	("GetSyllablesIntent", ("the syllables of",)),
	# ("GetPronunciationIntent", ("how to pronounce",)),
	# ("GetPronunciationIntent", ("pronunciation of",)),
	("GetFrequencyIntent", ("the frequency of",)),
	("GetFrequencyIntent", ("how common", "is"))
]


# Intent schema
intent_json = {"intents": []}
intent_json["intents"].append({"intent": "AMAZON.CancelIntent"})
intent_json["intents"].append({"intent": "AMAZON.HelpIntent"})
intent_json["intents"].append({"intent": "AMAZON.StopIntent"})
for intent, utterance in custom_intents:
	intent_exists = False
	for json_intent in intent_json["intents"]:
		# print(intent)
		# print(json_intent["name"])
		if intent == json_intent["intent"]:
			intent_exists = True
			break
	if not intent_exists:
		intent_json["intents"].append({"intent": intent, "slots": [{"name": "WORD", "type": "ANY_WORD"}]})

with open(os.path.dirname(os.path.realpath(__file__)) + "/" + schema_output_file, "w") as f:
	json.dump(intent_json, f)


# Sample utterances
all_utterances = []
with open(os.path.dirname(os.path.realpath(__file__)) + "/" + utterances_output_file, 'w') as f:
	for intent, utterance in custom_intents:
		f.write(intent + " " + utterance[0] + " {WORD}" + ((" " + utterance[1]) if (len(utterance) > 1) else "") + "\n")
