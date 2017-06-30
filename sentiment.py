import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob
import time

consumer_key = 'YOUR_CONSUMER_KEY'
consumer_secret = 'YOUR_CONSUMER_SECRET'

access_token = 'YOUR_ACCESS_TOKEN'
access_secret = 'YOUR_ACCESS_SECRET'

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
