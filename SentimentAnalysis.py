import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import re


def PerformSentimentAnalysis(tweets):
    sentimentData = []
    tweetsToDelete = []
    count = 0
    nb, vect = TrainMachine()

    print()
    print('Finding sentiment data for ' + str(len(tweets)) + ' tweets...')
    for tweet in tweets:
        text = CleanTweet(tweet)
        sentiment, sentimentScore, delete = ProcessTweet(text, nb, vect)
        if delete:
            tweetsToDelete.append(count)
        else:
            sentimentData.append([tweet, [sentiment, sentimentScore]])
        count += 1
    print('Found sentiment data for all tweets')

    return sentimentData, tweetsToDelete


def TrainMachine():
    print()
    print('Super sci-fi fun time. Training the machine...')

    data = pd.read_csv('TrainingTweets.csv')

    X = data.text  # get tweets
    y = data.airline_sentiment  # get sentiment value (negative, neutral, positive)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)    # split each row into 80% testing and
                                                                                # 20% training data
    vect = CountVectorizer(binary=False)
    X_train_vect = vect.fit_transform(X_train)

    sm = SMOTE()

    X_train_res, y_train_res = sm.fit_sample(X_train_vect, y_train)  # artifically creating new test data

    nb = MultinomialNB()
    nb.fit(X_train_res, y_train_res)

    X_test_vect = vect.transform(X_test)
    y_pred = nb.predict(X_test_vect)

    print('Training Complete')
    print('Accuracy: {:.2f}%'.format(accuracy_score(y_test, y_pred) * 100))
    print('F1 Score: {:.2f}%'.format(f1_score(y_test, y_pred, average='weighted') * 100))
    print('Confusion Matrix:')
    print('WNegPNeg\tWNegPNeu\tWNegPPos\nWNeuPNeg\tWNeuPNeu\tWNeuPPos\nWPosPNeg\tWPosPNeu\tWPosPPos')
    print(confusion_matrix(y_test, y_pred))

    return nb, vect


def CleanTweet(tweet):
    text = tweet[0]
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
