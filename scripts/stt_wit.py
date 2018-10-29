#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Speech to text using wit.ai Speech-to-Text API.

Example usage:
    python transcribe.py audio.wav

References:
	https://wit.ai/
	https://github.com/wit-ai/pywit
	https://www.liip.ch/en/blog/speech-recognition-with-wit-ai

	There isn't a lot of detail regarding the desired audio format: 
	- https://github.com/wit-ai/wit/issues/217

	Language must be set in the user-interface

"""

import os
import time
import argparse

from wit import Wit


def transcribe(
	filename,
	verbose=True):
	"""Convert speech to text

	Args:
		filename (str): Path to audio file.

	Returns:
		transcript (str): Transcription of audio file.
		proc_time (float): STT processing time.

	"""
	client = Wit(os.environ['SERVER_ACCESS_TOKEN']); # server access token

	response = None
	with open(filename, 'rb') as f:
		start_time = time.time();
		response = client.speech(f, None, {'Content-Type': 'audio/wav'})
		proc_time = time.time() - start_time

	transcript = response['_text']

	if verbose:
		print(transcript)
		print("Elapsed Time: {:.3f} seconds".format(proc_time))

	return transcript, proc_time


if __name__ == '__main__':
    # handle arguments
    parser = argparse.ArgumentParser(description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        'path', help='File path for audio file to be transcribed')
    args = parser.parse_args()
    
    transcribe(args.path, verbose=True)
