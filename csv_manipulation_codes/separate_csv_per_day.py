# -*- coding: utf-8 -*-

import csv
from polyglot.detect import Detector
import string

#  EDIT!!!!
read_file = '../to_be_skimbordeng/with_locations/marawi_tweets_09_17_to_09_18.csv'
# write_file_with_locations = "../to_be_skimbordengswith_locations_tweets_may/with_locations/to_be_skimbordengswith_locationsv"
# write_file_with_no_locations = "../to_be_skimbordengswith_locations_tweets_may/no_locations/marawi_tweets_with_no_locations_05_29_to_05_30.csv"

#--------------------------------------------------------------------------------------------------
def separate_csv_per_day(read_path):
    write_path1 = '../to_be_skimbordeng/with_locations/marawi_tweets_09_17_1.csv'
    write_path2 = '../to_be_skimbordeng/with_locations/marawi_tweets_09_18_2.csv'
    # write_path3 = '../to_be_skimbordeng/with_locations/marawi_tweets_09_23.csv'
    # write_path4 = '../to_be_skimbordeng/with_locations/marawi_tweets_09_24_2.csv'
    # write_path5 = '../to_be_skimbordeng/with_locations/marawi_tweets_09_09.csv'
    # write_path6 = '../to_be_skimbordeng/with_locations/marawi_tweets_09_09_2.csv'
    # write_path7 = './to_be_skimbordeng/with_locations/marawi_tweets_31_30.csv'
    # write_path8 = './to_be_skimbordeng/with_locations/marawi_tweets_31_31.csv'
    # write_path9 = './to_be_skimbordeng/with_locations/marawi_tweets_31_01.csv'
    # write_path09 = './to_be_skimbordeng/with_locations/marawi_tweets_31_02_2.csv'
    
    with open (write_path1, 'w') as outFile1, open (write_path2, 'w') as outFile2: #, open (write_path3, 'w') as outFile3, open (write_path4, 'w') as outFile4: #, open (write_path5, 'w') as outFile5, open (write_path6, 'w') as outFile6:#, open (write_path7, 'w') as outFile7, open (write_path8, 'w') as outFile8, open (write_path9, 'w') as outFile9, open (write_path09, 'w') as outFile09:
        file_writer_1 = csv.writer(outFile1)
        file_writer_2 = csv.writer(outFile2)
        # file_writer_3 = csv.writer(outFile3)
        # file_writer_4 = csv.writer(outFile4)
        # file_writer_5 = csv.writer(outFile5)
        # file_writer_6 = csv.writer(outFile6)
        # file_writer_7 = csv.writer(outFile7)
        # file_writer_8 = csv.writer(outFile8)
        # file_writer_9 = csv.writer(outFile9)
        # file_writer_09 = csv.writer(outFile09)

        with open(read_path,'r') as inFile:
            file_reader = csv.reader(inFile)
            for row in file_reader:
                date = row[1]

                # print(row[9])
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

                if "09/17/2017" in date or "2017-09-17" in date:
                    # print("belongs in 2017-08-05")
                    file_writer_1.writerow(data)
                elif "09/18/2017" in date or "2017-09-18" in date:
                    # print("belongs in 2017-06-06")
                    file_writer_2.writerow(data)
                # elif "09/23/2017" in date or "2017-09-23" in date:
                #     #print("belongs in 2017-14-05")
                #     file_writer_3.writerow(data)    
                # elif "09/24/2017" in date or "2017-09-24" in date:
                #     #print("belongs in 2017-14-05")
                #     file_writer_4.writerow(data)
                # elif "9/9/2017" in date or "2017-09-09" in date:
                #     #print("belongs in 2017-14-05")
                #     file_writer_5.writerow(data)
                # elif "9/09/2017" in date or "2017-09-09" in date:
                #     #print("belongs in 2017-14-05")
                #     file_writer_6.writerow(data)
                # elif "2017-08-30" in date:
                #     #print("belongs in 2017-14-05")
                #     file_writer_7.writerow(data)
                # elif "2017-08-31" in date:
                #     #print("belongs in 2017-14-05")
                #     file_writer_8.writerow(data)
                # elif "2017-31-0" in date:
                #     #print("belongs in 2017-14-05")
                #     file_writer_9.writerow(data)
                # elif "2017-31-0" in date:
                #     #print("belongs in 2017-14-05")
                #     file_writer_09.writerow(data)
                else:
                    #file_writer_3.writerow(data)
                    print("belongs somewhere else")
                    #file_writer_3.writerow(data)


#-----------------------------------------------------------------------------------------------------
separate_csv_per_day(read_file)