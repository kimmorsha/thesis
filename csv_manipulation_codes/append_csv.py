# -*- coding: utf-8 -*-

import csv
from polyglot.detect import Detector
import string

read_file1 = '../marawi_tweets_with_location/marawi_tweets_september/marawi_tweets_09_15_1.csv'
read_file2 = '../marawi_tweets_with_location/marawi_tweets_september/marawi_tweets_09_15_2.csv'
write_file = '../marawi_tweets_with_location/marawi_tweets_september/marawi_tweets_09_15.csv'

# write_file_with_locations = "../marawi_tweets_with_locations_separation/marawi_tweets_september/with_locations/marawi_tweets_with_locations_06_05_to_06_30.csv"
# write_file_with_no_locations = "../marawi_tweets_with_locations_separation/marawi_tweets_september/no_locations/marawi_tweets_with_no_locations_06_05_to_06_30.csv"

#--------------------------------------------------------------------------------------------------
def append_csv_files(read_path1, read_path2, write_path):
    with open (write_path, 'w') as outFile: #, open (write_path2, 'w') as outFile2, open (write_path6, 'w') as outFile6, open (write_path3, 'w') as outFile3, open (write_path4, 'w') as outFile4, open (write_path5, 'w') as outFile5:
        file_writer = csv.writer(outFile)

        with open(read_path1,'r') as inFile:
            file_reader = csv.reader(inFile)

            for row in file_reader:
                data = [row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9]]
                file_writer.writerow(data)

    with open (write_path, 'ab') as outFile: #, open (write_path2, 'w') as outFile2, open (write_path6, 'w') as outFile6, open (write_path3, 'w') as outFile3, open (write_path4, 'w') as outFile4, open (write_path5, 'w') as outFile5:
        file_writer = csv.writer(outFile)

        with open(read_path2,'r') as inFile:
            file_reader = csv.reader(inFile)

            for row in file_reader:
                date = row[1]
                data = [row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9]]
                if "9/15/2017" in date or "2017-09-15" in date:
                    print(date)
                    file_writer.writerow(data)
                else:
                    print("doesnt belong")


#-----------------------------------------------------------------------------------------------------
append_csv_files(read_file1, read_file2, write_file)