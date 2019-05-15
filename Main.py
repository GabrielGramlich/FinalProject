from CorrelationAnalysis import *
from SentimentAnalysis import *
from StartingData import *
from TweetFarming import *
from WeatherAnalysis import *


def Main():
    # started at 8:58, 785 tweets
    tsoCount = input('Count: ')
    weatherScores, sentimentData = GetData(tsoCount)
    DisplayData(weatherScores, sentimentData)


def GetData(tsoCount):
    cityData = GetCityData()
    tweetData = FindTweets(cityData, tsoCount)
    sentimentData, tweetsToDelete = PerformSentimentAnalysis(tweetData)
    for i in range(len(tweetsToDelete)):
        tweetData.pop(tweetsToDelete[i] - i)
        print('Deleted tweet with no sentiment data available.')

    weatherData, tweetsToDelete = GetWeatherData(tweetData)
    for i in range(len(tweetsToDelete)):
        sentimentData.pop(tweetsToDelete[i] - i)
        print('Deleted tweet with no weather data available.')

    weatherScores, tweetsToDelete = GetWeatherScores(weatherData)
    for i in range(len(tweetsToDelete)):
        sentimentData.pop(tweetsToDelete[i] - i)
        print('Deleted tweet with no weather data available.')

    return weatherScores, sentimentData


def DisplayData(weatherScores, sentimentData):
    returnData, correlationData = DetermineCorrelationVader(sentimentData, weatherScores)
    OutputDataVader(returnData, correlationData)
    correlationData, returnData = DetermineCorrelationNaiveBayes(sentimentData, weatherScores)
    OutputDataNaiveBayes(correlationData, returnData)


Main()
