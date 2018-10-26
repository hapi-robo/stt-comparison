#!/usr/bin/env python
# coding: utf8

"""Japanese speech corpus of Saruwatari-lab., University of Tokyo (JSUT)

Codec: PCM S16 LE (s16l)
Channels: Mono
Sample Rate 48000 Hz
Bits per sample: 16

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
import Levenshtein


def compare_string(s1, s2):
    """ Compute Levenshtein distance and ratio 
        
    Args:
        s1 (str): First string.
        s2 (str): Second string.

    Returns:
        distance (int): Levenshtein distance.
        ratio (float): Levenstein ratio.

    Todo: 
        This may not be the best metric to use for comparing speech 
        transcription.

    References:
        https://en.wikipedia.org/wiki/Levenshtein_distance
        https://rawgit.com/ztane/python-Levenshtein/master/docs/Levenshtein.html

    """
    distance = Levenshtein.distance(string1, string2)
    ratio = Levenshtein.ratio(string1, string2)
    print("Distance:", distance)
    print("Ratio:", ratio)
    return distance, ratio

def strip_punctuation(s):
    """ Strip Japanese symbols and punctuation

    Args:
        s (str): String that may contain Japanese symbols and/or 
            punctuations.

    Returns:
        str: String without Japanese symbols and/or punctuations.

    References:
        http://www.localizingjapan.com/blog/2012/01/20/regular-expressions-for-japanese-text/
        https://regex101.com/r/cO8lqs/2
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
            # print(row[1]) # print original transcript
            print(strip_punctuation(row[1])) # print processed transcript
            print(args.path + 'wav/' + row[0] + '.wav') # print file path
            print('\n')
