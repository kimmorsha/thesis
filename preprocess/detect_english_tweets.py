# -*- coding: utf-8 -*-

import csv
from polyglot.detect import Detector
import string

file_to_read = "./marawi_tweets_05_23_to_05_24.csv"
file_to_write = "./marawi_english_tweets_05_23_to_05_24.csv"

#--------------------------------------------------------------------------------------------------
def csv_read_and_write(read_path, write_path):
    with open(write_path ,'w') as outFile:
        fileWriter = csv.writer(outFile)
        i = 1;
        with open(read_path,'r') as inFile:
            fileReader = csv.reader(inFile)
            for row in fileReader:
                tweet = row[4]
                print(i, tweet)
                is_english = detect_language(tweet)
                print(is_english)
                if is_english is True:
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
                    fileWriter.writerow(data)
                i = i + 1

#-----------------------------------------------------------------------------------------------------
def detect_language(tweet):
	# tweet = filter(lambda x: x in string.printable, tweet)
	is_utf8 = isUTF8Strict(tweet) 
	if is_utf8:
		# tweet = tweet.decode('utf-8')
		languages = Detector(tweet.decode('utf-8'), quiet=True).languages
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
				if float(language.confidence) >= 5.0:
					is_english = False
		return is_english
	else:
		return False
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
csv_read_and_write(file_to_read, file_to_write)
