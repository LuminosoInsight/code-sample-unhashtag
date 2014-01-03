import sys

def hashtagify(text):
    return '#' + text.lower().replace(' ', '').replace("'", '')

if __name__ == '__main__':
    for line in sys.stdin:
        line = line.decode('utf-8').strip()
        print(hashtagify(line).encode('utf-8'))
