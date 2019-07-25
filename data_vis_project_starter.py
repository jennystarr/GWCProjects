import json
from textblob import TextBlob
import matplotlib.pyplot as plt
import numpy as np
from wordcloud import WordCloud
from textblob import TextBlob
import os
from os import path

tweetFile = open("tweets_small.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()
# Continue your program below!
polarity = []
subjectivity = []

bigtweet = ""
for tweet in tweetData:
    text = tweet["text"]
    tb = TextBlob(tweet["text"])
    polarity.append(tb.polarity)
    subjectivity.append(tb.subjectivity)

    bigtweet += text

bigblob = TextBlob(bigtweet)
filterd = {}
commonwords = ("the", "a", "and", "about", "https", "for", "can", "out")
wordsList = bigblob.words
for word in wordsList:
    if len(word) < 3:
        continue
    if word in commonwords:
        continue

    filterd[word] = bigblob.word_counts[word]


tb = TextBlob("You are a brilliant computer scientist.")
print(tb.polarity)
# Fixing random state for reproducibility

plt.xlabel('Polarity')
plt.ylabel('Amount of tweets')
plt.title('Polarity of tweets')
plt.axis([-1, 1, 0, 60])
# Textblob sample:
plt.grid(True)
plt.hist(polarity, bins = [-1, -0.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75, 1.1])
plt.show()

print(tb.subjectivity)
plt.xlabel('Subjectivity')
plt.ylabel('Amount of tweets')
plt.title('Subjectivity of tweets')
plt.axis([-1, 1, 0, 60])
# Textblob sample:
plt.grid(True)
plt.hist(subjectivity, bins = [-1, -0.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75, 1.1])
plt.show()

# Plot
plt.scatter(subjectivity, polarity)
plt.xlabel('Polarity')
plt.ylabel('Amount of tweets')
plt.title('Scatter plot of polarity')
plt.grid(True)
plt.show()


# get data directory (using getcwd() is needed to support running example in generated IPython notebook)

wordcloud = WordCloud().generate_from_frequencies(filterd)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

#all_tweets = ', '.join(tweet['text']for tweet in tweetData)
#tb = TextBlob(all_tweets)
#print(all_tweets)

#filteredWords[word] = count
