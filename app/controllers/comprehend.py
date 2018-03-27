import boto3
import sys
import re

from hue import HueManager, QhueException

import json
import decimal
import uuid

USER_KEY = "OTf6TuWbVekHudvGnPYZauZxkBAtKBojG-idfhr0"
BRIDGE_IP = "http://10.0.1.2"

# Used for identifying colors found in stream
COLOR_LIST = [
    "aqua",
    "blue",
    "navy",
    "teal",
    "olive",
    "green",
    "red",
    "maroon",
    "orange",
    "purple",
    "yellow",
    "fuchsia",
    "white"
]


class ComprehendManager(object):

    def __init__(self):
        self.comprehend = boto3.client(service_name='comprehend', region_name='us-west-2')
        self.dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
        self.table = self.dynamodb.Table('hue-sense')
        self.hue = HueManager(bridge_ip=BRIDGE_IP, user_key=USER_KEY)

    def listen_sentiment_loop(self, responses):
        """Iterates through server responses and converts them to sentiment values.

        The responses passed is a generator that will block until a response
        is provided by the server.

        Each response may contain multiple results, and each result may contain
        multiple alternatives; for details, see https://goo.gl/tjCPAU.  Here we
        print only the transcription for the top alternative of the top result.

        In this case, responses are provided for interim results as well. If the
        response is an interim one, print a line feed at the end of it, to allow
        the next result to overwrite it, until the response is a final one. For the
        final one, print a newline to preserve the finalized transcription.
        """

        num_chars_printed = 0
        for response in responses:
            if not response.results:
                continue

            # The `results` list is consecutive. For streaming, we only care about
            # the first result being considered, since once it's `is_final`, it
            # moves on to considering the next utterance.
            result = response.results[0]
            if not result.alternatives:
                continue

            # Display the transcription of the top alternative.
            transcript = result.alternatives[0].transcript

            # Display interim results, but with a carriage return at the end of the
            # line, so subsequent lines will overwrite them.
            #
            # If the previous result was longer than this one, we need to print
            # some extra spaces to overwrite the previous result
            overwrite_chars = ' ' * (num_chars_printed - len(transcript))

            if not result.is_final:
                sys.stdout.write(transcript + overwrite_chars + '\r')
                sys.stdout.flush()

                num_chars_printed = len(transcript)

            else:
                transcript_with_overwrite = transcript + overwrite_chars
                print("Captured Text: {0}".format(transcript_with_overwrite))

                # Exit recognition if any of the transcribed phrases could be
                # one of our keywords.
                if re.search(r'\b(exit|quit)\b', transcript, re.I):
                    print('Exiting..')

                    # TODO: Send 'lights out' command to turn off lights
                    exit()

                num_chars_printed = 0

                found_color = [x for x in COLOR_LIST if x in transcript]

                if found_color:
                    self.hue.change_color(found_color[0])

                else:

                    sentiment_response = self.comprehend.detect_sentiment(Text=transcript, LanguageCode='en')

                    if sentiment_response:
                        sentiment_response['transcript'] = transcript
                        sentiment_response['language'] = 'en'
                        sentiment = sentiment_response['Sentiment']
                        sentiment_score = sentiment_response['SentimentScore']
                        sentiment_response['stream-id'] = str(uuid.uuid4())

                        self.hue.change_color_sentiment(sentiment, sentiment_score)

                        # Convert floats to decimal
                        json_str = json.dumps(sentiment_response)
                        sentiment_score_dict = json.loads(json_str, parse_float=decimal.Decimal)
                        print sentiment_score_dict
                        response = self.table.put_item(Item=sentiment_score_dict)
                        print("dynamodb response: {0}".format(json.dumps(response)))
