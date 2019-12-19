# @Author   Timothy Marotta
# @Date     October 21, 2019

import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob
import config


class TwitterScraper:
    def __init__(self):
        consumer_key = config.CONSUMER_KEY
        consumer_secret = config.CONSUMER_SECRET
        access_token = config.ACCESS_KEY
        access_token_secret = config.ACCESS_SECRET

        try:
            self.auth = OAuthHandler(consumer_key, consumer_secret)
            self.auth.set_access_token(access_token, access_token_secret)
            self.api = tweepy.API(self.auth)
            print("Authenticated")
        except:
            print("Error: Authentication Failed")

    def clean_tweet(self, tweet):
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])| (\w+:\ / \ / \S+)", " ", tweet).split())

    def get_tweet_sentiment(self, tweet):
        analysis = TextBlob(self.clean_tweet(tweet))
        return analysis.sentiment.polarity

    def get_tweets(self, query, count):
        """
        Scrapes Twitter for a given number of tweets that follow the query
        Returns parsed list of tweets
        """
        tweets = []

        try:
            # call twitter api to fetch tweets
            count_check = 0
            for tweet in tweepy.Cursor(self.api.search, q=query, count=count).items(200):
                count_check += 1
                # empty dictionary to store required params of a tweet
                parsed_tweet = {'text': tweet.text, 'sentiment': self.get_tweet_sentiment(tweet.text)}

                # appending parsed tweet to tweets list
                if tweet.retweet_count > 0:
                    # if tweet has retweets, ensure that it is appended only once
                    if parsed_tweet not in tweets:
                        tweets.append(parsed_tweet)
                else:
                    tweets.append(parsed_tweet)

                    # return parsed tweets
            print(count)
            return tweets
        except tweepy.TweepError as e:
            # print error (if any)
            print("Error : " + str(e))


def main():
    api = TwitterScraper()
    tweets = api.get_tweets(query="Joe Biden", count=400)
    positive_tweets = [tweet for tweet in tweets if tweet['sentiment'] > 0]
    print("Positive tweets percentage: {} %".format(100 * len(positive_tweets) / len(tweets)))
    negative_tweets = [tweet for tweet in tweets if tweet['sentiment'] < 0]
    print("Negative tweets percentage: {} %".format(100 * len(negative_tweets) / len(tweets)))
    neutral_tweets = [tweet for tweet in tweets if tweet['sentiment'] == 0]
    print("Neutral tweets percentage: {} %".format(100 * len(neutral_tweets) / len(tweets)))

    # printing first 5 positive tweets
    print("\n\nPositive tweets:")
    for tweet in positive_tweets[:10]:
        print(tweet['text'])

    # printing first 5 negative tweets
    print("\n\nNegative tweets:")
    for tweet in negative_tweets[:10]:
        print(tweet['text'])

    print("\n\nNeutral tweets:")
    for tweet in neutral_tweets[:10]:
        print(tweet['text'])

    print(len(positive_tweets))
    print(len(negative_tweets))
    print(len(neutral_tweets))


if __name__ == "__main__":
    main()
