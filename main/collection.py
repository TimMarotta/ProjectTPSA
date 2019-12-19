# @Author   Timothy Marotta
# @Date     December 16, 2019
import datetime
import tweepy
from tweepy import OAuthHandler
import config
import re
from textblob import TextBlob
import time


class TwitterCollection:
    def __init__(self):
        consumer_key = config.CONSUMER_KEY
        consumer_secret = config.CONSUMER_SECRET
        access_token = config.ACCESS_KEY
        access_token_secret = config.ACCESS_SECRET

        try:
            self.auth = OAuthHandler(consumer_key, consumer_secret)
            self.auth.set_access_token(access_token, access_token_secret)
            self.api = tweepy.API(self.auth, wait_on_rate_limit=False)
            print("Authenticated")
        except tweepy.TweepError:
            print("Error: Authentication Failed")

    def clean_tweet(self, tweet):
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])| (\w+:\ / \ / \S+)", " ", tweet).split())

    def get_tweet_sentiment(self, tweet):
        analysis = TextBlob(self.clean_tweet(tweet))
        return analysis.sentiment.polarity

    def get_tweets(self, name):
        print(name)
        print(datetime.datetime.now())
        back_counter = 1
        while True:
            try:
                with open('output/raw_' + name.replace(' ', '_').lower() + '.txt', 'a') as outfile:
                    statuses = list(tweepy.Cursor(self.api.search, q=name).items(250))
                    outfile.write(str(statuses))
                filtered = []
                for tweet in range(len(statuses)):
                    data = {'text': statuses[tweet].text, 'time': str(statuses[tweet].created_at),
                            'sentiment': self.get_tweet_sentiment(statuses[tweet].text)}
                    filtered.append(data)
                with open('output/' + name.replace(' ', '_').lower() + '.txt', 'a') as outfile:
                    for tweet in filtered:
                        outfile.write(str(tweet))

                print(datetime.datetime.now())
                print("\n")
                break
            except tweepy.TweepError as e:
                print(e.reason)
                time.sleep(60*back_counter)
                back_counter += 1
                continue


def main():
    tool = TwitterCollection()
    candidates_to_search = ['Joe Biden', 'Pete Buttigieg', 'Amy Klobuchar', 'Bernie Sanders', 'Tom Steyer',
                            'Elizabeth Warren', 'Andrew Yang', 'Donald Trump', 'Democrat', 'Republican']
    count = 1
    while count <= 50:
        for name in candidates_to_search:
            tool.get_tweets(name=name)
        print("Finished round " + str(count) + " at " + str(datetime.datetime.now()))
        count += 1


if __name__ == '__main__':
    main()
