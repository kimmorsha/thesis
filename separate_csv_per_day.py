# -*- coding: utf-8 -*-

import csv
from polyglot.detect import Detector
import string

read_file = './marawi_tweets_with_location/marawi_tweets_september/by_batch/marawi_tweets_09_10_to_09_15.csv'
# write_file_with_locations = "../marawi_tweets_with_locations_separation/marawi_tweets_may/with_locations/marawi_tweets_with_locations_05_29_to_05_30.csv"
# write_file_with_no_locations = "../marawi_tweets_with_locations_separation/marawi_tweets_may/no_locations/marawi_tweets_with_no_locations_05_29_to_05_30.csv"

#--------------------------------------------------------------------------------------------------
def separate_csv_per_day(read_path):
    write_path1 = './marawi_tweets_with_location/marawi_tweets_september/marawi_tweets_09_10_to_09_11.csv'
    write_path2 = './marawi_tweets_with_location/marawi_tweets_september/marawi_tweets_09_11_to_09_12.csv'
    write_path3 = './marawi_tweets_with_location/marawi_tweets_september/marawi_tweets_09_12_to_09_13.csv'
    write_path4 = './marawi_tweets_with_location/marawi_tweets_september/marawi_tweets_09_13_to_09_14.csv'
    write_path5 = './marawi_tweets_with_location/marawi_tweets_september/marawi_tweets_09_14_to_09_15.csv'
    write_path6 = './marawi_tweets_with_location/marawi_tweets_september/marawi_tweets_09_15_extra.csv'
   
    with open (write_path1, 'w') as outFile1, open (write_path2, 'w') as outFile2, open (write_path6, 'w') as outFile6, open (write_path3, 'w') as outFile3, open (write_path4, 'w') as outFile4, open (write_path5, 'w') as outFile5:
        file_writer_1 = csv.writer(outFile1)
        file_writer_2 = csv.writer(outFile2)
        file_writer_3 = csv.writer(outFile3)
        file_writer_4 = csv.writer(outFile4)
        file_writer_5 = csv.writer(outFile5)
        file_writer_6 = csv.writer(outFile6)

        with open(read_path,'r') as inFile:
            file_reader = csv.reader(inFile)
            for row in file_reader:
                date = row[1]
            	print(date)
                data = [row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9]]

                if "2017-09-10" in date:
                    print("belongs in 2017-09-10")
                    file_writer_1.writerow(data)
                elif "2017-09-11" in date:
                    print("belongs in 2017-09-11")
                    file_writer_2.writerow(data)
                elif "2017-09-12" in date:
                    print("belongs in 2017-09-12")
                    file_writer_3.writerow(data)
                elif "2017-09-13" in date:
                    print("belongs in 2017-09-13")
                    file_writer_4.writerow(data)
                elif "2017-09-14" in date:
                    print("belongs in 2017-09-14")
                    file_writer_5.writerow(data)
                else:
                    print("belongs in 2017-09-15")
                    file_writer_6.writerow(data)


#-----------------------------------------------------------------------------------------------------
separate_csv_per_day(read_file)