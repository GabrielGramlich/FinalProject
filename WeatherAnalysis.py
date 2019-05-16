from datetime import datetime as dt
from datetime import timedelta
from dateutil.parser import parse
from Display import DisplayBlock, ProgressBar
from noaa_sdk import noaa


def GetWeatherData(tweets):
    DisplayBlock()
    print('| Finding weather data for {} tweets...'.format(len(tweets)).ljust(82) + '|')

    n = noaa.NOAA()
    weatherData = []
    tweetsToDelete = []
    count = 0

    for tweet in tweets:
        failedPass = True

        temperature = 0
        oldPressure = 0
        newPressure = 0
        humidity = 0
        dateFormat = '%Y-%m-%d %H:%M:%S'

        tweetDateEnd = str(parse(tweet[1]))
        try:
            index = tweetDateEnd.index('+')
            tweetDateEnd = tweetDateEnd[0:index]
        except ValueError:
            tweetDateEnd = tweetDateEnd
        tweetDateStart = dt.strptime(tweetDateEnd, dateFormat)
        tweetDateStart = dt.strftime(tweetDateStart - timedelta(hours=1), dateFormat)
        observations = n.get_observations(tweet[2], 'us', tweetDateStart, tweetDateEnd)
        for observation in observations:
            failedPass = False
            temperature = observation['temperature']['value']
            newPressure = observation['barometricPressure']['value']
            humidity = observation['relativeHumidity']['value']
            break

        if failedPass is True:
            tweetsToDelete.append(count)
        else:
            tweetDateEnd = dt.strptime(tweetDateEnd, dateFormat)
            tweetDateEnd = dt.strftime(tweetDateEnd - timedelta(hours=3), dateFormat)
            tweetDateStart = dt.strptime(tweetDateStart, dateFormat)
            tweetDateStart = dt.strftime(tweetDateStart - timedelta(hours=3), dateFormat)
            observations = n.get_observations(tweet[2], 'us', tweetDateStart, tweetDateEnd)
            for observation in observations:
                oldPressure = observation['barometricPressure']['value']
                weatherData.append([temperature, oldPressure, newPressure, humidity])
                break

        count += 1
        ProgressBar(count / len(tweets))
    print('| Found weather data for all tweets'.ljust(82) + '|')

    return weatherData, tweetsToDelete


def GetWeatherScores(weatherData):
    weatherScores = []
    tweetsToDelete = []
    count = 0

    for weather in weatherData:
        if weather[0] is None and weather[2] is None and weather[3] is None:
            tweetsToDelete.append(count)
        else:
            temperatureScore = GetTemperatureScore(weather)
            pressureScore = GetPressureScore(weather)
            humidityScore = GetHumidityScore(weather)

            weatherScore = (temperatureScore + pressureScore + humidityScore) / 4

            weatherSentiment = ''
            if weatherScore < -0.33:
                weatherSentiment = 'negative'
            elif weatherScore > 0.33:
                weatherSentiment = 'positive'
            else:
                weatherSentiment = 'neutral'
            weatherScores.append([weatherScore, weatherSentiment])

        count += 1

    return weatherScores, tweetsToDelete


def GetTemperatureScore(weather):
    temperatureScore = 0

    try:
        if weather[0] < 0 or weather[0] > 40:
            temperatureScore = -2
        elif weather[0] < 15 or weather[0] > 25:
            temperatureScore = -1
        elif weather[0] >= 15 or weather[0] <= 25:
            temperatureScore = 1
        if weather[0] > 20:
            temperatureScore += 1
    except TypeError:
        temperatureScore = 0

    return temperatureScore


def GetPressureScore(weather):
    pressureScore = 0

    try:
        conversionRate = 0.0002952998751
        oldPressure = weather[1] * conversionRate
        newPressure = weather[2] * conversionRate
        if newPressure < 29.92:  # low pressure is a rule of thumb for bad weather, high pressure for good
            pressureScore = -.5
        else:
            pressureScore = .5
        if oldPressure - newPressure < -0.04:  # change in pressure over three hours shows a storm front moving in
            pressureScore += .5
        elif oldPressure - newPressure > 0.04:
            pressureScore += -.5
    except TypeError:
        pressureScore = 0

    return pressureScore


def GetHumidityScore(weather):
    humidityScore = 0

    try:
        if weather[3] < 20 or weather[3] > 65:
            humidityScore = -1
        elif weather[3] >= 30 or weather[3] <= 50:
            humidityScore = 1
    except TypeError:
        humidityScore = 0

    return humidityScore
