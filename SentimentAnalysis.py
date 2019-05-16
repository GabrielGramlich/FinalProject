from Display import DisplayTrainingResults, DisplayBlock
from imblearn.over_sampling import SMOTE
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB


def PerformSentimentAnalysis(tweets):
    sentimentData = []
    tweetsToDelete = []
    count = 0
    nb, vect = TrainMachine()

    print('|'.ljust(82) + '|')
    print('| Finding sentiment data for {} tweets...'.format(len(tweets)).ljust(82) + '|')
    for tweet in tweets:
        text = tweet[0]
        sentiment, sentimentScore, delete = ProcessTweet(text, nb, vect)
        if delete:
            tweetsToDelete.append(count)
        else:
            sentimentData.append([tweet, [sentiment, sentimentScore]])
        count += 1
    print('| Found sentiment data for all tweets'.ljust(82) + '|')

    return sentimentData, tweetsToDelete


def TrainMachine():
    DisplayBlock()
    print('| Super sci-fi fun time. Training the machine...'.ljust(82) + '|')

    go = True
    count = 10
    labelTest = None
    labelPrediction = None
    nb = None
    vect = None

    while go:
        data = pd.read_csv('TrainingTweets.csv')

        features = data.text    # Get tweets
        y = data.airline_sentiment  # Get sentiment value (negative, neutral, positive)
        # Split each row into 80% training and 20% testing data
        featuresTrain, featuresTest, labelTrain, labelTest = train_test_split(features, y, test_size=0.2)
        vect = CountVectorizer(binary=False)
        featuresTrainVect = vect.fit_transform(featuresTrain)   # Gathers features from text for training

        sm = SMOTE()

        # Artificially creating new test data
        featuresTrainBalanced, labelTrainBalanced = sm.fit_sample(featuresTrainVect, labelTrain)

        nb = MultinomialNB()
        nb.fit(featuresTrainBalanced, labelTrainBalanced)   # Finding patterns between features and labels

        featuresTestVect = vect.transform(featuresTest)     # Gathers features from text for testing
        labelPrediction = nb.predict(featuresTestVect)  # Get predictions

        if accuracy_score(labelTest, labelPrediction) * 100 > 80:
            go = False
        if count % 20 == 0:
            print('| Insufficient test result accuracy. Retraining...'.ljust(82) + '|')
        count += 1
    DisplayTrainingResults(labelTest, labelPrediction)

    return nb, vect


def ProcessTweet(text, nb, vect):
    tweets = [text]
    testTweets = vect.transform(tweets)     # Gather features from text
    sentiment = nb.predict(testTweets)  # Find sentiment of tweets
    delete = False

    sia = SentimentIntensityAnalyzer()
    sentimentScore = None
    ss = sia.polarity_scores(text)  # Get sentiment rating, vader style
    for item in sorted(ss):
        sentimentScore = ss[item]
        break

    if sentimentScore == 0.0 and text == '':
        delete = True

    return sentiment, sentimentScore, delete
