# -*- coding: utf-8 -*-

import csv
import string

file_to_read = "../marawi_tweets_with_location/marawi_tweets_september/official/cleaned_tweets/marawi_tweets_09_03.csv"
file_to_write1 = "../marawi_tweets_with_location/marawi_tweets_september/official/philippines_tweets/marawi_tweets_09_03.csv"
file_to_write2 = "../marawi_tweets_with_location/marawi_tweets_september/official/other_locations/marawi_tweets_09_03.csv"

#------------------------------------------------------------------------------------------------------
def csv_read_and_write(read_path, write_path1, write_path2):
    with open (write_path1, 'wb') as outFile1, open(write_path2, 'wb') as outFile2:
        file_writer1 = csv.writer(outFile1)
        file_writer2 = csv.writer(outFile2)

        with open(read_path,'r') as inFile:
            fileReader = csv.reader(inFile)
            for row in fileReader:
                location = row[5]
                # print("location : " + location)
                phil_loc = is_philippinelocation(location)

                data = [row[0],
                        row[1],
                        row[2],
                        row[3],
                        row[4],
                        row[5],
                        row[6],
                        row[7],
                        row[8],
                        row[9],
                        row[10]]

                if phil_loc is True:
                	file_writer1.writerow(data)
                else:
                	file_writer2.writerow(data)
#-----------------------------------------------------------------------------------------------------
def is_philippinelocation(location):
	name = location.
	print(name)
	return True


#-----------------------------------------------------------------------------------------------------

csv_read_and_write(file_to_read, file_to_write1, file_to_write2)