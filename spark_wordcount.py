#!/usr/bin/env python3
import shutil

from pyspark import SparkContext, SparkConf

import nltk
from nltk.tokenize import word_tokenize

# check if we have NLTK corpi (corpuses?) and download if not.
try:
    word_tokenize("test string to tokenize. yahoo!")
except LookupError:
    nltk.download("all")

shutil.rmtree("./spark_output", ignore_errors=True)

sc = SparkContext("local","PySpark Bible Word Count")
words = sc.textFile("./kjbible.txt").flatMap(lambda line: [word for word in word_tokenize(line.lower())])
word_counts = words.map(lambda word: (word, 1)).reduceByKey(lambda a,b: a + b)

# for debugging. Use `pdb-attach` in another Terminal to debug
#from pdb_clone import pdb; pdb.set_trace_remote()

word_counts.saveAsTextFile("./spark_output")