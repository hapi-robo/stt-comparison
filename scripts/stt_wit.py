#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Speech to text using wit.ai Speech-to-Text API.

Example usage:
    python stt_wit.py /path/to/audio/sample.wav

Notes:
	- Default sampling rate is 16 kHz
	- Language must be predefined in the user-interface
	- There isn't a lot of detail regarding the desired audio format, see: https://github.com/wit-ai/wit/issues/217
	- No confidence level provided, default to 1.0
	
References:
	- https://wit.ai/
	- https://github.com/wit-ai/pywit
	- https://www.liip.ch/en/blog/speech-recognition-with-wit-ai
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
		transcript (unicode, utf-8): Transcription of audio file.
		proc_time (float): STT processing time.
		confidence (float): None provided, so default to 1.0.

	"""
	service = Wit(os.environ['SERVER_ACCESS_TOKEN']); # server access token

	response = None
	with open(filename, 'rb') as audio_file:
		start_time = time.time();
		response = service.speech(audio_file, None, {'Content-Type': 'audio/wav'})
		proc_time = time.time() - start_time

	transcript = response['_text']

	if verbose:
		print("Filename: {}".format(filename))
		print(transcript)
		print("Elapsed Time: {:.3f} seconds".format(proc_time))
		print("Confidence: None Provided")

	return transcript, proc_time, 1.0


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        'path', help='File path for audio file to be transcribed')
    args = parser.parse_args()
    
    transcribe(args.path, verbose=True)
