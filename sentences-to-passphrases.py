#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import codecs
import string
import re
import sys


def generate_passphrases_from_sentence(sentence, word_count, with_spaces):
    words = sentence.strip().split()
    length = len(words)
    i = 0

    while i <= length - word_count:
        w = words[i:i+word_count]
        if with_spaces:
            p = " ".join(w)
        else:
            p = "".join(w)

        if len(p) > 12:
            yield p

        i += 1


def generate_passphrases_from_stream(stream, word_count, with_spaces):
    valid_characters = string.lowercase + string.digits + u"çéâêîôûàèùëïü" + ",.':;$ "
    number_editor_regex = re.compile(r'(?<=\d)[,. ](?=\d)')
    period_replace_regex = re.compile(r'[,:;!?]')

    for line in stream:
        line = line.strip().lower()
        line = number_editor_regex.sub('', line)
        line = period_replace_regex.sub('.', line)
        line = u"".join([c for c in line if c in valid_characters]).encode('utf-8')
        if not line:
            continue

        for sentence in [p for p in line.split('.') if p]:
            for passphrase in generate_passphrases_from_sentence(sentence, word_count, with_spaces):
                print passphrase


parser = argparse.ArgumentParser(description='Creates passphrases from sentences.')
parser.add_argument('--file', '-f', action='store', dest='file', default=None, help='Path to the sentences file.')
parser.add_argument('--with-spaces', action="store_true", dest='with_spaces', default=False, help="Indicates if the passphrases should contain spaces or not.")
parser.add_argument('--word-count', '-c', action="store", dest='word_count', default=4, type=int, help='The number of words in the passphrases.')
args = parser.parse_args()

if args.file is not None:
    with codecs.open(args.file, 'r', encoding='utf-8') as f:
        generate_passphrases_from_stream(f, args.word_count, args.with_spaces)
else:
    with codecs.getreader('utf-8')(sys.stdin) as f:
        generate_passphrases_from_stream(f, args.word_count, args.with_spaces)
