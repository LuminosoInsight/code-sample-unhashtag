# unhashtag: a coding challenge

Are you interested in working for [Luminoso](http://luminoso.com)? Great! We'd like to see what your code looks like, and how good you are at doing messy things with messy text.

## Task: How do you separate words in Twitter hashtags?

It is, of course, a time-honored tradition on the Internet to WRITE THINGS IN ALL CAPS when you want to emphasize them and also be annoying.

The popularity of Twitter, however, has created a new way to annoyingly emphasize things: by running all the words together and making them into a hashtag.

    Before: HEY PAY ATTENTION TO ME
    After: #heypayattentiontome

In this repository, we've created a data set that takes this to its natural conclusion. We extracted 50,000 all-caps phrases from Twitter, and made an alternate version of them that converts them to a lowercase hashtag, with no spaces or apostrophes. `hashtagify.py` is a very simple script that performs this operation.

Your task is to write a Python script that **reverses the process** as accurately as possible.

An outline of what you'll need to do:

* Write code that builds a model of where spaces belong, using whatever techniques you like. You'll probably want to use the training files for this.
* Write an "unhashtagifier", code that uses this model to convert hashtags into all-caps phrases with spaces. (Don't worry about apostrophes unless you really want to.)
* Write evaluation code that runs your unhashtagifier on the testing files, and measures how often it puts spaces in the correct places. Output your precision and recall, or alternatively, your rate of false positives and false negatives.

## The data files

* `data/training_orig.txt` and `data/testing_orig.txt` contain all-caps phrases with spaces.
* `data/training_hashtags.txt` and `data/testing_hashtags.txt` contain the same phrases, in the same order, converted into hashtags using `hashtagify.py`.

Each file has 25,000 lines. The text is Unicode encoded in UTF-8. Most of the text is in English, but not all of it.

The text is pseudo-randomly sampled from tweets collected in late 2013. Aside from limiting it to all-caps phrases, we have only minimally filtered it. Some of the text content may be offensive, and a *lot* of it may be insipid, and for that we apologize in advance.

## What to send us

Send us a `.zip` or `.tar.gz` file of all the code you used to accomplish the task. If you depend on publically-available Python packages, include a list of those packages (a Pip `requirements.txt` file or a Setuptools `setup.py` file will do nicely). Include the evaluation results in a text file.

We hope to be able to run the code you send us, on different data than the included training and test data.
