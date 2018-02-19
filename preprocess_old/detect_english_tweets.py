# -*- coding: utf-8 -*-

import csv
from polyglot.detect import Detector

file_to_read = "./marawi_tweets_05_23_to_05_24.csv"
file_to_write = "./marawi_english_tweets_05_23_to_05_24.csv"

#------------------------------------------------------------------------------------------------
def csv_read_and_write(read_path, write_path):
    with open(write_path ,'w') as outFile:
        fileWriter = csv.writer(outFile)
        with open(read_path,'r') as inFile:
            fileReader = csv.reader(inFile)
            for row in fileReader:
                tweet = row[4]
                tweet.decode()
                print(tweet)
                is__english = detect_english(tweet)
                print(is__english)

                if is__english:
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
               
#----------------------------------------------------------------------
def detect_english(tweet):
	try:
		languages = Detector(tweet.decode('utf-8'), quiet=True).languages
		for language in languages:
			if language.name == "English":
				print(language.confidence)
				if float(language.confidence) >= 85.0:
					return True
				else:
					return False
		return False
	except UnicodeError:
		print("string not UTF-8")
		return False

#--------------------------------------------------------------------------------

csv_read_and_write(file_to_read, file_to_write)