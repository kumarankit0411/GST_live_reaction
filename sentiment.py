import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob
import time

consumer_key = 'ozT7P2ebEfkOOHliDyhoimnqS'
consumer_secret = 'h3Ha26bzIP7X2KRTcynTEB9bJ7skbenUgoWznASBojmt9dSg9c'

access_token = '1336053463-PaURYGu3cef6ARTdWExBgSSnGhbxFiuRJIipriR'
access_secret = 'gRlsEA6OWll2gMfhpH8wJsddMcnhd8IuSruNO0bzEXpOK'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

public_tweets = api.search('GST')
pol=[]
while(True):
    public_tweets = api.search('GST')
    for tweet in public_tweets:
        #print(tweet.text)
        analysis = TextBlob(tweet.text)
        #print(analysis.sentiment)
        pol.append(analysis.sentiment.polarity)

    avg = sum(pol)/len(pol)
    if avg < -.3:
        print("People are not liking GST")
    elif avg >= .3 and avg < 0:
        print("People are soemwhat against GST")
    elif avg == 0:
        print("People don't understand GST")
    elif avg > 0 and avg < .3:
        print("People like GST")
    else:
        print("People love GST")
    time.sleep(10)    
