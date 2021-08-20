from tweepy import OAuthHandler, Stream, StreamListener
import configparser
import json

config = configparser.ConfigParser()
config.read('configuration.ini')


consumer_key = config['twitter']['key']
consumer_secret = config['twitter']['secret']
access_token = config['twitter']['token']
access_token_secret= config['twitter']['secretToken']


def extract_data(data):
    raw_json = json.loads(data)
    id_str = raw_json['id_str']
    language = raw_json['lang']
    timestamp = raw_json['timestamp_ms']
    user = raw_json['user']['screen_name']
    text = raw_json['text']
    user_followers = raw_json['user']['followers_count']
    user_friends = raw_json['user']['friends_count']
    user_followers = raw_json['user']['followers_count']
    user_statuses = raw_json['user']['statuses_count']
    user_creation = raw_json['user']['created_at']
    return [id_str,
        language,
        timestamp,
        user,
        text,
        user_followers,
        user_friends,
        user_followers,
        user_statuses,
        user_creation
        ]

class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_data(self, data):
        test = extract_data(data)
        print(test)
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(track=['venezuela'])