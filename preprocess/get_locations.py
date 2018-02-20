# -*- coding: utf-8 -*-

import csv
from polyglot.detect import Detector
import string

file_to_read = "../marawi_tweets_with_location/marawi_tweets_august/marawi_tweets_08_02_to_08_03.csv"
file_to_write = "../marawi_tweets_with_locations_only/marawi_tweets_august/marawi_tweets_with_locations_08_02_to_08_03.csv"

#--------------------------------------------------------------------------------------------------
def write_new_csv_with_locations(read_path, write_path):
    with open(write_path ,'w') as outFile:
        fileWriter = csv.writer(outFile)
        i = 1;
        with open(read_path,'r') as inFile:
            fileReader = csv.reader(inFile)
            for row in fileReader:
            	print(row[5])
                if row[5] in (None, ""):
                	continue
                else:
					print(i)
					data = [row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9]]
					fileWriter.writerow(data)
                i = i + 1

#-----------------------------------------------------------------------------------------------------
write_new_csv_with_locations(file_to_read, file_to_write)