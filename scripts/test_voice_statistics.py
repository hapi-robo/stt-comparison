#!/usr/bin/env python

"""Voice Statistics. http://voice-statistics.github.io/

Codec: PCM S16 LE (s16l)
Channels: Mono
Sample Rate 48000 Hz
Bits per sample: 16

Reference:
@misc{vsdataset,
author = {y\_benjo and MagnesiumRibbon},
title = {Voice-Actress Corpus},
howpublished = {\url{http://voice-statistics.github.io/}
}

Example usage:
    python test_voice_statistics voice-statistics.github.com/

Todo:
    Combine this with test_jsut.py

"""

import os
import argparse
import csv


if __name__ == '__main__':
    # handle arguments
    parser = argparse.ArgumentParser(description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        'path', help='JSUT file path for data to be tested')
    args = parser.parse_args()

    # args.path = 'resources/voice-statistics.github.com/'
    with open(args.path + 'assets/doc/balance_sentences.txt', 'r') as f:
        csv_reader = csv.reader(f, delimiter='\t')
        for row in csv_reader:
            audio_file = args.path + 'assets/data/fujitou_angry/fujitou_angry_' + row[0] + '.wav'
            audio_file = args.path + 'assets/data/fujitou_happy/fujitou_happy_' + row[0] + '.wav'
            audio_file = args.path + 'assets/data/fujitou_normal/fujitou_normal_' + row[0] + '.wav'
            audio_file = args.path + 'assets/data/tsuchiya_angry/tsuchiya_angry_' + row[0] + '.wav'
            audio_file = args.path + 'assets/data/tsuchiya_happy/tsuchiya_happy_' + row[0] + '.wav'
            audio_file = args.path + 'assets/data/tsuchiya_happy/tsuchiya_happy_' + row[0] + '.wav'
            audio_file = args.path + 'assets/data/uemura_angry_angry/uemura_angry_angry_' + row[0] + '.wav'
            audio_file = args.path + 'assets/data/uemura_angry_happy/uemura_angry_happy_' + row[0] + '.wav'
            audio_file = args.path + 'assets/data/uemura_angry_happy/uemura_angry_happy_' + row[0] + '.wav'
            audio_file = args.path + 'assets/data/hiroshiba_normal/hiroshiba_normal_' + row[0] + '.wav'
            
            # transcribe audio
            tru_transcript = row[1]
            # stt_transcript, proc_time = ...

            # print to console
            print(audio_file)
            print("STT:", stt_transcript)
            print("TRUE:", tru_transcript)
            print('\n')
