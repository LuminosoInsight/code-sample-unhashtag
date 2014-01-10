from __future__ import unicode_literals
import sys


def hashtagify(text):
    """
    Convert text with spaces to a 'hashtag' without spaces.
    """
    return '#' + text.lower().replace(' ', '').replace("'", '')


def py2_main():
    """
    Convert text with spaces on standard input, to text without spaces on
    standard output. This version runs on Python 2.
    """
    for line in sys.stdin:
        line = line.decode('utf-8')
        print(hashtagify(line.strip()).encode('utf-8'))


def py3_main():
    """
    Convert text with spaces on standard input, to text without spaces on
    standard output. This version runs on Python 3.
    """
    for line in sys.stdin:
        print(hashtagify(line.strip()))


if __name__ == '__main__':
    if sys.version_info[0] == 2:
        py2_main()
    else:
        py3_main()
