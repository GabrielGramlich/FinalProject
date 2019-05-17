# FinalProject

This project pulls tweets for sentiment analysis, and then finds the weather at the time and location the tweet
was sent to see how the user's mood correlates . In regard to the sentiment analysis, it utilizes a dataset from
kaggle and modules from sklearn and imblearn to train the machine with twitter data. Then the tweets pulled from
Twitter's API are fed through that to determine mood. It also utilizes NLTK's Vader module to get a second source
of sentiment data. The weather is pulled from NOAA and processed in a rudimentary way to determine the 'setinment'
of the weather. Finally, those results are compared to the surprising result that there is really no correlation
at all.

Happy trails, friends.
