# Removes duplicates from freq.txt

import os

with open(os.path.dirname(os.path.realpath(__file__)) + "/freq.txt", "r") as f:
    all_words = list(set([line.strip() for line in f]))

# Debugging duplicates
# with open(os.path.dirname(os.path.realpath(__file__)) + "/freq.txt", "r") as f:
#     all_words_dup = [line.strip() for line in f]
#
# print(len(all_words))
# print(len(all_words_dup))
# occurrences = {}
# for word in all_words_dup:
#     if word not in occurrences:
#         occurrences[word] = 0
#     occurrences[word] += 1
# 
# sum = 0
# for word in occurrences:
#     if occurrences[word] > 1:
#         print(word, occurrences[word])
#         sum += occurrences[word] - 1
# print(sum)

with open(os.path.dirname(os.path.realpath(__file__)) + "/freq.txt", 'w') as f:
    for word in all_words:
        f.write(word + "\n")
