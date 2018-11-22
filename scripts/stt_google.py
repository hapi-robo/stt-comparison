#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Speech to text using Google Cloud Speech-to-Text API.
    
Example usage:
    python stt_google.py /path/to/audio/sample.wav

Notes:
    - Default sampling rate is 16 kHz

References:
    - https://cloud.google.com/speech-to-text/
"""

import time
import argparse

from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types


def transcribe(
    filename, 
    sample_rate=16000,
    verbose=True):
    """Convert speech to text 
        
    Args:
        filename (str): Path to audio file.

    Returns:
        transcript (unicode, utf-8): Transcription of audio file.
        proc_time (float): STT processing time.
        confidence (float): Normalized confidence level.

    References:
        https://cloud.google.com/speech-to-text/docs/recognition-metadata

    """
    service = speech.SpeechClient()

    with open(filename, 'rb') as audio_file:
        content = audio_file.read()

    audio = types.RecognitionAudio(content=content)
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=sample_rate,
        language_code='ja')

    start_time = time.time();
    response = service.recognize(config, audio)
    proc_time = time.time() - start_time

    # iterate through consecutive portions of the audio to get 
    # the complete audio transcript.
    for result in response.results:
        transcript = result.alternatives[0].transcript 
        confidence = result.alternatives[0].confidence

    if verbose:
        print("Filename: {}".format(filename))
        print(transcript)
        print("Sampling Rate: {} Hz".format(sample_rate))
        print("Elapsed Time: {:.3f} seconds".format(proc_time))
        print("Confidence Level: {}".format(confidence))

    return transcript, proc_time, confidence


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        'path', help='File path for audio file to be transcribed')
    parser.add_argument(
        '--rate', help='Sampling rate [Hz]', type=int)
    args = parser.parse_args()
    
    if len(vars(args)) > 2:
        transcribe(args.path, sample_rate=args.rate, verbose=True)
    else:
        transcribe(args.path, verbose=True)