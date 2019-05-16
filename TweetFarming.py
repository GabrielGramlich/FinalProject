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
    threeDaysAgo = dt.now() - timedelta(days=3)  # subtracting 3 days from now
    threeDaysAgo = threeDaysAgo.strftime('%Y-%m-%d')  # converting from timedelta to string object
    threeDaysAgo = dt.strptime(threeDaysAgo, '%Y-%m-%d').date()  # converting back to date object
    allTweetData = []
    count = 0
    for city in cities:
        try:
            cityRadius = int(math.sqrt(city[2] / math.pi))

            tso = TwitterSearchOrder()
            tso.set_count(tsoCount)
            tso.set_keywords([' '])
            tso.set_language('en') # we want to see German tweets only
            tso.set_include_entities(False) # and don't give us all those entity information
            tso.set_geocode(latitude=city[3][0], longitude=city[3][1], radius=cityRadius, imperial_metric=False)
            tso.set_since(threeDaysAgo)

            # it's about time to create a TwitterSearch object with our secret tokens
            ts = TwitterSearch(
                consumer_key='BMek2JK3Ykw5le2aMCI4drivX',
                consumer_secret='ifJU4ALt59Es3B6XVxulsmjjhenF3Jp3gcAsH6V0336Du7bOW1',
                access_token='1125600489784139776-Fj5caK02PrxgGvPaYjggFTGPCjl8IU',
                access_token_secret='dWQe8VzGGNO4bFUlnAUrIKwwVKJil18gBc5Mmxx47vWge'
            )

            for tweet in ts.search_tweets_iterable(tso):
                allTweetData.append(GetTweetData(tweet, city))

            count += 1
            ProgressBar(count / len(cities))
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
    # remove links
    text = re.sub(r'http\S+', '', text)
    # remove hashtags
    text = re.sub(r'#', '', text)
    # remove hollas
    text = re.sub(r'@\S+', '', text)
    # remove RT
    text = re.sub(r'RT', '', text)
    text = text.strip()
    return text
