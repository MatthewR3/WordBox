# Generates sample utterances for WordWorks based on 1,000 of the most common words in the English language

# {
#   "name": "IntentName",
#   "samples": [],
#   "slots": [
#     {
#       "name": "Word",
#       "type": "AMAZON.LITERAL",
#       "samples": []
#     }
#   ]
# },

import os
import json


dev = 1

input_file = "freq_small.txt" if dev else "freq.txt"
output_file = "interaction_model_small.json" if dev else "interaction_model.json"

with open(os.path.dirname(os.path.realpath(__file__)) + "/freq_small.txt", "r") as f:
	all_words = [line.strip() for line in f]

custom_intents = [
	("GetSynonymIntent", ("a synonym for",)),
	("GetAntonymIntent", ("an antonym for",)),
	("GetPOSIntent", ("the part of speech for",)),
	("GetRhymeIntent", ("a rhyme for",)),
	("GetDefinitionIntent", ("the definition of",)),
	("GetDefinitionIntent", ("define",)),
	("GetSyllablesIntent", ("the syllables for",)),
	("GetSyllablesIntent", ("the syllables of",)),
	("GetFrequencyIntent", ("the frequency of",)),
	("GetFrequencyIntent", ("how common", "is")),
	("GetPronunciationIntent", ("how to pronounce",)),
	("GetPronunciationIntent", ("pronunciation of",))
]

custom_slots = [
	("LITERAL", all_words)
]

intent_json = {"intents": [], "types": []}
intent_json["intents"].append({"name": "AMAZON.CancelIntent", "samples": []})
intent_json["intents"].append({"name": "AMAZON.HelpIntent", "samples": ["help"]})
intent_json["intents"].append({"name": "AMAZON.StopIntent", "samples": ["cancel"]})

for intent, utterance in custom_intents:
	all_samples = []
	for word in all_words:
		all_samples.append(utterance[0] + " {" + word + "|Word}" + ((" " + utterance[1]) if (len(utterance) > 1) else ""))
	intent_exists = False
	for json_intent in intent_json["intents"]:
		# print(intent)
		# print(json_intent["name"])
		if intent == json_intent["name"]:
			json_intent["samples"].extend(all_samples)
			intent_exists = True
			break
	if not intent_exists:
		intent_json["intents"].append({"name": intent, "samples": all_samples, "slots": [{"name": "Word", "type": "LITERAL", "samples": all_words}]})

for slot, values in custom_slots:
	intent_json["types"].append({"name": slot, "values": values})


with open(os.path.dirname(os.path.realpath(__file__)) + "/sample_utterances_small.json", "w") as f:
	json.dump(intent_json, f)
