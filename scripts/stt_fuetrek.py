#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Speech to text using Fuetrek's Speech-to-Text API.

Example usage:
    python stt_fuetrek.py /path/to/audio/sample.wav

Notes:
	- Audio sampling rate must be 16 kHz
"""

import os
import time
import argparse
import requests
import json

SERVICE_ADDRESS = "172.16.0.41:3000"

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
	response = None

	with open(filename, 'rb') as audio_file:
		start_time = time.time();
		response = requests.post(url="http://" + SERVICE_ADDRESS + "/fuetrek_stt_api/", 
								data=audio_file, 
								headers={'Content-Type': 'application/json'})
		proc_time = time.time() - start_time

	response.encoding = 'utf-8'
	transcript = response.json()['transcript']
	confidence = response.json()['confidence'] / 100.0

	if verbose:
		print(transcript)
		print("Elapsed Time: {:.3f} seconds".format(proc_time))
		print("Confidence Level: {:.3f}".format(confidence))

	return transcript, proc_time, confidence


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        'path', help='File path for audio file to be transcribed')
    args = parser.parse_args()
    
    transcribe(args.path, verbose=True)
