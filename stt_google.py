#!/usr/bin/env python

"""Test Google Cloud Speech-to-Text API (https://cloud.google.com/speech-to-text/).

Example usage:
    python transcribe.py audio.wav

"""

import time
import argparse
import io

def transcribe(filename):
    from google.cloud import speech
    from google.cloud.speech import enums
    from google.cloud.speech import types
    client = speech.SpeechClient()

    with io.open(filename, 'rb') as audio_file:
        content = audio_file.read()

    audio = types.RecognitionAudio(content=content)

    # https://cloud.google.com/speech-to-text/docs/recognition-metadata
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code='ja')

    start = time.time();
    response = client.recognize(config, audio)
    end = time.time();
    
    # Iterate through consecutive portions of the audio to get 
    # the complete audio transcript.
    # print(response) # raw response
    for result in response.results:
        print(result.alternatives[0].transcript)

    print("Elapsed Time:", end - start);


if __name__ == '__main__':
    # handle arguments
    parser = argparse.ArgumentParser(description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        'path', help='File path for audio file to be transcribed')
    args = parser.parse_args()
    
    transcribe(args.path)
