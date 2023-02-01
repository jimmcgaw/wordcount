# Word Counting Adventures

Experiments in doing word count on a corpus of text in Python 3 and Spark.

I use NLTK to tokenize the text into words.

In order to set up:

```
$ python -m venv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

To run the word count using "MapReduce", run:

`$ python mapreduce.py`

Note that this doesn't actually use map-reduce, I attempted to use Python's functools.reduce
function but this wasn't actually the best approach. Instead it iterates using a simple counter.

In order to use Apache Spark, you must have it installed on your machine. (I refer you to RTFM to do so.)

To run:

`$ spark-submit spark_wordcount.py`

You can inspect the counts in the output saved in the `./spark_output` directory.