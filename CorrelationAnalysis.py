import matplotlib.pyplot as plt
import collections
import random


def DetermineCorrelationVader(sentimentData, weatherScores):
    correlationResults = []
    variance = .25
    totalTrue = 0
    totalFalse = 0

    totalSentiment = 0
    totalWeather = 0
    for i in range(len(sentimentData)):
        weatherScore = weatherScores[i][0]
        correlation = False
        point = sentimentData[i][1][1]
        low = point - variance
        high = point + variance
        if weatherScore > low and weatherScore < high:
            correlation = True
        correlationResults.append([point, weatherScore, correlation])
        if correlation:
            totalTrue += 1
        else:
            totalFalse += 1
        totalSentiment += point
        totalWeather += weatherScores[i][0]

    percentCorrelation = totalTrue / len(sentimentData) * 100
    variance = variance / 2 * 100
    averageWeather = totalWeather / len(sentimentData)
    averageSentiment = totalSentiment / len(sentimentData)

    returnData = [percentCorrelation, variance, averageWeather, averageSentiment, totalTrue, totalFalse]

    return returnData, correlationResults


def OutputDataVader(returnData, correlationData):
    print('\n\n\nVader Sentiment Results:')

    print()
    print('Average tweet sentiment score:\t{:.4f}'.format(returnData[3]))
    print('Average weather score:\t\t\t{:.4f}'.format(returnData[2]))
    print('Percent true correlation:\t\t{:.2f}%'.format(returnData[4] / (returnData[4] + returnData[5])))
    print('Percent false correlation:\t\t{:.2f}%'.format(returnData[5] / (returnData[4] + returnData[5])))

    randomData = CreateRandomCorrelationData(len(correlationData))
    DisplayGraphVader(randomData, 'Random Data')
    DisplayGraphVader(correlationData, 'Vader Data')

    print()
    print('There is a {:.2f}% correlation between mood and weather given a {:.1f}% variance.'.format(returnData[0],
                                                                                                     returnData[1]))


def CreateRandomCorrelationData(upperBound):
    randomData = []

    for i in range(upperBound):
        randomSentiment = random.randint(-100, 100)
        randomSentiment = randomSentiment / 100
        randomWeather = random.randint(-4, 4)
        randomWeather = randomWeather / 4
        randomData.append([randomSentiment, randomWeather])

    return randomData


def DisplayGraphVader(correlationData, title):
    sentimentPlotDict = {}
    weatherPlotDict = {}
    for i in range(len(correlationData)):
        key = (correlationData[i][0] * 1000000) + i
        sentimentPlotDict[key] = correlationData[i][0]
        weatherPlotDict[key] = correlationData[i][1]

    orderedSentimentDict = collections.OrderedDict(sorted(sentimentPlotDict.items()))
    orderedWeatherDict = collections.OrderedDict(sorted((weatherPlotDict.items())))

    sentimentPlotPoints = []
    for key in orderedSentimentDict:
        sentimentPlotPoints.append(orderedSentimentDict[key])

    weatherPlotPoints = []
    for key in orderedWeatherDict:
        weatherPlotPoints.append(orderedWeatherDict[key])

    plt.plot(sentimentPlotPoints, 'grey', sentimentPlotPoints, 'k.', weatherPlotPoints, 'k', weatherPlotPoints, 'b.')
    plt.ylabel('negative to positive sentiment(grey) and weather(blue)')
    plt.title(title)
    plt.show()


