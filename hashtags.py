from __future__ import unicode_literals, print_function
import sys
import os
import io


THIS_DIR = os.path.dirname(os.path.realpath(__file__))
DATA_DIR = THIS_DIR + '/data'
PYTHON2 = (sys.version_info[0] == 2)
if PYTHON2:
    from itertools import izip
else:
    izip = zip


def iter_lines(filename):
    """
    Given a filename, returns an iterator of Unicode strings for the lines
    in that file, with line-breaks stripped.
    """
    for line in io.open(filename, encoding='utf-8'):
        yield line.rstrip()


class Unhashtagger(object):
    """
    The job of the Unhashtagger is to restore spaces in text that has had its
    spaces removed. It should take in lowercase text, preceded by a # symbol
    and with no spaces, and output capitalized text with spaces in it, based
    on a reasonable prediction of where the spaces should go.

    What we've implemented here, as a baseline, is terrible at doing this job.
    It never learns anything from training data. All it does is insert a space
    after every letter 'e'.

    Your job is to replace this heuristic with something reasonably good.
    """
    def __init__(self):
        # TODO: Set up whatever state you need to.
        pass

    def to_hashtag(self, text):
        """
        Convert text with spaces to a 'hashtag' without spaces.
        """
        return '#' + text.lower().replace(' ', '')

    def train(self, examples):
        """
        Takes an in iterator of training examples, containing text in all caps
        with spaces. These are the desired outputs. You can convert these to
        their corresponding inputs using the `to_hashtag` method.
        """
        for all_caps_text in examples:
            pass
            # TODO: You should probably do something with the training
            # examples.

    def from_hashtag(self, text):
        """
        Converts text in hashtag form to uppercase text with its spaces restored.

        The implementation we've got here is an utterly terrible baseline. Because
        most tweets are in English, and lots of English words end in 'e', this
        function just inserts a space after every letter 'e'. You can definitely
        do better than that.
        """
        # TODO
        return text.lstrip('#').replace('e', 'e ').upper().strip()

    def evaluate(self):
        """
        Please don't change this method.

        This method evaluates the accuracy of the Unhashtagger after it's been
        trained. It measures the precision (what proportion of the spaces it
        outputs are there in the training data), recall (what proportion of the
        spaces in the training data it outputs), and F_1 score (the harmonic
        mean of precision and recall).

        Your goal is to make the F_1 score as high as possible.
        """
        precision_correct = precision_total = recall_correct = recall_total = 0
        for hashtag, gold_standard in izip(
            iter_lines(DATA_DIR + '/testing_hashtags.txt'),
            iter_lines(DATA_DIR + '/testing_orig.txt')
        ):
            unhashtagged = self.from_hashtag(hashtag)
            if unhashtagged.startswith('#'):
                raise ValueError("You should remove the # symbol in from_hashtag.")
            pos1 = 0
            pos2 = 0
            while pos2 < len(gold_standard):
                if pos1 >= len(unhashtagged):
                    raise ValueError(
                        "Your output ended too soon. The gold standard text is "
                        "%r, but your text is %r. Text remaining: %r" % (
                            gold_standard, unhashtagged, gold_standard[pos2:]
                        )
                    )
                output_char = unhashtagged[pos1]
                gold_char = gold_standard[pos2]
                if output_char == ' ' and gold_char == ' ':
                    # True positive
                    precision_correct += 1
                    recall_correct += 1
                    precision_total += 1
                    recall_total += 1
                    pos1 += 1
                    pos2 += 1
                elif output_char == ' ':
                    # False positive
                    precision_total += 1
                    pos1 += 1
                elif gold_char == ' ':
                    # False negative
                    recall_total += 1
                    pos2 += 1
                elif output_char == gold_char:
                    # Ordinary matching characters
                    pos1 += 1
                    pos2 += 1
                else:
                    raise ValueError(
                        "These characters didn't match. The gold standard text is %r, "
                        "and your text is %r. The gold standard has %r where your text "
                        "has %r." % (gold_standard, unhashtagged, gold_char, output_char)
                    )
        precision = float(precision_correct) / precision_total
        recall = float(recall_correct) / recall_total
        f1 = (2 * precision * recall) / (precision + recall)
        return {
            'precision': precision,
            'recall': recall,
            'f1': f1
        }


def main():
    """
    Convert text with spaces on standard input, to text without spaces on
    standard output. This version runs on Python 2.
    """
    unhashtagger = Unhashtagger()
    unhashtagger.train(iter_lines(DATA_DIR + '/training_orig.txt'))
    results = unhashtagger.evaluate()

    print('Precision: %5.2f%%' % (results['precision'] * 100))
    print('Recall:    %5.2f%%' % (results['recall'] * 100))
    print('F1 score:  %5.2f%%' % (results['f1'] * 100))



if __name__ == '__main__':
    main()

