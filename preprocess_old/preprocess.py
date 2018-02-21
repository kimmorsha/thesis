# -*- coding: utf-8 -*-

import csv
import preprocessor as p

file_to_read = "../marawi_tweets_with_location/marawi_tweets_may/marawi_tweets_05_23_to_05_24.csv"

#----------------------------------------------------------------------------------------------------------
def csv_reader(file_obj):
	with open(file_obj,'r') as file:
	    reader = csv.reader(file)
	    for row in reader:
	        tweet = row[4]
	        p.set_options(p.OPT.URL)
	       	tokenized_tweet = p.tokenize(tweet)
	       	print(tokenized_tweet)
#----------------------------------------------------------------------------------------------------------     

csv_reader(file_to_read)

#p.tokenize()