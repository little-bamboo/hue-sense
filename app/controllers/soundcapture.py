#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import subprocess

import time

from comprehend import ComprehendManager
from stream import MicrophoneStream

from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

# Audio recording parameters
RATE = 16000
CHUNK = int(RATE / 10)  # 100ms

EXTERNAL_AUDIO_DETECTION = False


# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "../../configs/HuePi.json"


class SoundCapture(object):

    def __init__(self):
        self.comp = ComprehendManager()

    def external_audio(self):
        # todo offset, root via param
        root = os.getcwd()
        offset = 0.15  # user defined

        filedate = time.strftime("%Y%m%d-%H%M%S")
        filename = root + filedate + ".wav"

        proc = subprocess.Popen(['/bin/bin', 'bin/mic-noise-detection.sh', filename, '0.1'], stdout=subprocess.PIPE)
        result, error = proc.communicate()
        amplitude = float(result)

        print amplitude

        os.remove(filename)

        if amplitude >= offset:
            self.hue_speech_detection()
        else:
            return

    def hue_speech_detection(self):

        # See http://g.co/cloud/speech/docs/languages
        # for a list of supported languages.
        language_code = 'en-US'  # a BCP-47 language tag

        client = speech.SpeechClient()
        config = types.RecognitionConfig(
            encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=RATE,
            language_code=language_code)
        streaming_config = types.StreamingRecognitionConfig(
            config=config,
            interim_results=True)

        with MicrophoneStream(RATE, CHUNK) as stream:
            audio_generator = stream.generator()
            requests = (types.StreamingRecognizeRequest(audio_content=content)
                        for content in audio_generator)

            responses = client.streaming_recognize(streaming_config, requests)

            # Now, put the transcription responses to use.
            self.comp.listen_sentiment_loop(responses)
