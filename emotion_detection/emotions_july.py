# -*- coding: utf-8 -*-

import csv
import string
import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 \
  import Features, EmotionOptions


readFile = '../marawi_tweets_with_location/marawi_tweets_september/official/cleaned_tweets/marawi_tweets_09_03.csv'
writeFile1 = '../marawi_tweets_with_location/marawi_tweets_september/official/final_tweets/marawi_tweets_09_03.csv'
writeFile2 = '../marawi_tweets_with_location/marawi_tweets_september/official/final_tweets/no_emotions/marawi_tweets_09_03.csv'
#------------------------------------------------------------------------------------------------------
def analyze_emotions(read_path, write_path1, write_path2):
	natural_language_understanding = NaturalLanguageUnderstandingV1(
		username='5e002a7b-361d-4611-9bea-2175ab049b34',
		password='5BvZsR4TRc0u',
		version='2018-03-16')

	with open (write_path1, 'wb') as outFile1, open (write_path2, 'w') as outFile2:
		file_writer1 = csv.writer(outFile1)
		file_writer2 = csv.writer(outFile2)

		i = 1
		with open(read_path,'r') as inFile:
			fileReader = csv.reader(inFile)
			for row in fileReader:
				tweet = row[4]
				tweet = remove_words_with_numbers(tweet)
				print(i, tweet)



				# data = [row[0],
				# 		row[1],
				# 		row[4],
				# 		row[5],
				# 		row[10]]

				if isNotEmpty(tweet):
				    response = natural_language_understanding.analyze(
				    	language="en",
				    	text=tweet,
				    	features=Features(emotion=EmotionOptions()))

				    jsonData = json.dumps(response, indent=2)
				    print(jsonData)
				    my_dict = json.loads(jsonData)
				    my_dict2 = my_dict["emotion"]
				    document = my_dict2["document"]
				    emotion = document["emotion"]

				    highest_emotion = get_highest_emotion(emotion["anger"],
									            		emotion["joy"],
									            		emotion["sadness"],
									            		emotion["fear"],
									            		emotion["disgust"])
				    print(highest_emotion)

				    data = [row[0],
				    		row[1],
				    		row[4],
				    		row[5],
				    		row[10],
				    		emotion["anger"],
				    		emotion["joy"],
				    		emotion["sadness"],
				    		emotion["fear"],
				    		emotion["disgust"],
				    		highest_emotion]

				    file_writer1.writerow(data)

				    i = i+1

				else:
					data = [row[0],
				    		row[1],
				    		row[4],
				    		row[5],
				    		row[10]]
					file_writer2.writerow(data)

#-----------------------------------------------------------------------------------------------------
def remove_words_with_numbers(tweet):
	t = ""
	for word in tweet.split():
		if num_there(word) is False:
			t = t + word
			t += " "
	return t


def num_there(s):
    return any(i.isdigit() for i in s)


def isNotEmpty(s):
    return bool(s and s.strip())
#-----------------------------------------------------------------------------------------------------
def get_highest_emotion(anger, joy, sadness, fear, disgust):
	highest_emotion = []
	highest_percent = max(anger, joy, sadness, fear, disgust)

	if highest_percent == anger:
		highest_emotion.append("anger")
	elif highest_percent == joy:
		highest_emotion.append("joy")
	elif highest_percent == sadness:
		highest_emotion.append("sadness")
	elif highest_percent == fear:
		highest_emotion.append("fear")
	elif highest_percent == disgust:
		highest_emotion.append("disgust")

	highest_emotion.append(highest_percent) 

	return highest_emotion

#-----------------------------------------------------------------------------------------------------
# analyze_emotions(readFile, writeFile1, writeFile2)	

analyze_emotions("../marawi_tweets_with_location/marawi_tweets_july/official/cleaned_tweets/marawi_tweets_07_01.csv",
                   "../marawi_tweets_with_location/marawi_tweets_july/official/final_tweets/marawi_tweets_07_01.csv",
                   "../marawi_tweets_with_location/marawi_tweets_july/official/final_tweets/no_emotions/marawi_tweets_07_01.csv")

analyze_emotions("../marawi_tweets_with_location/marawi_tweets_july/official/cleaned_tweets/marawi_tweets_07_02.csv",
                   "../marawi_tweets_with_location/marawi_tweets_july/official/final_tweets/marawi_tweets_07_02.csv",
                   "../marawi_tweets_with_location/marawi_tweets_july/official/final_tweets/no_emotions/marawi_tweets_07_02.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_july/official/cleaned_tweets/marawi_tweets_07_03.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_july/official/final_tweets/marawi_tweets_07_03.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_july/official/final_tweets/no_emotions/marawi_tweets_07_03.csv")

analyze_emotions("../marawi_tweets_with_location/marawi_tweets_july/official/cleaned_tweets/marawi_tweets_07_04.csv",
                   "../marawi_tweets_with_location/marawi_tweets_july/official/final_tweets/marawi_tweets_07_04.csv",
                   "../marawi_tweets_with_location/marawi_tweets_july/official/final_tweets/no_emotions/marawi_tweets_07_04.csv")

