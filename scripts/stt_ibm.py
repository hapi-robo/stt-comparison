#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Speech to text using IBM Watson Speech to Text API.

Example usage:
    python transcribe.py audio.wav

References:
    https://www.ibm.com/watson/services/speech-to-text/
    https://github.com/watson-developer-cloud/python-sdk
    https://console.bluemix.net/docs/services/speech-to-text/audio-formats.html#audio-formats
    
    A localized version of this Watson service is available in Japan. 
    Visit the following link for details: http://www.softbank.jp/biz/watson

"""

# from __future__ import print_function

import os
import time
import argparse

from watson_developer_cloud import SpeechToTextV1


def transcribe(
    filename,
    sample_rate=16000,
    verbose=True):
    """Convert speech to text

    Args:
        filename (str): Path to audio file.

    Returns:
        transcript (str): Transcription of audio file.
        proc_time (float): STT processing time.

    """
    # Service Location: Sydney
    service = SpeechToTextV1(
        iam_apikey=os.environ['IAM_APIKEY'],
        url=os.environ['URL'])

    # Service Location: US South
    # service = SpeechToTextV1(
    #     username='0bd3eb37-95f0-4f93-a46a-46adce7984b8',
    #     password='ZlwSjChnmBoI',
    #     url='https://stream.watsonplatform.net/speech-to-text/api')

    with open(filename, 'rb') as audio_file:
        start_time = time.time()
        response = service.recognize(
            audio=audio_file,
            content_type='audio/l16; rate=' + int2str(sample_rate),
            model='ja-JP_BroadbandModel').get_result()
        proc_time = time.time() - start_time

    transcript = response['results'][0]['alternatives'][0]['transcript']; 

    if verbose:
        print(transcript)
        print("Sampling Rate:", sample_rate)
        print("Elapsed Time:{:.3f}".format(proc_time))

    return transcript, proc_time


if __name__ == '__main__':
    # handle arguments
    parser = argparse.ArgumentParser(description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        'path', help='File path for audio file to be transcribed')
    parser.add_argument(
        '--rate', help='Sampling rate [Hz]', type=int)
    args = parser.parse_args()
    
    transcribe(args.path, sample_rate=args.rate, verbose=True)
