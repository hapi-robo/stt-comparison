#!/usr/bin/env python

"""Test wit.ai Speech-to-Text API (https://wit.ai/).

Example usage:
    python transcribe.py audio.wav

Notes:
- https://wit.ai/docs
- https://github.com/wit-ai/pywit
- https://www.liip.ch/en/blog/speech-recognition-with-wit-ai
- There isn't much detail provided on the desired audio format: 
- https://github.com/wit-ai/wit/issues/217

"""

import os
import time
import argparse
from wit import Wit


def transcribe(filename):
	client = Wit(os.environ['SERVER_ACCESS_TOKEN']); # server access token

	response = None
	with open(filename, 'rb') as f:
		start = time.time();
		response = client.speech(f, None, {'Content-Type': 'audio/wav'})
		end = time.time();

	# print(response); # raw response
	print((response['_text']))
	print("Elapsed Time:", end - start)


if __name__ == '__main__':
    # handle arguments
    parser = argparse.ArgumentParser(description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        'path', help='File path for audio file to be transcribed')
    args = parser.parse_args()
    
    transcribe(args.path)