analyze_emotions("../marawi_tweets_with_location/marawi_tweets_july/official/cleaned_tweets/marawi_tweets_07_05.csv",
                   "../marawi_tweets_with_location/marawi_tweets_july/official/final_tweets/marawi_tweets_07_05.csv",
                   "../marawi_tweets_with_location/marawi_tweets_july/official/final_tweets/no_emotions/marawi_tweets_07_05.csv")

analyze_emotions("../marawi_tweets_with_location/marawi_tweets_july/official/cleaned_tweets/marawi_tweets_07_06.csv",
                   "../marawi_tweets_with_location/marawi_tweets_july/official/final_tweets/marawi_tweets_07_06.csv",
                   "../marawi_tweets_with_location/marawi_tweets_july/official/final_tweets/no_emotions/marawi_tweets_07_06.csv")

analyze_emotions("../marawi_tweets_with_location/marawi_tweets_july/official/cleaned_tweets/marawi_tweets_07_07.csv",
                   "../marawi_tweets_with_location/marawi_tweets_july/official/final_tweets/marawi_tweets_07_07.csv",
                   "../marawi_tweets_with_location/marawi_tweets_july/official/final_tweets/no_emotions/marawi_tweets_07_07.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_july/official/cleaned_tweets/marawi_tweets_07_08.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_july/official/final_tweets/marawi_tweets_07_08.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_july/official/final_tweets/no_emotions/marawi_tweets_07_08.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_july/official/cleaned_tweets/marawi_tweets_07_09.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_july/official/final_tweets/marawi_tweets_07_09.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_july/official/final_tweets/no_emotions/marawi_tweets_07_09.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_july/official/cleaned_tweets/marawi_tweets_07_10.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_july/official/final_tweets/marawi_tweets_07_10.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_july/official/final_tweets/no_emotions/marawi_tweets_07_10.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_july/official/cleaned_tweets/marawi_tweets_07_11.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_july/official/final_tweets/marawi_tweets_07_11.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_july/official/final_tweets/no_emotions/marawi_tweets_07_11.csv")

analyze_emotions("../marawi_tweets_with_location/marawi_tweets_july/official/cleaned_tweets/marawi_tweets_07_12.csv",
                   "../marawi_tweets_with_location/marawi_tweets_july/official/final_tweets/marawi_tweets_07_12.csv",
                   "../marawi_tweets_with_location/marawi_tweets_july/official/final_tweets/no_emotions/marawi_tweets_07_12.csv")

analyze_emotions("../marawi_tweets_with_location/marawi_tweets_july/official/cleaned_tweets/marawi_tweets_07_13.csv",
                   "../marawi_tweets_with_location/marawi_tweets_july/official/final_tweets/marawi_tweets_07_13.csv",
                   "../marawi_tweets_with_location/marawi_tweets_july/official/final_tweets/no_emotions/marawi_tweets_07_13.csv")

analyze_emotions("../marawi_tweets_with_location/marawi_tweets_july/official/cleaned_tweets/marawi_tweets_07_14.csv",
                   "../marawi_tweets_with_location/marawi_tweets_july/official/final_tweets/marawi_tweets_07_14.csv",
                   "../marawi_tweets_with_location/marawi_tweets_july/official/final_tweets/no_emotions/marawi_tweets_07_14.csv")

analyze_emotions("../marawi_tweets_with_location/marawi_tweets_july/official/cleaned_tweets/marawi_tweets_07_15.csv",
                   "../marawi_tweets_with_location/marawi_tweets_july/official/final_tweets/marawi_tweets_07_15.csv",
                   "../marawi_tweets_with_location/marawi_tweets_july/official/final_tweets/no_emotions/marawi_tweets_07_15.csv")

analyze_emotions("../marawi_tweets_with_location/marawi_tweets_july/official/cleaned_tweets/marawi_tweets_07_16.csv",
                   "../marawi_tweets_with_location/marawi_tweets_july/official/final_tweets/marawi_tweets_07_16.csv",
                   "../marawi_tweets_with_location/marawi_tweets_july/official/final_tweets/no_emotions/marawi_tweets_07_16.csv")

analyze_emotions("../marawi_tweets_with_location/marawi_tweets_july/official/cleaned_tweets/marawi_tweets_07_17.csv",
                   "../marawi_tweets_with_location/marawi_tweets_july/official/final_tweets/marawi_tweets_07_17.csv",
                   "../marawi_tweets_with_location/marawi_tweets_july/official/final_tweets/no_emotions/marawi_tweets_07_17.csv")

analyze_emotions("../marawi_tweets_with_location/marawi_tweets_july/official/cleaned_tweets/marawi_tweets_07_18.csv",
                   "../marawi_tweets_with_location/marawi_tweets_july/official/final_tweets/marawi_tweets_07_18.csv",
                   "../marawi_tweets_with_location/marawi_tweets_july/official/final_tweets/no_emotions/marawi_tweets_07_18.csv")

