#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Speech to text using Google Cloud Speech-to-Text API.
    
Example usage:
    python transcribe.py audio.wav

References:
    https://cloud.google.com/speech-to-text/

"""

import time
import argparse
import io

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
        transcript (str): Transcription of audio file.
        proc_time (float): STT processing time.

    References:
        https://cloud.google.com/speech-to-text/docs/recognition-metadata

    """
    service = speech.SpeechClient()

    with io.open(filename, 'rb') as audio_file: # <------------- why is io.open used here??
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
    transcript = ""
    for result in response.results:
        transcript += result.alternatives[0].transcript 
    
    if verbose:
        print(transcript)
        print("Sampling Rate:", sample_rate)
        print("Language Code:", language_code)
        print("Elapsed Time: {:.3f} seconds".format(proc_time))

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