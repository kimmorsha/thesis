# -*- coding: utf-8 -*-

import csv
from polyglot.detect import Detector
import string

read_file = './marawi_tweets_with_location/marawi_tweets_may/marawi_tweets_05_24_to_05_27.csv'
# write_file_with_locations = "../marawi_tweets_with_locations_separation/marawi_tweets_may/with_locations/marawi_tweets_with_locations_05_29_to_05_30.csv"
# write_file_with_no_locations = "../marawi_tweets_with_locations_separation/marawi_tweets_may/no_locations/marawi_tweets_with_no_locations_05_29_to_05_30.csv"

#--------------------------------------------------------------------------------------------------
def separate_csv_per_day(read_path):
    write_path1 = './marawi_tweets_with_location/marawi_tweets_may/marawi_tweets_05_24_to_05_27/marawi_tweets_05_24_to_05_25.csv'
    write_path2 = './marawi_tweets_with_location/marawi_tweets_may/marawi_tweets_05_24_to_05_27/marawi_tweets_05_25_to_05_26.csv'
    write_path3 = './marawi_tweets_with_location/marawi_tweets_may/marawi_tweets_05_24_to_05_27/marawi_tweets_05_26_to_05_27.csv'
    write_path4 = './marawi_tweets_with_location/marawi_tweets_may/marawi_tweets_05_24_to_05_27/marawi_tweets_05_extra.csv'

    with open (write_path1, 'w') as outFile1, open (write_path2, 'w') as outFile2, open (write_path3, 'w') as outFile3, open (write_path4, 'w') as outFile4:
        file_writer_1 = csv.writer(outFile1)
        file_writer_2 = csv.writer(outFile2)
        file_writer_3 = csv.writer(outFile3)
        file_writer_4 = csv.writer(outFile4)

        with open(read_path,'r') as inFile:
            file_reader = csv.reader(inFile)
            for row in file_reader:
                date = row[1]
            	print(date)
                data = [row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9]]

                if "2017-05-24" in date:
                    print("belongs in 2017-05-24")
                    file_writer_1.writerow(data)
                elif "2017-05-25" in date:
                    print("belongs in 2017-05-25")
                    file_writer_2.writerow(data)
                elif "2017-05-26" in date:
                    print("belongs in 2017-05-26")
                    file_writer_3.writerow(data)
                else:
                    print("belongs in someone else mehehe")
                    file_writer_4.writerow(data)


#-----------------------------------------------------------------------------------------------------
separate_csv_per_day(read_file)