# unhashtag: a coding challenge

Are you interested in working for [Luminoso](http://luminoso.com)? Great! We'd like to see what your Python code looks like, and how good you are at doing messy things with messy text.

We're not going to use your code for any purpose except to see if you solved the task well. Submitting your code sample will impress us, not further our current projects.

## Task: How do you separate words in Twitter hashtags?

It is, of course, a time-honored tradition on the Internet to WRITE THINGS IN ALL CAPS when you want to emphasize them and also be annoying.

The popularity of Twitter, however, has created a new way to annoyingly emphasize things: by running all the words together and making them into a hashtag.

    Before: HEY PAY ATTENTION TO ME
    After: #heypayattentiontome

In this repository, we've created a data set that takes this to its natural conclusion. We extracted 50,000 all-caps phrases from Twitter, and made an alternate version of them that converts them to a lowercase hashtag, with no spaces or apostrophes.

Your task is to write Python code that reverses this process, determining where to insert spaces into the hashtags to separate them into words again.

## What you need to do

The code we provide contains one Python module, `hashtags.py`, containing the Unhashtagger class. It contains code to evaluate a solution to the task, along with a really bad baseline solution. You should modify this class, particularly the `train` and `from_hashtag` methods, so that it can solve the task reasonably competently.

When you run `hashtags.py` as a script, it will train the Unhashtagger on the training data, then evaluate it on the test data, outputting these statistics:

* *Precision*: of the spaces you output, what proportion of them are correct?
* *Recall*: of the spaces in the test data, what proportion of them do you correctly output?
* Your *F1 score* is (2 * *precision* * *recall*) / (*precision* + *recall*).

We are looking for code that is written with good style, is reasonably efficient, and solves the problem well (as measured by the F1 score). The baseline scores an abysmal 20.4%. We'd like to see your solution score at least 80%.

You can write your code in Python 2 or 3, and use Python libraries to whatever extent is appropriate.

## The data files

* `data/training_orig.txt` and `data/testing_orig.txt` contain all-caps phrases with spaces.
* `data/training_hashtags.txt` and `data/testing_hashtags.txt` contain the same phrases, in the same order, converted into hashtags using `hashtagify.py`.

The training files have 1,304,197 lines, and the testing files have 10,000 lines. The text is Unicode encoded in UTF-8. All of the text uses the Latin alphabet, but not all of it is in English.

The text is arbitrarily sampled from tweets collected in 2015. Aside from limiting it to all-caps phrases, we have only minimally filtered it. Some of the text content may be offensive, and a *lot* of it may be insipid, and for that we apologize in advance.

## Submitting your code

Send us a `.zip` or `.tar.gz` file of all the code you used to accomplish the task to `hiring@luminoso.com`. Include a text file that describes your approach and our evaluation results. Please send it only to us, and don't make your code publicly available.

We review code samples anonymously, so please **do not put your name** in any of your files or filenames.

We do want to be able to run it, especially so we can see how it performs on different data from the included training and test data. To that end, please include a list of any external packages you depend on (a Pip `requirements.txt` file will do nicely), and include instructions on how to set up your code if it's non-trivial.
