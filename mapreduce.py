#!/usr/bin/env python3
"""A pure Python implementation of the infamous "hello world" word count
done by a map-reduce algorithm. nltk library is used to tokenize the text
into words.

"""
from collections import Counter

import nltk
from nltk.tokenize import word_tokenize

# check if we have NLTK corpi (corpuses?) and download if not.
try:
    word_tokenize("test string to tokenize. yahoo!")
except LookupError:
    nltk.download("all")


with open("./kjbible.txt", 'r') as f:
    text = f.read()


word_counter = Counter()
for word in word_tokenize(text.lower()):
    word_counter[word] += 1

print(word_counter)
