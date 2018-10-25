#!/usr/bin/env python

"""Japanese speech corpus of Saruwatari-lab., University of Tokyo (JSUT)

Reference:
Ryosuke Sonobe, Shinnosuke Takamichi and Hiroshi Saruwatari,  "JSUT corpus: 
free large-scale Japanese speech corpus for end-to-end speech synthesis," 
arXiv preprint, 1711.00354, 2017. (https://arxiv.org/pdf/1711.00354.pdf)

Example usage:
    python test_jsut jsut_ver1.1/basic5000/
"""

import os
import argparse
import csv
import regex as re


def strip_punctuation(s):
    """ Strip Japanese symbols and punctuation
    - http://www.localizingjapan.com/blog/2012/01/20/regular-expressions-for-japanese-text/
    - https://regex101.com/r/cO8lqs/2
    """
    return re.sub(u'[\u3000-\u303F]', "", s)

if __name__ == '__main__':
    # handle arguments
    parser = argparse.ArgumentParser(description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        'path', help='JSUT file path for data to be tested')
    args = parser.parse_args()

    # args.path = 'resources/jsut_ver1.1/basic5000/'
    with open(args.path + 'transcript_utf8.txt', 'r') as f:
        csv_reader = csv.reader(f, delimiter=':')
        for row in csv_reader:
            transcript = strip_punctuation(row[1]);
            print(row[1]) # print original transcription
            print(transcript) # print processed transcription
            print(args.path + 'wav' + row[0] + '.wav') # print file path
            print('\n')
