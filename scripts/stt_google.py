#!/usr/bin/env python

"""Test Google Cloud Speech-to-Text API (https://cloud.google.com/speech-to-text/).

Example usage:
    python transcribe.py audio.wav

"""

import time
import argparse
import io


def transcribe(
    filename, 
    sample_rate=16000, 
    language_code='ja',
    verbose=True):
    """ Convert speech to text 
        
    Args:
        filename (str): Path to audio file.

    Returns:
        transcript (str): Transcription of audio file.
        proc_time (float): STT processing time.

    References:
        https://cloud.google.com/speech-to-text/docs/recognition-metadata

    """
    from google.cloud import speech
    from google.cloud.speech import enums
    from google.cloud.speech import types
    client = speech.SpeechClient()

    with io.open(filename, 'rb') as audio_file:
        content = audio_file.read()

    audio = types.RecognitionAudio(content=content)
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=sample_rate,
        language_code=language_code)

    start = time.time();
    response = client.recognize(config, audio)
    proc_time = time.time() - start
        
    # Iterate through consecutive portions of the audio to get 
    # the complete audio transcript.
    # print(response) # raw response
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
    parser.add_argument('path', 
        help='File path for audio file to be transcribed')
    parser.add_argument('--rate', 
        help='Sampling rate [Hz]', type=int)
    args = parser.parse_args()
    
    transcribe(args.path, sample_rate=args.rate, verbose=True)