# -*- coding: utf-8 -*-

import csv
import string
from geopy.geocoders import Nominatim
geolocator = Nominatim()
from geopy.exc import GeocoderTimedOut
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

file_to_read = "../marawi_tweets_with_location/marawi_tweets_september/official/final_tweets/marawi_tweets_09_03.csv"
file_to_write1 = "../marawi_tweets_with_location/marawi_tweets_september/official/final_tweets/philippines_tweets/marawi_tweets_09_03.csv"
file_to_write2 = "../marawi_tweets_with_location/marawi_tweets_september/official/final_tweets/other_locations/marawi_tweets_09_03.csv"
# location = "(['MSU', ' Marawi City'], Location((45.6639448, -111.076470877, 0.0)))"
#------------------------------------------------------------------------------------------------------
def csv_read_and_write(read_path, write_path1, write_path2):
    with open (write_path1, 'wb') as outFile1, open(write_path2, 'wb') as outFile2:
        file_writer1 = csv.writer(outFile1)
        file_writer2 = csv.writer(outFile2)

        with open(read_path,'r') as inFile:
            fileReader = csv.reader(inFile)
            for row in fileReader:

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

                location = row[5]
                print("location : " + str(location))

                if location is not None:
                    index = find_nth(location, "]", 1)
                    place = location[:index]
                    index_2 = find_nth(place, "[", 1)
                    place = place[index_2+1:]
                    place = place.upper()
                    print("place String = " + str(place))

                    # for special cases: ACRONYMS
                    place = place.encode('utf-8')

                    if "'CEB'" in place:
                        place = place.replace("'CEB'", "Cebu")
                    elif "'BUDA'" in place:
                        place = place.replace("'BUDA'", "Bukidnon-Davao")
                    elif "'MNL'" in place:
                        place = place.replace("'MNL'", "Manila")
                    elif "'LB'" in place:
                        place = place.replace("'LB'", "Los Baños")
                    elif "'COMVAL'" in place:
                        place = place.replace("'COMVAL'", "Compostela Valley")
                    elif "'CAR'" in place:
                        place = place.replace("'CAR'", "Cordillera Administrative Region")
                    elif "'CDO'" in place:
                        place = place.replace("'CDO'", "Cagayan de Oro")
                    elif "'CAR'" in place:
                        place = place.replace("'CAR'", "Cordillera Administrative Region")
                    elif "'LP'" in place:
                        place = place.replace("'LP'", "Las Piñas")
                    elif "'NCR'" in place:
                        place = place.replace("'NCR'", "National Capital Region")
                    elif "'BCD'" in place:
                        place = place.replace("'BCD'", "Bacolod")
                    elif "'DGT'" in place:
                        place = place.replace("'DGT'", "Dumaguete")
                    elif "'DVO'" in place:
                        place = place.replace("'DVO'", "Davao")
                    elif "'ILO'" in place:
                        place = place.replace("'ILO'", "Iloilo")
                    elif "'KLO'" in place:
                        place = place.replace("'KLO'", "Kalibo, Aklan")
                    elif "'LP'" in place:
                        place = place.replace("'LP'", "Las Piñas")
                    elif "'NEGOCC'" in place:
                        place = place.replace("'NEGOCC'", "Negros Occidental")
                    elif "'NEGOR'" in place:
                        place = place.replace("'NEGOR'", "Negros Oriental")
                    elif "'QC'" in place:
                        place = place.replace("'QC'", "Quezon City")
                    elif "'GENSAN'" in place:
                        place = place.replace("'GENSAN'", "General Santos")
                    elif "'GES'" in place:
                        place = place.replace("'GES'", "General Santos")
                    elif "'ZC'" in place:
                        place = place.replace("'ZC'", "Zamboanga City")
                    elif "'ZAM'" in place:
                        place = place.replace("'ZAM'", "Zamboanga City")
                    elif "'NRA'" in place:
                        place = place.replace("'NRA'", "''")


                    location = geolocator.geocode(place)

                    print("Address : " + str(location))

                    if location.address is not None and "Philippines" in location.address:
                        loc = "([" + str(location.address) + "], Location((" + str(location.latitude) + "," + str(location.latitude) + ")))"
                        data = [row[0],
                                row[1],
                                row[2],
                                loc,
                                row[4],
                                row[5],
                                row[6],
                                row[7],
                                row[8],
                                row[9],
                                row[10]]
                        file_writer1.writerow(data)
                    else:
                        file_writer2.writerow(data)
                else:
                    file_writer2.writerow(data)

#-----------------------------------------------------------------------------------------------------
def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start

#-----------------------------------------------------------------------------------------------------

csv_read_and_write(location)