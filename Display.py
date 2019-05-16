import collections
from CorrelationAnalysis import ConvertTargetsToInts, CreateRandomCorrelationData
from datetime import datetime as dt
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix
import sys

startingTime = None


def ProgressBar(progress):
    global startingTime

    status = ''
    if progress >= 1:   # Checking if completed
        progress = 1
        status = 'Done      |\r\n'
        startingTime = None
    else:
        if startingTime is not None:
            currentTime = dt.now()
            timeElapsed = currentTime - startingTime
            remainingProgress = 1 - progress
            baseTime = timeElapsed / progress
            remainingTime = str(remainingProgress * baseTime)
            remainingTimeIndex = remainingTime.index('.')
            remainingTime = remainingTime[:remainingTimeIndex]
            status = 'Time remaining: ' + remainingTime
        else:
            startingTime = dt.now()
            status = 'Calculating time remaining...'

    barLength = 40  # Setting size of progress bar in characters
    block = int(round(barLength * progress))  # Making the completed section of the bar
    text = '\r| Percent completed: {1:.2f}% [{0}] {2}'.format('#'*block + '-'*(barLength - block),
                                                              progress * 100, status)
    sys.stdout.write(text)
    sys.stdout.flush()


def DisplayBlock():
    # Making a pretty display between sections of code
    print('+' + '-'*81 + '+')
    print('|' + '\\-/' * 27 + '|')
    print('|' + '/-\\' * 27 + '|')
    print('+' + '-'*81 + '+')


def DisplayTrainingResults(labelTest, labelPrediction):
    cm = confusion_matrix(labelTest, labelPrediction)
    print('| Training Complete'.ljust(82) + '|')
    print('|'.ljust(82) + '|')
    print('| Training Results:'.ljust(82) + '|')
    print('| Accuracy: {:.2f}%'.format(accuracy_score(labelTest, labelPrediction) * 100).ljust(82) + '|')
    print('| F1 Score: {:.2f}%'.format(f1_score(labelTest, labelPrediction, average='weighted') * 100).ljust(82) + '|')
    print('|'.ljust(82) + '|')
    print('| Confusion Matrix:'.ljust(82) + '|')
    print('| *************Pred neg --> Pred pos*'.ljust(82) + '|')
    print('| * Neg results                     *'.ljust(82) + '|')
    print('| *      |        {}\t{}\t {} \t*'.format(cm[0][0], cm[0][1], cm[0][2]).ljust(77) + '|')
    print('| *      |        {}\t{}\t {} \t*'.format(cm[1][0], cm[1][1], cm[1][2]).ljust(77) + '|')
    print('| *      V        {}\t{}\t {} \t*'.format(cm[2][0], cm[2][1], cm[2][2]).ljust(77) + '|')
    print('| **Pos results**********************'.ljust(82) + '|')


def OutputDataVader(returnData, correlationData):
    randomData = CreateRandomCorrelationData(len(correlationData))
    DisplayGraphVader(randomData, 'Random Data')    # Displaying a graph of random data for comparison to real data

    booleanTotal = returnData[4] + returnData[5]

    DisplayBlock()
    print('| Vader Sentiment Results:'.ljust(82) + '|')
    print('|'.ljust(82) + '|')
    print('| Average tweet sentiment score:\t{:.4f}'.format(returnData[3]).ljust(79) + '|')
    print('| Average weather score:\t\t\t{:.4f}'.format(returnData[2]).ljust(73) + '|')
    print('| Does correlate:\t\t\t\t\t{:.2f}%'.format((returnData[4] / booleanTotal) * 100).ljust(68) + '|')
    print('| Does not correlate:\t\t\t\t{:.2f}%'.format((returnData[5] / booleanTotal) * 100).ljust(71) + '|')
    print('|'.ljust(82) + '|')
    print('| There is a {:.2f}% correlation between mood and weather given '
          'a {:.1f}% variance.'.format(returnData[0], returnData[1]).ljust(82) + '|')

    DisplayGraphVader(correlationData, 'Vader Data')


def DisplayGraphVader(correlationData, title):
    sentimentPlotDict = {}
    weatherPlotDict = {}
    for i in range(len(correlationData)):
        # Creating a key so values of both dictionaries can be sorted together
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

    plt.plot(weatherPlotPoints, 'k', sentimentPlotPoints, 'grey', sentimentPlotPoints, 'k.', weatherPlotPoints, 'b.')
    plt.ylabel('negative to positive sentiment(grey) and weather(blue)')
    plt.title(title)
    plt.show()


def OutputDataNaiveBayes(correlationData, returnData):
    tweetTotal = returnData[0] + returnData[1] + returnData[2]
    weatherTotal = returnData[3] + returnData[4] + returnData[5]
    booleanTotal = returnData[6] + returnData[7]

    DisplayBlock()
    print('| Naive Bayes Sentiment Results:'.ljust(82) + '|')
    print('|'.ljust(82) + '|')
    print('| Negative tweets:\t\t{:.2f}%'.format((returnData[0] / tweetTotal) * 100).ljust(78) + '|')
    print('| Neutral tweets:\t\t{:.2f}%'.format((returnData[1] / tweetTotal) * 100).ljust(77) + '|')
    print('| Positive tweets:\t\t{:.2f}%'.format((returnData[2] / tweetTotal) * 100).ljust(78) + '|')
    print('| Negative weather:\t\t{:.2f}%'.format((returnData[3] / weatherTotal) * 100).ljust(79) + '|')
    print('| Neutral weather:\t\t{:.2f}%'.format((returnData[4] / weatherTotal) * 100).ljust(78) + '|')
    print('| Positive weather:\t\t{:.2f}%'.format((returnData[5] / weatherTotal) * 100).ljust(79) + '|')
    print('| Does correlate:\t\t{:.2f}%'.format((returnData[6] / booleanTotal) * 100).ljust(77) + '|')
    print('| Does not correlate:\t{:.2f}%'.format((returnData[7] / booleanTotal) * 100).ljust(80) + '|')
    print('|'.ljust(82) + '|')
    print('| There is a {:.2f}% correlation between mood and weather.'.format(returnData[8]).ljust(82) + '|')
    print('+' + '-'*81 + '+')

    DisplayGraphNaiveBayes(correlationData, 'Naive Bayes Data')


def DisplayGraphNaiveBayes(correlationData, title):
    sentimentData, weatherData = ConvertTargetsToInts(correlationData)

    sentimentPlotDict = {}
    weatherPlotDict = {}
    for i in range(len(correlationData)):
        # Creating a key so values of both dictionaries can be sorted together
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

    plt.plot(sentimentPlotPoints, 'ko', sentimentPlotPoints, 'w.', weatherPlotPoints, 'b.')
    plt.ylabel('negative to positive sentiment(black) and weather(blue)')
    plt.title(title)
    plt.show()


