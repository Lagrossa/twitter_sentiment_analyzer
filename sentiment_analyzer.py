import tweepy
import csv
from textblob import TextBlob

access_token = '1377146544139345934-xdGCvOMp0f1ExDlcAvwiFZFl8C8YJX'
access_token_secret = 'bDYZP1N8c24ewRnC0mfiPdLpCqmM80Ufx4g5XFxHgnV91'

API_key = '4U4kv4hT6lF4JXhihOhFNTiaE'
API_secretKey = 'nsU37dS5CxaBzouBCkndbbnaqsB7cvG6Wx0hxcXvvOhixYViAh' 

auth = tweepy.OAuthHandler(API_key, API_secretKey)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search(input())

with open('tweets.csv', 'w') as csv_file:
    csv_writer = csv.writer(csv_file)

    for tweet in public_tweets:
        raw_tweet = tweet.text
        analysis = TextBlob(raw_tweet)
        print(raw_tweet)
        csv_writer.writerow([raw_tweet])
        csv_writer.writerow([analysis.sentiment])
