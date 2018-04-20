# -*- coding: utf-8 -*-

import csv
from polyglot.detect import Detector
import string

read_file1 = '../marawi_tweets_with_location/marawi_tweets_may/official/final_tweets/philippines_tweets/marawi_tweets_05_24.csv'
read_file2 = '../marawi_tweets_with_location/marawi_tweets_may/official/final_tweets/philippines_tweets/marawi_tweets_05_25.csv'
read_file3 = '../marawi_tweets_with_location/marawi_tweets_may/official/final_tweets/philippines_tweets/marawi_tweets_05_26.csv'
read_file4 = '../marawi_tweets_with_location/marawi_tweets_may/official/final_tweets/philippines_tweets/marawi_tweets_05_27.csv'
read_file5 = '../marawi_tweets_with_location/marawi_tweets_may/official/final_tweets/philippines_tweets/marawi_tweets_05_28.csv'
read_file6 = '../marawi_tweets_with_location/marawi_tweets_may/official/final_tweets/philippines_tweets/marawi_tweets_05_29.csv'
read_file7 = '../marawi_tweets_with_location/marawi_tweets_may/official/final_tweets/philippines_tweets/marawi_tweets_05_30.csv'
read_file8 = '../marawi_tweets_with_location/marawi_tweets_may/official/final_tweets/philippines_tweets/marawi_tweets_05_31.csv'
write_file = '../marawi_tweets_with_location/marawi_tweets_may/official/final_tweets/philippines_tweets/marawi_tweets_may.csv'

#--------------------------------------------------------------------------------------------------
def append_by_month(read_path1, read_path2, read_path3, read_path4, read_path5, read_path6, read_path7, read_path8, write_path):
    with open (write_path, 'wb') as outFile:
        file_writer = csv.writer(outFile)

        with open(read_path1,'r') as inFile:
            file_reader = csv.reader(inFile)

            for row in file_reader:
                data = [row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10]]
                file_writer.writerow(data)

    with open (write_path, 'ab') as outFile: 
        file_writer = csv.writer(outFile)

        with open(read_path2,'r') as inFile:
            file_reader = csv.reader(inFile)

            for row in file_reader:
                data = [row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10]]
                file_writer.writerow(data)

    with open (write_path, 'ab') as outFile: 
        file_writer = csv.writer(outFile)

        with open(read_path3,'r') as inFile:
            file_reader = csv.reader(inFile)

            for row in file_reader:
                data = [row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10]]
                file_writer.writerow(data)

    with open (write_path, 'ab') as outFile: 
        file_writer = csv.writer(outFile)

        with open(read_path4,'r') as inFile:
            file_reader = csv.reader(inFile)

            for row in file_reader:
                data = [row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10]]
                file_writer.writerow(data)

    with open (write_path, 'ab') as outFile: 
        file_writer = csv.writer(outFile)

        with open(read_path5,'r') as inFile:
            file_reader = csv.reader(inFile)

            for row in file_reader:
                data = [row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10]]
                file_writer.writerow(data)

    with open (write_path, 'ab') as outFile: 
        file_writer = csv.writer(outFile)

        with open(read_path6,'r') as inFile:
            file_reader = csv.reader(inFile)

            for row in file_reader:
                data = [row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10]]
                file_writer.writerow(data)

    with open (write_path, 'ab') as outFile: 
        file_writer = csv.writer(outFile)

        with open(read_path7,'r') as inFile:
            file_reader = csv.reader(inFile)

            for row in file_reader:
                data = [row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10]]
                file_writer.writerow(data)

    with open (write_path, 'ab') as outFile: 
        file_writer = csv.writer(outFile)

        with open(read_path8,'r') as inFile:
            file_reader = csv.reader(inFile)

            for row in file_reader:
                data = [row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10]]
                file_writer.writerow(data)
#-----------------------------------------------------------------------------------------------------
append_by_month(read_file1, read_file2, read_file3, read_file4, read_file5, read_file6, read_file7, read_file8, write_file)


