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
    y_test = None
    y_pred = None
    nb = None
    vect = None

    while go:
        data = pd.read_csv('TrainingTweets.csv')

        X = data.text  # get tweets
        y = data.airline_sentiment  # get sentiment value (negative, neutral, positive)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)  # split each row into 80% training and
        # 20% testing data
        vect = CountVectorizer(binary=False)
        X_train_vect = vect.fit_transform(X_train)

        sm = SMOTE()

        X_train_res, y_train_res = sm.fit_sample(X_train_vect, y_train)  # artificially creating new test data

        nb = MultinomialNB()
        nb.fit(X_train_res, y_train_res)

        X_test_vect = vect.transform(X_test)
        y_pred = nb.predict(X_test_vect)

        if accuracy_score(y_test, y_pred) * 100 > 80:
            go = False
        if count % 20 == 0:
            print('| Insufficient test result accuracy. Retraining...'.ljust(82) + '|')
        count += 1
    DisplayTrainingResults(y_test, y_pred)

    return nb, vect


def ProcessTweet(text, nb, vect):
    tweets = [text]
    test_tweets = vect.transform(tweets)
    sentiment = nb.predict(test_tweets)
    delete = False

    sia = SentimentIntensityAnalyzer()
    sentimentScore = None
    ss = sia.polarity_scores(text)
    for item in sorted(ss):
        sentimentScore = ss[item]
        break

    if sentimentScore == 0.0 and text == '':
        delete = True

    return sentiment, sentimentScore, delete
