from CorrelationAnalysis import *
from SentimentAnalysis import *
from StartingData import *
from TweetFarming import *
from WeatherAnalysis import *
from Display import *


def Main():
    try:
        print('\nWelcome to Panga\'s program. It\'s pretty righteous.')
        tsoCount = int(input('Tweets: '))
        cityCount = int(input('Cities: '))
        weatherScores, sentimentData = GetData(tsoCount, cityCount)
        DisplayData(weatherScores, sentimentData)
        print('\nIt was dope, right? Tell your friends.\n')
    except IndexError:
        print('+' + '-'*81 + '+' + '\n')
        print('There was an issue with data compiled. Please run again.')
    except ZeroDivisionError:
        print('+' + '-'*81 + '+' + '\n')
        print('Not enough data to complete operations. Try extending search parameters.')
    except Exception as ex:
        print('+' + '-'*81 + '+' + '\n')
        print('Something unexpected happened:')
        print(ex)


def GetData(tsoCount, cityCount):
    cityData = GetCityData(cityCount)
    tweetData = FindTweets(cityData, tsoCount)
    sentimentData, tweetsToDelete = PerformSentimentAnalysis(tweetData)

    rangeCount = len(tweetsToDelete)
    plural = 's'
    if rangeCount == 1:
        plural = ''
    for i in range(rangeCount):
        tweetData.pop(tweetsToDelete[i] - i)
    if rangeCount > 0:
        print('| Deleted {} tweet{} with no sentiment data available.'.format(rangeCount, plural).ljust(82) + '|')

    weatherData, tweetsToDelete = GetWeatherData(tweetData)

    rangeCount = len(tweetsToDelete)
    plural = 's'
    if rangeCount == 1:
        plural = ''
    for i in range(rangeCount):
        sentimentData.pop(tweetsToDelete[i] - i)
    if rangeCount > 0:
        print('| Deleted {} tweet{} with no weather data available.'.format(rangeCount, plural).ljust(82) + '|')

    weatherScores, tweetsToDelete = GetWeatherScores(weatherData)

    rangeCount = len(tweetsToDelete)
    plural = 's'
    if rangeCount == 1:
        plural = ''
    for i in range(rangeCount):
        sentimentData.pop(tweetsToDelete[i] - i)
    if rangeCount > 0:
        print('| Deleted {} tweet{} with insufficient weather data.'.format(rangeCount, plural).ljust(82) + '|')

    return weatherScores, sentimentData


def DisplayData(weatherScores, sentimentData):
    returnData, correlationData = DetermineCorrelationVader(sentimentData, weatherScores)
    OutputDataVader(returnData, correlationData)
    correlationData, returnData = DetermineCorrelationNaiveBayes(sentimentData, weatherScores)
    OutputDataNaiveBayes(correlationData, returnData)


Main()
