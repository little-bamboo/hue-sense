from qhue import create_new_username, Bridge, QhueException
import requests
import json
from colour import Color

SENTIMENT_COLORS = {'NEGATIVE': 0, 'NEUTRAL': 42770, 'POSITIVE': 21840}


class HueManager(object):
    """Create a Hue Instance to interface with lighting system"""

    def __init__(self, bridge_ip=None, user_key=None):

        """ First check to ensure a bridge IP address has been supplied """
        if bridge_ip is None:
            print("Please Supply Bridge IP Address")
            exit()
        else:
            self._bridge_ip = bridge_ip

        """ If a user has not been created, create one """
        if user_key is None:
            self._user_key = create_new_username(bridge_ip)
            print("New user: {} .".format(self._user_key))
        else:
            self._user_key = user_key

        self.bridge = Bridge(self._bridge_ip, self._user_key)
        self.bridge_url = self._bridge_ip + '/api/' + user_key + '/groups/1/action'

    # Ensure lights turn off when Hue closes
    def __del__(self):
        # self.light_state(False)
        print('Removing HueManager')

    def change_color_sentiment(self, sentiment, sentiment_score):
        print("Sentiment: {0}".format(sentiment))
        print("Sentiment Score: {0}".format(sentiment_score))

        color_payload = {"hue": SENTIMENT_COLORS[sentiment], "bri": 254, "sat": 254,
                         "transitiontime": 20}

        r = requests.put(self.bridge_url, data=json.dumps(color_payload))
        print r.content

    def change_color(self, color):
        print("Changing to color: {0}".format(color))

        c = Color(color)
        hue_var = int(c.hsl[0] * 65535)
        sat_var = int(c.hsl[1] * 254)

        color_payload = {"hue": hue_var, "sat": sat_var, "bri": 254, "transitiontime": 20}
        r = requests.put(self.bridge_url, data=json.dumps(color_payload))
        print r.content

    def light_state(self, state):
        # Pass light switch
        state_payload = {'on': state}
        r = requests.put(self.bridge_url, data=json.dumps(state_payload))
        print r.content
