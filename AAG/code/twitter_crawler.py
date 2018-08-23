import tweepy
import csv
import pandas as pd
####input your credentials here
consumer_key = 'P57mbSICPaHYFWrGii5cw7qcC'
consumer_secret = 'vltNZ8qRg6aZCV1p4PXVQWzImptVIU5STELM7WIsIQ3Bf3JNI0'
access_token = '2230551123-9hRy3le9Oc8xFYAbJRN3FpkILE1A5VzIRNi9UPB'
access_token_secret = 'TqIVtzNVOitUVMHZ668ObmOJZkv0ZWbnxcfM2mK85VppD'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
#####United Airlines
# Open/Create a file to append data
csvFile = open('cmt.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)


for tweet in tweepy.Cursor(api.search,q="#capmetroatx OR #capitalMETRO OR #capmetro", count = 200,
                           lang="en",
                           since="2010-01-01").items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