def DetermineCorrelationNaiveBayes(sentimentData, weatherScores):
    correlationResults = []
    totalTrue = 0
    totalFalse = 0
    negTweets = 0
    neuTweets = 0
    posTweets = 0
    negWeather = 0
    neuWeather = 0
    posWeather = 0

    for i in range(len(sentimentData)):
        correlation = False
        tweetSentiment = sentimentData[i][1][0]
        weatherSentiment = weatherScores[i][1]
        if tweetSentiment == 'negative':
            negTweets += 1
        elif tweetSentiment == 'neutral':
            neuTweets += 1
        elif tweetSentiment == 'positive':
            posTweets += 1
        if weatherSentiment == 'negative':
            negWeather += 1
        elif weatherSentiment == 'neutral':
            neuWeather += 1
        elif weatherSentiment == 'positive':
            posWeather += 1

        if weatherSentiment == tweetSentiment:
            correlation = True
        correlationResults.append([tweetSentiment, weatherSentiment, correlation])
        if correlation:
            totalTrue += 1
        else:
            totalFalse += 1

    percentCorrelation = totalTrue / len(sentimentData) * 100
    returnData = [negTweets, neuTweets, posTweets, negWeather, neuWeather, posWeather, totalTrue, totalFalse,
                  percentCorrelation]

    return correlationResults, returnData


def OutputDataNaiveBayes(correlationData, returnData):
    print('\n\n\nNaive Bayes Sentiment Results:')

    print()
    print('Percent negative tweets:\t{:.2f}%'.format(returnData[0] /
                                                     (returnData[0] + returnData[1] + returnData[2])))
    print('Percent neutral tweets:\t\t{:.2f}%'.format(returnData[1] /
                                                      (returnData[0] + returnData[1] + returnData[2])))
    print('Percent positive tweets:\t{:.2f}%'.format(returnData[2] /
                                                     (returnData[0] + returnData[1] + returnData[2])))
    print('Percent negative weather:\t{:.2f}%'.format(returnData[3] /
                                                      (returnData[3] + returnData[4] + returnData[5])))
    print('Percent neutral weather:\t{:.2f}%'.format(returnData[4] /
                                                     (returnData[3] + returnData[4] + returnData[5])))
    print('Percent positive weather:\t{:.2f}%'.format(returnData[5] /
                                                      (returnData[3] + returnData[4] + returnData[5])))
    print('Percent true correlation:\t{:.2f}%'.format(returnData[6] / (returnData[6] + returnData[7])))
    print('Percent false correlation:\t{:.2f}%'.format(returnData[7] / (returnData[6] + returnData[7])))

    DisplayGraphNaiveBayes(correlationData, 'Naive Bayes Data')

    print()
    print('There is a {:.2f}% correlation between mood and weather.'.format(returnData[8]))


def DisplayGraphNaiveBayes(correlationData, title):
    sentimentData, weatherData = ConvertTargetsToInts(correlationData)

    sentimentPlotDict = {}
    weatherPlotDict = {}
    for i in range(len(correlationData)):
        key = (sentimentData[i] * 1000000) + i
        sentimentPlotDict[key] = sentimentData[i]
        weatherPlotDict[key] = weatherData[i]

    orderedSentimentDict = collections.OrderedDict(sorted(sentimentPlotDict.items()))
    orderedWeatherDict = collections.OrderedDict(sorted((weatherPlotDict.items())))

    sentimentPlotPoints = []
    for key in orderedSentimentDict:
        sentimentPlotPoints.append(orderedSentimentDict[key])

    weatherPlotPoints = []
    for key in orderedWeatherDict:
        weatherPlotPoints.append(orderedWeatherDict[key])

    plt.plot(sentimentPlotPoints, 'grey', sentimentPlotPoints, 'k.', weatherPlotPoints, 'k', weatherPlotPoints, 'b.')
    plt.ylabel('negative to positive sentiment(grey) and weather(blue)')
    plt.title(title)
    plt.show()


def ConvertTargetsToInts(correlationData):
    sentimentData = []
    weatherData = []

    for i in range(len(correlationData)):
        tweetSentiment = correlationData[i][0]
        weatherSentiment = correlationData[i][1]
        if tweetSentiment == 'negative':
            sentimentData.append(-1)
        elif tweetSentiment == 'neutral':
            sentimentData.append(0)
        elif tweetSentiment == 'positive':
            sentimentData.append(1)
        if weatherSentiment == 'negative':
            weatherData.append(-1)
        elif weatherSentiment == 'neutral':
            weatherData.append(0)
        elif weatherSentiment == 'positive':
            weatherData.append(1)

    return sentimentData, weatherData
