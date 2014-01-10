# unhashtag: a coding challenge

Are you interested in working for [Luminoso](http://luminoso.com)? Great! We'd like to see what your Python code looks like, and how good you are at doing messy things with messy text.

## Task: How do you separate words in Twitter hashtags?

It is, of course, a time-honored tradition on the Internet to WRITE THINGS IN ALL CAPS when you want to emphasize them and also be annoying.

The popularity of Twitter, however, has created a new way to annoyingly emphasize things: by running all the words together and making them into a hashtag.

    Before: HEY PAY ATTENTION TO ME
    After: #heypayattentiontome

In this repository, we've created a data set that takes this to its natural conclusion. We extracted 50,000 all-caps phrases from Twitter, and made an alternate version of them that converts them to a lowercase hashtag, with no spaces or apostrophes. `hashtagify.py` is a very simple script that performs this operation.

Your task is to write a Python script that reverses this process, determining where to insert spaces into the hashtags to separate them into words again.

An outline of what you'll need to do:

* Write code that builds a model of where spaces belong, using whatever techniques you like. You'll probably want to use the training files for this.
* Write an "unhashtagifier", code that uses this model to convert hashtags into all-caps phrases with spaces. (Don't worry about apostrophes unless you really want to.)
* Write evaluation code that runs your unhashtagifier on the testing files, and measures how often it puts spaces in the correct places.

We are looking for code that solves the problem well (as measured by the F-score defined below), is written with good style, and is reasonably efficient.

## Evaluation

Measure your performance by computing the following statistics on the test data:

* *Precision*: of the spaces you output, what proportion of them are correct?
* *Recall*: of the 176582 spaces in the test data, what proportion of them do you correctly output?
* Your *F-score* is (2 * *precision* * *recall*) / (*precision* + *recall*).

## The data files

* `data/training_orig.txt` and `data/testing_orig.txt` contain all-caps phrases with spaces.
* `data/training_hashtags.txt` and `data/testing_hashtags.txt` contain the same phrases, in the same order, converted into hashtags using `hashtagify.py`.

Each file has 25,000 lines. The text is Unicode encoded in UTF-8. Most of the text is in English, but not all of it.

The text is arbitrarily sampled from tweets collected in late 2013. Aside from limiting it to all-caps phrases likely to be in English, we have only minimally filtered it. Some of the text content may be offensive, and a *lot* of it may be insipid, and for that we apologize in advance.

## What to send us

Send us a `.zip` or `.tar.gz` file of all the code you used to accomplish the task to `hiring@luminoso.com`. Include the evaluation results, with precision, recall, and F-score, in a text file.

You can write your code in Python 2 or 3, and use any external Python packages you want, as long as they're publicly available.

We're not going to use your code for any purpose except to see if you solved the task well. Submitting your code sample will impress us, not further our current projects.

We do want to be able to run it, especially so we can see how it performs on different data from the included training and test data. To that end, please include a list of any external packages you depend on (a Pip `requirements.txt` file or a Setuptools `setup.py` file will do nicely), and include instructions on how to set up your code if it's non-trivial.
