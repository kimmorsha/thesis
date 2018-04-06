# -*- coding: utf-8 -*-

import csv
import string
from geopy.geocoders import Nominatim
geolocator = Nominatim()
from geopy.exc import GeocoderTimedOut

# file_to_read = "../marawi_tweets_with_location/marawi_tweets_september/official/final_tweets/marawi_tweets_09_03.csv"
# file_to_write1 = "../marawi_tweets_with_location/marawi_tweets_september/official/philippines_tweets/marawi_tweets_09_03.csv"
# file_to_write2 = "../marawi_tweets_with_location/marawi_tweets_september/official/other_locations/marawi_tweets_09_03.csv"
location = "(['MSU', ' Marawi City', ' Philippines'], Location((45.6639448, -111.076470877, 0.0)))"
#------------------------------------------------------------------------------------------------------
def csv_read_and_write(read_path, write_path1, write_path2):
    with open (write_path1, 'wb') as outFile1, open(write_path2, 'wb') as outFile2:
        file_writer1 = csv.writer(outFile1)
        file_writer2 = csv.writer(outFile2)

        with open(read_path,'r') as inFile:
            fileReader = csv.reader(inFile)
            for row in fileReader:
                loc = row[5]
                print("location : " + str(loc))
                location = get_location(loc)
                print("Address : " + str(location.address))
                print("Latitude : " + str(location.latitude))
                print("Longitude : " + str(location.longitude))

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
def get_location(location):

    if location is not None:
        index = find_nth(location, "]", 1)
        print("Index of Last Bracket of Place = " + str(index))
        # length = len(location) + 1
        place = location[:index]
        print("Place String = " + str(place))

        index_2 = find_nth(place, "[", 1)
        print("index of [ = " + str(index_2)) 
        place = place[index_2+1:]
        print("place String = " + str(place))

        # for special cases: ACRONYMS
        place = place.encode('utf-8')

        if "'CEB'" in place:
            place.replace("'CEB'", "Cebu")
        elif "'MNL'" in place:
            place.replace("'MNL'", "Manila")
        elif "'LB'" in place:
            place.replace("'LB'", "Los Baños")


        location = geolocator.geocode(place)

        return location
    else:
        return None

#-----------------------------------------------------------------------------------------------------
def is_philippines(address):
    address = address.lower()
    return "philippines" in address:
        
#-----------------------------------------------------------------------------------------------------
def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start

#-----------------------------------------------------------------------------------------------------

csv_read_and_write(location)