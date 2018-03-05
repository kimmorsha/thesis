# -*- coding: utf-8 -*-

import csv
from polyglot.detect import Detector
import string
import preprocessor as p

file_to_read = "../marawi_tweets_with_location/marawi_tweets_june/official/all_tweets/marawi_tweets_06_04.csv"
file_of_english_tweets = "../marawi_tweets_with_location/marawi_tweets_june/official/english_tweets/marawi_tweets_06_04.csv"
file_of_non_english_tweets = "../marawi_tweets_with_location/marawi_tweets_june/official/non_english_tweets/marawi_tweets_06_04.csv"

#------------------------------------------------------------------------------------------------------
def csv_read_and_write(read_path):
    with open (file_of_english_tweets, 'w') as outFile1, open (file_of_non_english_tweets, 'w') as outFile2:
        file_writer1 = csv.writer(outFile1)
        file_writer2 = csv.writer(outFile2)

        i = 1;
        with open(read_path,'r') as inFile:
            fileReader = csv.reader(inFile)
            for row in fileReader:
                tweet = row[4]
                p.set_options(p.OPT.URL, p.OPT.MENTION)
                cleaned_tweet = p.clean(tweet)
                print(i, cleaned_tweet)
                is_english = detect_language(cleaned_tweet) # where we call the function that detects if it is english or not
                print(is_english)
                
                data = [row[0],
                        row[1],
                        row[2],
                        row[3],
                        row[4],
                        row[5],
                        row[6],
                        row[7],
                        row[8],
                        row[9]]

                if is_english is True:
                    file_writer1.writerow(data)
                else:
                    file_writer2.writerow(data)
                i = i + 1

#-----------------------------------------------------------------------------------------------------
def detect_language(tweet):
	# tweet = filter(lambda x: x in string.printable, tweet)
	# is_utf8 = isUTF8Strict(tweet) 
	# if is_utf8:
		# tweet = tweet.decode('utf-8')
    try:
        languages = Detector(tweet, quiet = True).languages
        is_english = False
        max_confidence = 0

        for language in languages:
            if language.name == "English":
                max_confidence = language.confidence
                print(language.confidence)
                if float(language.confidence) >= 93.0:
                   is_english = True
                else:
                    is_english = False
            else:
                if float(language.confidence) >= 20.0:
                    is_english = False
        return is_english
    except UnicodeDecodeError:
        print("UnicodeDecodeError ew")
        return False
	# else:
	# 	return False

#------------------------------------------------------------------------------------------------------
def isUTF8Strict(data):
    try:
        decoded = data.decode('UTF-8')
    except UnicodeDecodeError:
        return False
    else:
        for ch in decoded:
            if 0xD800 <= ord(ch) <= 0xDFFF:
                return False
        return True

#--------------------------------------------------------------------------------------------------------
csv_read_and_write(file_to_read)
