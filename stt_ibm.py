#!/usr/bin/env python

"""Test IBM Watson Speech to Text API (https://www.ibm.com/watson/services/speech-to-text/).

Example usage:
    python transcribe.py audio.wav

Notes:
- https://github.com/watson-developer-cloud/python-sdk
- https://console.bluemix.net/docs/services/speech-to-text/audio-formats.html#audio-formats
- A localized version of this Watson service is available in Japan. Visit the following link for details: http://www.softbank.jp/biz/watson

"""

from __future__ import print_function

import os
import time
import argparse
from watson_developer_cloud import SpeechToTextV1

def transcribe(filename):
    # Location: Sydney
    service = SpeechToTextV1(
        iam_apikey=os.environ['IAM_APIKEY'],
        url=os.environ['URL'])

    # Location: US South
    # service = SpeechToTextV1(
    #     username='0bd3eb37-95f0-4f93-a46a-46adce7984b8',
    #     password='ZlwSjChnmBoI',
    #     url='https://stream.watsonplatform.net/speech-to-text/api')

    with open(filename, 'rb') as audio_file:
        start = time.time()
        response = service.recognize(
            audio=audio_file,
            content_type='audio/l16; rate=16000',
            model='ja-JP_BroadbandModel').get_result()
        end = time.time();

    # print(response) # raw response
    print(response['results'][0]['alternatives'][0]['transcript'])
    print("Elapsed Time:", end - start)


if __name__ == '__main__':
    # handle arguments
    parser = argparse.ArgumentParser(description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        'path', help='File path for audio file to be transcribed')
    args = parser.parse_args()
    
    transcribe(args.path)