analyze_emotions("../marawi_tweets_with_location/marawi_tweets_july/official/cleaned_tweets/marawi_tweets_07_19.csv",
                   "../marawi_tweets_with_location/marawi_tweets_july/official/final_tweets/marawi_tweets_07_19.csv",
                   "../marawi_tweets_with_location/marawi_tweets_july/official/final_tweets/no_emotions/marawi_tweets_07_19.csv")

analyze_emotions("../marawi_tweets_with_location/marawi_tweets_july/official/cleaned_tweets/marawi_tweets_07_20.csv",
                   "../marawi_tweets_with_location/marawi_tweets_july/official/final_tweets/marawi_tweets_07_20.csv",
                   "../marawi_tweets_with_location/marawi_tweets_july/official/final_tweets/no_emotions/marawi_tweets_07_20.csv")

analyze_emotions("../marawi_tweets_with_location/marawi_tweets_july/official/cleaned_tweets/marawi_tweets_07_21.csv",
                   "../marawi_tweets_with_location/marawi_tweets_july/official/final_tweets/marawi_tweets_07_21.csv",
                   "../marawi_tweets_with_location/marawi_tweets_july/official/final_tweets/no_emotions/marawi_tweets_07_21.csv")

analyze_emotions("../marawi_tweets_with_location/marawi_tweets_july/official/cleaned_tweets/marawi_tweets_07_22.csv",
                   "../marawi_tweets_with_location/marawi_tweets_july/official/final_tweets/marawi_tweets_07_22.csv",
                   "../marawi_tweets_with_location/marawi_tweets_july/official/final_tweets/no_emotions/marawi_tweets_07_22.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_july/official/cleaned_tweets/marawi_tweets_07_23.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_july/official/final_tweets/marawi_tweets_07_23.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_july/official/final_tweets/no_emotions/marawi_tweets_07_23.csv")

# analyze_emotions("../marawi_tweets_with_location/marawi_tweets_july/official/cleaned_tweets/marawi_tweets_07_24.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_july/official/final_tweets/marawi_tweets_07_24.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_july/official/final_tweets/no_emotions/marawi_tweets_07_24.csv")

analyze_emotions("../marawi_tweets_with_location/marawi_tweets_july/official/cleaned_tweets/marawi_tweets_07_25.csv",
                   "../marawi_tweets_with_location/marawi_tweets_july/official/final_tweets/marawi_tweets_07_25.csv",
                   "../marawi_tweets_with_location/marawi_tweets_july/official/final_tweets/no_emotions/marawi_tweets_07_25.csv")

analyze_emotions("../marawi_tweets_with_location/marawi_tweets_july/official/cleaned_tweets/marawi_tweets_07_26.csv",
                   "../marawi_tweets_with_location/marawi_tweets_july/official/final_tweets/marawi_tweets_07_26.csv",
                   "../marawi_tweets_with_location/marawi_tweets_july/official/final_tweets/no_emotions/marawi_tweets_07_26.csv")

analyze_emotions("../marawi_tweets_with_location/marawi_tweets_july/official/cleaned_tweets/marawi_tweets_07_27.csv",
                   "../marawi_tweets_with_location/marawi_tweets_july/official/final_tweets/marawi_tweets_07_27.csv",
                   "../marawi_tweets_with_location/marawi_tweets_july/official/final_tweets/no_emotions/marawi_tweets_07_27.csv")

analyze_emotions("../marawi_tweets_with_location/marawi_tweets_july/official/cleaned_tweets/marawi_tweets_07_28.csv",
                   "../marawi_tweets_with_location/marawi_tweets_july/official/final_tweets/marawi_tweets_07_28.csv",
                   "../marawi_tweets_with_location/marawi_tweets_july/official/final_tweets/no_emotions/marawi_tweets_07_28.csv")

analyze_emotions("../marawi_tweets_with_location/marawi_tweets_july/official/cleaned_tweets/marawi_tweets_07_29.csv",
                   "../marawi_tweets_with_location/marawi_tweets_july/official/final_tweets/marawi_tweets_07_29.csv",
                   "../marawi_tweets_with_location/marawi_tweets_july/official/final_tweets/no_emotions/marawi_tweets_07_29.csv")

analyze_emotions("../marawi_tweets_with_location/marawi_tweets_july/official/cleaned_tweets/marawi_tweets_07_30.csv",
                   "../marawi_tweets_with_location/marawi_tweets_july/official/final_tweets/marawi_tweets_07_30.csv",
                   "../marawi_tweets_with_location/marawi_tweets_july/official/final_tweets/no_emotions/marawi_tweets_07_30.csv")

analyze_emotions("../marawi_tweets_with_location/marawi_tweets_july/official/cleaned_tweets/marawi_tweets_07_31.csv",
                   "../marawi_tweets_with_location/marawi_tweets_july/official/final_tweets/marawi_tweets_07_31.csv",
                   "../marawi_tweets_with_location/marawi_tweets_july/official/final_tweets/no_emotions/marawi_tweets_07_31.csv")
