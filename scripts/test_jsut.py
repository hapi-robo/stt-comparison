#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test JSUT against various STT or ASR platforms

Japanese Speech Corpus of Saruwatari-Lab., University of Tokyo (JSUT)

Reference:
Ryosuke Sonobe, Shinnosuke Takamichi and Hiroshi Saruwatari,  "JSUT corpus: 
free large-scale Japanese speech corpus for end-to-end speech synthesis," 
arXiv preprint, 1711.00354, 2017. (https://arxiv.org/pdf/1711.00354.pdf)
https://sites.google.com/site/shinnosuketakamichi/publication/jsut

File specifications:
- Codec: PCM S16 LE (s16l)
- Channels: Mono
- Sample Rate 48000 Hz
- Bits per sample: 16

Usage:
    python test_jsut [STT platform] [Path to JSUT] [CSV file]

Example usage:
    python test_jsut google jsut_ver1.1/basic5000/ filename.csv

Note:
    You must use an appropriate virtual environment for the STT platform
    you intend to test on. 

"""

import os
import argparse
import csv
import regex as re
import Levenshtein
import datetime

from itertools import islice

try:
    from stt_google import transcribe as google_transcribe
except ImportError:
    print "[WARNING] Cannot use Google STT"

try:
    from stt_wit import transcribe as wit_transcribe
except ImportError:
    print "[WARNING] Cannot use wit.ai STT"

try:
    from stt_ibm import transcribe as ibm_transcribe
except ImportError:
    print "[WARNING] Cannot use IBM STT"

try:
    from stt_fuetrek import transcribe as fuetrek_transcribe
except ImportError:
    print "[WARNING] Cannot import Fuetrek STT"


def compare_string(s1, s2):
    """ Compute Levenshtein distance and ratio 

    Levenshtein distance (LD) is a measure of the similarity between two strings, 
    which we will refer to as the source string (s) and the target string (t). 
    The distance is the number of deletions, insertions, or substitutions required 
    to transform s into t.
        
    Args:
        s1 (str/unicode): First string or unicode
        s2 (str/unicode): Second string or unicode

    Returns:
        distance (int): Levenshtein distance.
        ratio (float): Levenstein ratio.

    Todo: 
        This may not be the best metric to use for comparing speech 
        transcription in Japanese.


    References:
        https://en.wikipedia.org/wiki/Levenshtein_distance
        https://rawgit.com/ztane/python-Levenshtein/master/docs/Levenshtein.html

    """
    distance = Levenshtein.distance(s1, s2)
    ratio = Levenshtein.ratio(s1, s2)
    return distance, ratio

def strip_punctuation(s):
    """ Strip Japanese symbols and punctuation

    Args:
        s (str): String that may contain Japanese symbols and/or 
            punctuations.

    Returns:
        unicode (utf-8): String without Japanese symbols and/or punctuations.

    References:
        http://www.localizingjapan.com/blog/2012/01/20/regular-expressions-for-japanese-text/
        https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/
        https://regex101.com/r/cO8lqs/2
    """
    u = unicode(s, "utf-8")
    return re.sub(ur'[\u3000-\u303F]', "", u, flag=re.UNICODE)

if __name__ == '__main__':
    # handle arguments
    parser = argparse.ArgumentParser(description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        'stt', help='STT platform; choose from: google, ibm, wit, or fuetrek')
    parser.add_argument(
        'path', help='JSUT file path for data to be tested')
    parser.add_argument(
        'csv_filename', help='Filename of CSV to store data')
    args = parser.parse_args()

    # open CSV file for writing
    with open(args.csv_filename, mode='w') as csv_file:
        fieldnames = ['File Name', 'True Transcript', 'STT Transcript', 
            'Processing Time', 'Levenshtein Distance', 'Levenshtein Ratio', 'Confidence']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        # step through all audio samples;
        # note that transcript file contains the file names of all audio samples 
        with open(args.path + 'transcript_utf8.txt', 'r') as transcript_file:
            csv_reader = csv.reader(transcript_file, delimiter=':')
            for row in csv_reader:
            # for row in islice(csv_reader, 1, 100):

                # copy true transcript to memory
                tru_transcript = strip_punctuation(row[1])

                # transcribe audio
                if args.stt == 'google':
                    audio_file = args.path + 'wav/' + row[0] + '.wav'
                    stt_transcript, proc_time, confidence = google_transcribe(audio_file, sample_rate=48000)
                elif args.stt == 'ibm':
                    audio_file = args.path + 'wav/' + row[0] + '.wav'
                    stt_transcript, proc_time, confidence = ibm_transcribe(audio_file, sample_rate=48000)
                elif args.stt == 'wit':
                    audio_file = args.path + 'wav/' + row[0] + '.wav'
                    stt_transcript, proc_time, confidence = wit_transcribe(audio_file)
                elif args.stt == 'fuetrek':
                    audio_file = args.path + 'wav/' + row[0] + '.raw'
                    stt_transcript, proc_time, confidence = fuetrek_transcribe(audio_file)
                
                # evaluate performance
                l_distance, l_ratio = compare_string(stt_transcript, tru_transcript)

                # save transcript and performance data to CSV file
                print(os.path.basename(audio_file))
                writer.writerow({
                    'File Name': os.path.basename(audio_file), 
                    'True Transcript': tru_transcript.encode('utf-8'),
                    'STT Transcript': stt_transcript.encode('utf-8'),
                    'Processing Time': proc_time, 
                    'Levenshtein Distance': l_distance,
                    'Levenshtein Ratio': l_ratio,
                    'Confidence': confidence})

                # print to console
                print(audio_file)
                print("STT: {}".format(stt_transcript.encode('utf-8')))
                print("TRU: {}".format(tru_transcript.encode('utf-8')))
                print("Processing Time: {:.3f}".format(proc_time))
                print("Levenshtein Distance: {}, Ratio: {:.3f}".format(l_distance, l_ratio))
                print("Confidence: {:.3f}".format(confidence))
                print("\n")
