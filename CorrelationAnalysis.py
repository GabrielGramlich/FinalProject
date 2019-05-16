import random


def DetermineCorrelationVader(sentimentData, weatherScores):
    correlationResults = []
    variance = .25
    totalTrue = 0
    totalFalse = 0

    totalSentiment = 0
    totalWeather = 0

    for i in range(len(sentimentData)):
        try:
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
        except IndexError:
            print('Sentiment data: ' + str(len(sentimentData)))
            print('Weather data: ' + str(len(weatherScores)))
            print('i: ' + str(i))

    percentCorrelation = totalTrue / len(sentimentData) * 100
    variance = variance / 2 * 100
    averageWeather = totalWeather / len(sentimentData)
    averageSentiment = totalSentiment / len(sentimentData)

    returnData = [percentCorrelation, variance, averageWeather, averageSentiment, totalTrue, totalFalse]

    return returnData, correlationResults


def CreateRandomCorrelationData(upperBound):
    randomData = []

    for i in range(upperBound):
        randomSentiment = random.randint(-100, 100)
        randomSentiment = randomSentiment / 100
        randomWeather = random.randint(-4, 4)
        randomWeather = randomWeather / 4
        randomData.append([randomSentiment, randomWeather])

    return randomData


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
