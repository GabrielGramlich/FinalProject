from datetime import datetime as dt
from datetime import timedelta
from Display import ProgressBar
import math
import re
from TwitterSearch import *


def FindTweets(cities, tsoCount):
    print()
    print('+' + '-'*81 + '+')
    print('| Finding tweets...'.ljust(82) + '|')
    threeDaysAgo = dt.now() - timedelta(days=3)     # Subtracting 3 days from now
    threeDaysAgo = threeDaysAgo.strftime('%Y-%m-%d')    # Converting from timedelta to string object
    threeDaysAgo = dt.strptime(threeDaysAgo, '%Y-%m-%d').date()     # Converting back to date object
    allTweetData = []
    count = 0
    for city in cities:
        try:
            cityRadius = int(math.sqrt(city[2] / math.pi))  # Finding radius of the city from km2

            tso = TwitterSearchOrder()
            tso.set_count(tsoCount)
            tso.set_keywords([' '])     # Using space instead of a word so we get any and all tweets
            tso.set_language('en')
            tso.set_include_entities(False)
            tso.set_geocode(latitude=city[3][0], longitude=city[3][1], radius=cityRadius, imperial_metric=False)
            tso.set_since(threeDaysAgo)

            ts = TwitterSearch(
                consumer_key='BMek2JK3Ykw5le2aMCI4drivX',
                consumer_secret='ifJU4ALt59Es3B6XVxulsmjjhenF3Jp3gcAsH6V0336Du7bOW1',
                access_token='1125600489784139776-Fj5caK02PrxgGvPaYjggFTGPCjl8IU',
                access_token_secret='dWQe8VzGGNO4bFUlnAUrIKwwVKJil18gBc5Mmxx47vWge'
            )

            for tweet in ts.search_tweets_iterable(tso):
                allTweetData.append(GetTweetData(tweet, city))

            count += 1
            ProgressBar(count / len(cities))    # Creating a progress bar to keep the user from worrying
        except TwitterSearchException as ex:
            print(ex.message)

    print('| Finished finding tweets'.ljust(82) + '|')
    return allTweetData


def GetTweetData(tweet, city):
    text = CleanTweet(tweet['text'])
    time = tweet['created_at']
    location = city[1]
    tweetData = [text, time, location]
    return tweetData


def CleanTweet(text):
    text = re.sub(r'http\S+', '', text)     # Remove links
    text = re.sub(r'#', '', text)   # Remove hashtags
    text = re.sub(r'@\S+', '', text)    # Removes tags
    text = re.sub(r'RT', '', text)  # Remove retweets
    text = text.strip()     # Remove leading and trailing spaces
    return text
