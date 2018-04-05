# -*- coding: utf-8 -*-

import csv
import string
from geopy.geocoders import Nominatim
geolocator = Nominatim()
from geopy.exc import GeocoderTimedOut

# file_to_read = "../marawi_tweets_with_location/marawi_tweets_september/official/final_tweets/marawi_tweets_09_03.csv"
# file_to_write1 = "../marawi_tweets_with_location/marawi_tweets_september/official/philippines_tweets/marawi_tweets_09_03.csv"
# file_to_write2 = "../marawi_tweets_with_location/marawi_tweets_september/official/other_locations/marawi_tweets_09_03.csv"
location = "(['San Ildefonso', ' Central Luzon'], Location((18.04891605, -66.3510015447, 0.0)))"
#------------------------------------------------------------------------------------------------------
def csv_read_and_write(location):
    # with open (write_path1, 'wb') as outFile1, open(write_path2, 'wb') as outFile2:
    #     file_writer1 = csv.writer(outFile1)
    #     file_writer2 = csv.writer(outFile2)

    #     with open(read_path,'r') as inFile:
    #         fileReader = csv.reader(inFile)
    #         for row in fileReader:
    #             location = row[5]
                # print("location : " + location)
                phil_loc = is_philippinelocation(location)

                # data = [row[0],
                #         row[1],
                #         row[2],
                #         row[3],
                #         row[4],
                #         row[5],
                #         row[6],
                #         row[7],
                #         row[8],
                #         row[9],
                #         row[10]]

                '''
                Keywords:
                    'PH' 
                    'philippines' 
                    'Republic of the Philippines'
                    ''
                '''

                # if phil_loc is True:
                # 	file_writer1.writerow(data)
                # else:
                # 	file_writer2.writerow(data)
#-----------------------------------------------------------------------------------------------------
def is_philippinelocation(location):
    index = find_str(location, "Location")
    print("Index of Location = " + str(index))
    length = len(location) + 1
    coordinates = location[index:length]
    print("Coordinates String = " + str(coordinates))

    index_2 = find_nth(coordinates, "(", 2)
    print("index of ( = " + str(index_2)) 
    coordinates = coordinates[index_2+1:]
    print("Coordinates String = " + str(coordinates))

    index_2 = find_nth(coordinates, ",", 2)
    print("index of , = " + str(index_2)) 
    coordinates = coordinates[:index_2]
    print("Coordinates String = " + str(coordinates))

    location = geolocator.reverse(coordinates)
    print("Country =    " + str(location.address.country))

    return True

#-----------------------------------------------------------------------------------------------------
def find_str(s, char):
    index = 0

    if char in s:
        c = char[0]
        for ch in s:
            if ch == c:
                if s[index:index+len(char)] == char:
                    return index

            index += 1

    return -1

def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start

csv_read_and_write(location)