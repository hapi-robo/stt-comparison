#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Japanese Speech Corpus of Saruwatari-Lab., University of Tokyo (JSUT)

File specifications:
- Codec: PCM S16 LE (s16l)
- Channels: Mono
- Sample Rate 48000 Hz
- Bits per sample: 16

Reference:
Ryosuke Sonobe, Shinnosuke Takamichi and Hiroshi Saruwatari,  "JSUT corpus: 
free large-scale Japanese speech corpus for end-to-end speech synthesis," 
arXiv preprint, 1711.00354, 2017. (https://arxiv.org/pdf/1711.00354.pdf)
https://sites.google.com/site/shinnosuketakamichi/publication/jsut

Example usage:
    python test_jsut jsut_ver1.1/basic5000/ filename.csv

"""

import os
import argparse
import csv
import regex as re
import Levenshtein
import datetime

from itertools import islice
# from stt_google import transcribe as google_transcribe
# from stt_wit import transcribe as wit_transcribe
# from stt_ibm import transcribe as ibm_transcribe
from stt_fuetrek import transcribe as fuetrek_transcribe

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
    distance = Levenshtein.distance(s1, s2)
    ratio = Levenshtein.ratio(s1, s2)
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
                # audio_file = args.path + 'wav/' + row[0] + '.wav' # use for google, ibm, wit
                audio_file = args.path + 'wav/' + row[0] + '.raw' # use for fuetrek only
                
                # transcribe audio
                tru_transcript = strip_punctuation(row[1]).decode('utf-8', 'ignore')

                # stt_transcript, proc_time, confidence = google_transcribe(audio_file, sample_rate=48000)
                # stt_transcript, proc_time, confidence = ibm_transcribe(audio_file, sample_rate=48000)
                # stt_transcript, proc_time, confidence = wit_transcribe(audio_file)
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
