from nltk.corpus import words
import json, random
from pprint import pprint

pprint(words.words())
words_list = words.words()[:1000]
random.shuffle(words_list)
pprint(words_list)

words_list = [word.lower() for word in words_list]

words_list = list(set(words_list))

word_pairs = []
for word in words_list:
    pair = ' '.join(random.sample(words_list, 2))
    word_pairs.append(pair)

word_pairs = list(set(word_pairs))
values = []
for pair in word_pairs:
    values.append(pair)
print(json.dumps(values))
