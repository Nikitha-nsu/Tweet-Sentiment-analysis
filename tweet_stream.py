# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 15:14:18 2020

@author: Nikitha
"""

#Importing th tweepy package
import tweepy
from textblob import TextBlob
import credentials
import csv
import os



#Creating two step Authentication credentials
auth = tweepy.OAuthHandler(credentials.consumer_key, credentials.consumer_secret)
auth.set_access_token(credentials.access_token, credentials.access_token_secret)

#Create an object to access twitter API
api = tweepy.API(auth)

#Variables for the keyword you wish to search, and the number of tweets having that keyword
searchTerm = input('Enter the keyword to search....')
noOfTerms = int(input('Specify no of terms to search...')) 

#Searching for Tweets
tweets = tweepy.Cursor(api.search, q =searchTerm, lan = 'english').items(noOfTerms)


#Iterate through each of the tweets

for tweet in tweets:
    
    analysis = TextBlob(tweet.text)
    polar = analysis.sentiment.polarity
    
    if polar > 0:
        title = 'positive'
    elif polar < 0:
        title = 'negative'
    else:
        title = 'neutral'
         
    
    output = open('twitter-out.txt' , 'a')
    output.write(title)
    output.write('\n')
    output.close()
    
    
             
        
    
        




