# -*- coding: utf-8 -*-

import csv
import string
from geopy.geocoders import Nominatim
geolocator = Nominatim()
from geopy.exc import GeocoderTimedOut
import sys
geolocator=Nominatim(timeout=5)

reload(sys)
sys.setdefaultencoding('utf-8')

# file_to_read = "../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/prayformarawi_tweets/prayformarawi_tweets/prayformarawi_tweets/prayformarawi_tweets/marawi_tweets_06_02.csv"
# file_to_write1 = "../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/prayformarawi_tweets/prayformarawi_tweets/prayformarawi_tweets/prayformarawi_tweets/philippines_tweets/marawi_tweets_06_02.csv"
# file_to_write2 = "../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/prayformarawi_tweets/prayformarawi_tweets/prayformarawi_tweets/prayformarawi_tweets/other_locations/marawi_tweets_06_02.csv"
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
                        row[9]]

                location = row[3]
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

                    if "'Philippines'" in place or "' Philippines'" in place or "'PHILIPPINES'" in place or "' PHILIPPINES'" in place or "' PH'" in place or "'PH'" in place or "PHILIPPINES" in place:
                        file_writer1.writerow(data)
                        print("***** in the PHILS. | Address : " + str(location))
                    else:
                        # if "'CEB'" in place:
                        #     place = place.replace("'CEB'", "Cebu")
                        # elif "'BUDA'" in place:
                        #     place = place.replace("'BUDA'", "Bukidnon-Davao")
                        # elif "'MNL'" in place:
                        #     place = place.replace("'MNL'", "Manila")
                        # elif "'LB'" in place:
                        #     place = place.replace("'LB'", "Los Baños")
                        # elif "'COMVAL'" in place:
                        #     place = place.replace("'COMVAL'", "Compostela Valley")
                        # elif "'CAR'" in place:
                        #     place = place.replace("'CAR'", "Cordillera Administrative Region")
                        # elif "'CDO'" in place:
                        #     place = place.replace("'CDO'", "Cagayan de Oro")
                        # elif "'CAR'" in place:
                        #     place = place.replace("'CAR'", "Cordillera Administrative Region")
                        # elif "'LP'" in place:
                        #     place = place.replace("'LP'", "Las Piñas")
                        # elif "'NCR'" in place:
                        #     place = place.replace("'NCR'", "National Capital Region")
                        # elif "'BCD'" in place:
                        #     place = place.replace("'BCD'", "Bacolod")
                        # elif "'DGT'" in place:
                        #     place = place.replace("'DGT'", "Dumaguete")
                        # elif "'DVO'" in place:
                        #     place = place.replace("'DVO'", "Davao")
                        # elif "'ILO'" in place:
                        #     place = place.replace("'ILO'", "Iloilo")
                        # elif "'KLO'" in place:
                        #     place = place.replace("'KLO'", "Kalibo, Aklan")
                        # elif "'LP'" in place:
                        #     place = place.replace("'LP'", "Las Piñas")
                        # elif "'NEGOCC'" in place:
                        #     place = place.replace("'NEGOCC'", "Negros Occidental")
                        # elif "'NEGOR'" in place:
                        #     place = place.replace("'NEGOR'", "Negros Oriental")
                        # elif "'QC'" in place:
                        #     place = place.replace("'QC'", "Quezon City")
                        # elif "'GENSAN'" in place:
                        #     place = place.replace("'GENSAN'", "General Santos")
                        # elif "'GES'" in place:
                        #     place = place.replace("'GES'", "General Santos")
                        # elif "'ZC'" in place:
                        #     place = place.replace("'ZC'", "Zamboanga City")
                        # elif "'ZAM'" in place:
                        #     place = place.replace("'ZAM'", "Zamboanga City")
                        # elif "'NRA'" in place:
                        #     place = place.replace("'NRA'", "''")


                        # location = geolocator.geocode(place)

                        # print("Address : " + str(location))

                        # if location is not None and "Philippines" in location.address:
                        #     loc = "([" + str(location.address) + "], Location((" + str(location.latitude) + "," + str(location.latitude) + ")))"
                        #     data = [row[0],
                        #             row[1],
                        #             row[2], 
                        #             loc,
                        #             row[4],
                        #             row[5],
                        #             row[6],
                        #             row[7],
                        #             row[8],
                        #             row[9],
                        #             row[10]]
                        #     file_writer1.writerow(data)
                        #     print("***** in the PHILS. | Address : " + str(location))
                        # else:
                        file_writer2.writerow(data)
                        print("###### NOPE | Address : " + str(location))
                else:
                    file_writer2.writerow(data)
                    print("###### NOPE | Address : " + str(location))

#-----------------------------------------------------------------------------------------------------
def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start

#-----------------------------------------------------------------------------------------------------
def do_geocode(address):
    try:
        return geopy.geocode(address)
    except GeocoderTimedOut:
        return do_geocode(address)

#-----------------------------------------------------------------------------------------------------

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_may/official/prayformarawi_tweets/raw/marawi_tweets_05_23.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_may/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_05_23.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_may/official/prayformarawi_tweets/other_locations/marawi_tweets_05_23.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_may/official/prayformarawi_tweets/raw/marawi_tweets_05_24.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_may/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_05_24.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_may/official/prayformarawi_tweets/other_locations/marawi_tweets_05_24.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_may/official/prayformarawi_tweets/raw/marawi_tweets_05_25.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_may/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_05_25.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_may/official/prayformarawi_tweets/other_locations/marawi_tweets_05_25.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_may/official/prayformarawi_tweets/raw/marawi_tweets_05_26.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_may/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_05_26.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_may/official/prayformarawi_tweets/other_locations/marawi_tweets_05_26.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_may/official/prayformarawi_tweets/raw/marawi_tweets_05_27.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_may/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_05_27.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_may/official/prayformarawi_tweets/other_locations/marawi_tweets_05_27.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_may/official/prayformarawi_tweets/raw/marawi_tweets_05_28.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_may/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_05_28.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_may/official/prayformarawi_tweets/other_locations/marawi_tweets_05_28.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_may/official/prayformarawi_tweets/raw/marawi_tweets_05_29.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_may/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_05_29.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_may/official/prayformarawi_tweets/other_locations/marawi_tweets_05_29.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_may/official/prayformarawi_tweets/raw/marawi_tweets_05_30.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_may/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_05_30.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_may/official/prayformarawi_tweets/other_locations/marawi_tweets_05_30.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_may/official/prayformarawi_tweets/raw/marawi_tweets_05_31.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_may/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_05_31.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_may/official/prayformarawi_tweets/other_locations/marawi_tweets_05_31.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/raw/marawi_tweets_06_01.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_06_01.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/other_locations/marawi_tweets_06_01.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/raw/marawi_tweets_06_02.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_06_02.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/other_locations/marawi_tweets_06_02.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/raw/marawi_tweets_06_03.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_06_03.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/other_locations/marawi_tweets_06_03.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/raw/marawi_tweets_06_04.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_06_04.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/other_locations/marawi_tweets_06_04.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/raw/marawi_tweets_06_05.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_06_05.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/other_locations/marawi_tweets_06_05.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/raw/marawi_tweets_06_06.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_06_06.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/other_locations/marawi_tweets_06_06.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/raw/marawi_tweets_06_07.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_06_07.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/other_locations/marawi_tweets_06_07.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/raw/marawi_tweets_06_08.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_06_08.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/other_locations/marawi_tweets_06_08.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/raw/marawi_tweets_06_09.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_06_09.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/other_locations/marawi_tweets_06_09.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/raw/marawi_tweets_06_10.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_06_10.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/other_locations/marawi_tweets_06_10.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/raw/marawi_tweets_06_11.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_06_11.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/other_locations/marawi_tweets_06_11.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/raw/marawi_tweets_06_12.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_06_12.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/other_locations/marawi_tweets_06_12.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/raw/marawi_tweets_06_13.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_06_13.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/other_locations/marawi_tweets_06_13.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/raw/marawi_tweets_06_14.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_06_14.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/other_locations/marawi_tweets_06_14.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/raw/marawi_tweets_06_15.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_06_15.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/other_locations/marawi_tweets_06_15.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/raw/marawi_tweets_06_16.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_06_16.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/other_locations/marawi_tweets_06_16.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/raw/marawi_tweets_06_17.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_06_17.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/other_locations/marawi_tweets_06_17.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/raw/marawi_tweets_06_18.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_06_18.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/other_locations/marawi_tweets_06_18.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/raw/marawi_tweets_06_19.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_06_19.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/other_locations/marawi_tweets_06_19.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/raw/marawi_tweets_06_20.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_06_20.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/other_locations/marawi_tweets_06_20.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/raw/marawi_tweets_06_21.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_06_21.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/other_locations/marawi_tweets_06_21.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/raw/marawi_tweets_06_22.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_06_22.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/other_locations/marawi_tweets_06_22.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/raw/marawi_tweets_06_23.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_06_23.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/other_locations/marawi_tweets_06_23.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/raw/marawi_tweets_06_24.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_06_24.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/other_locations/marawi_tweets_06_24.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/raw/marawi_tweets_06_25.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_06_25.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/other_locations/marawi_tweets_06_25.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/raw/marawi_tweets_06_26.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_06_26.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/other_locations/marawi_tweets_06_26.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/raw/marawi_tweets_06_27.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_06_27.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/other_locations/marawi_tweets_06_27.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/raw/marawi_tweets_06_28.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_06_28.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/other_locations/marawi_tweets_06_28.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/raw/marawi_tweets_06_29.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_06_29.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/other_locations/marawi_tweets_06_29.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/raw/marawi_tweets_06_30.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_06_30.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_june/official/prayformarawi_tweets/other_locations/marawi_tweets_06_30.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/raw/marawi_tweets_07_01.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_07_01.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/other_locations/marawi_tweets_07_01.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/raw/marawi_tweets_07_02.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_07_02.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/other_locations/marawi_tweets_07_02.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/raw/marawi_tweets_07_03.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_07_03.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/other_locations/marawi_tweets_07_03.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/raw/marawi_tweets_07_04.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_07_04.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/other_locations/marawi_tweets_07_04.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/raw/marawi_tweets_07_05.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_07_05.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/other_locations/marawi_tweets_07_05.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/raw/marawi_tweets_07_06.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_07_06.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/other_locations/marawi_tweets_07_06.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/raw/marawi_tweets_07_07.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_07_07.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/other_locations/marawi_tweets_07_07.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/raw/marawi_tweets_07_08.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_07_08.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/other_locations/marawi_tweets_07_08.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/raw/marawi_tweets_07_09.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_07_09.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/other_locations/marawi_tweets_07_09.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/raw/marawi_tweets_07_10.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_07_10.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/other_locations/marawi_tweets_07_10.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/raw/marawi_tweets_07_11.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_07_11.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/other_locations/marawi_tweets_07_11.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/raw/marawi_tweets_07_12.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_07_12.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/other_locations/marawi_tweets_07_12.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/raw/marawi_tweets_07_13.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_07_13.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/other_locations/marawi_tweets_07_13.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/raw/marawi_tweets_07_14.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_07_14.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/other_locations/marawi_tweets_07_14.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/raw/marawi_tweets_07_15.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_07_15.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/other_locations/marawi_tweets_07_15.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/raw/marawi_tweets_07_16.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_07_16.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/other_locations/marawi_tweets_07_16.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/raw/marawi_tweets_07_17.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_07_17.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/other_locations/marawi_tweets_07_17.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/raw/marawi_tweets_07_18.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_07_18.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/other_locations/marawi_tweets_07_18.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/raw/marawi_tweets_07_19.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_07_19.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/other_locations/marawi_tweets_07_19.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/raw/marawi_tweets_07_20.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_07_20.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/other_locations/marawi_tweets_07_20.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/raw/marawi_tweets_07_21.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_07_21.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/other_locations/marawi_tweets_07_21.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/raw/marawi_tweets_07_22.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_07_22.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/other_locations/marawi_tweets_07_22.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/raw/marawi_tweets_07_23.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_07_23.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/other_locations/marawi_tweets_07_23.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/raw/marawi_tweets_07_24.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_07_24.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/other_locations/marawi_tweets_07_24.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/raw/marawi_tweets_07_25.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_07_25.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/other_locations/marawi_tweets_07_25.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/raw/marawi_tweets_07_26.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_07_26.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/other_locations/marawi_tweets_07_26.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/raw/marawi_tweets_07_27.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_07_27.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/other_locations/marawi_tweets_07_27.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/raw/marawi_tweets_07_28.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_07_28.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/other_locations/marawi_tweets_07_28.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/raw/marawi_tweets_07_29.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_07_29.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/other_locations/marawi_tweets_07_29.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/raw/marawi_tweets_07_30.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_07_30.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/other_locations/marawi_tweets_07_30.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/raw/marawi_tweets_07_31.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_07_31.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_july/official/prayformarawi_tweets/other_locations/marawi_tweets_07_31.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/raw/marawi_tweets_08_01.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_08_01.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/other_locations/marawi_tweets_08_01.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/raw/marawi_tweets_08_02.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_08_02.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/other_locations/marawi_tweets_08_02.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/raw/marawi_tweets_08_03.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_08_03.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/other_locations/marawi_tweets_08_03.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/raw/marawi_tweets_08_04.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_08_04.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/other_locations/marawi_tweets_08_04.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/raw/marawi_tweets_08_05.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_08_05.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/other_locations/marawi_tweets_08_05.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/raw/marawi_tweets_08_06.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_08_06.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/other_locations/marawi_tweets_08_06.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/raw/marawi_tweets_08_07.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_08_07.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/other_locations/marawi_tweets_08_07.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/raw/marawi_tweets_08_08.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_08_08.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/other_locations/marawi_tweets_08_08.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/raw/marawi_tweets_08_09.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_08_09.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/other_locations/marawi_tweets_08_09.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/raw/marawi_tweets_08_10.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_08_10.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/other_locations/marawi_tweets_08_10.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/raw/marawi_tweets_08_11.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_08_11.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/other_locations/marawi_tweets_08_11.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/raw/marawi_tweets_08_12.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_08_12.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/other_locations/marawi_tweets_08_12.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/raw/marawi_tweets_08_13.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_08_13.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/other_locations/marawi_tweets_08_13.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/raw/marawi_tweets_08_14.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_08_14.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/other_locations/marawi_tweets_08_14.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/raw/marawi_tweets_08_15.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_08_15.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/other_locations/marawi_tweets_08_15.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/raw/marawi_tweets_08_16.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_08_16.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/other_locations/marawi_tweets_08_16.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/raw/marawi_tweets_08_17.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_08_17.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/other_locations/marawi_tweets_08_17.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/raw/marawi_tweets_08_18.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_08_18.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/other_locations/marawi_tweets_08_18.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/raw/marawi_tweets_08_19.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_08_19.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/other_locations/marawi_tweets_08_19.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/raw/marawi_tweets_08_20.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_08_20.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/other_locations/marawi_tweets_08_20.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/raw/marawi_tweets_08_21.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_08_21.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/other_locations/marawi_tweets_08_21.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/raw/marawi_tweets_08_22.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_08_22.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/other_locations/marawi_tweets_08_22.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/raw/marawi_tweets_08_23.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_08_23.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/other_locations/marawi_tweets_08_23.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/raw/marawi_tweets_08_24.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_08_24.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/other_locations/marawi_tweets_08_24.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/raw/marawi_tweets_08_25.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_08_25.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/other_locations/marawi_tweets_08_25.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/raw/marawi_tweets_08_26.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_08_26.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/other_locations/marawi_tweets_08_26.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/raw/marawi_tweets_08_27.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_08_27.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/other_locations/marawi_tweets_08_27.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/raw/marawi_tweets_08_28.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_08_28.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/other_locations/marawi_tweets_08_28.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/raw/marawi_tweets_08_29.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_08_29.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/other_locations/marawi_tweets_08_29.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/raw/marawi_tweets_08_30.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_08_30.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/other_locations/marawi_tweets_08_30.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/raw/marawi_tweets_08_31.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_08_31.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_august/official/prayformarawi_tweets/other_locations/marawi_tweets_08_31.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/raw/marawi_tweets_09_01.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_09_01.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/other_locations/marawi_tweets_09_01.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/raw/marawi_tweets_09_02.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_09_02.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/other_locations/marawi_tweets_09_02.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/raw/marawi_tweets_09_03.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_09_03.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/other_locations/marawi_tweets_09_03.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/raw/marawi_tweets_09_04.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_09_04.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/other_locations/marawi_tweets_09_04.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/raw/marawi_tweets_09_05.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_09_05.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/other_locations/marawi_tweets_09_05.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/raw/marawi_tweets_09_06.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_09_06.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/other_locations/marawi_tweets_09_06.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/raw/marawi_tweets_09_07.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_09_07.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/other_locations/marawi_tweets_09_07.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/raw/marawi_tweets_09_08.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_09_08.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/other_locations/marawi_tweets_09_08.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/raw/marawi_tweets_09_09.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_09_09.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/other_locations/marawi_tweets_09_09.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/raw/marawi_tweets_09_10.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_09_10.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/other_locations/marawi_tweets_09_10.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/raw/marawi_tweets_09_11.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_09_11.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/other_locations/marawi_tweets_09_11.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/raw/marawi_tweets_09_12.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_09_12.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/other_locations/marawi_tweets_09_12.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/raw/marawi_tweets_09_13.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_09_13.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/other_locations/marawi_tweets_09_13.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/raw/marawi_tweets_09_14.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_09_14.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/other_locations/marawi_tweets_09_14.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/raw/marawi_tweets_09_15.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_09_15.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/other_locations/marawi_tweets_09_15.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/raw/marawi_tweets_09_16.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_09_16.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/other_locations/marawi_tweets_09_16.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/raw/marawi_tweets_09_17.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_09_17.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/other_locations/marawi_tweets_09_17.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/raw/marawi_tweets_09_18.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_09_18.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/other_locations/marawi_tweets_09_18.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/raw/marawi_tweets_09_19.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_09_19.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/other_locations/marawi_tweets_09_19.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/raw/marawi_tweets_09_20.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_09_20.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/other_locations/marawi_tweets_09_20.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/raw/marawi_tweets_09_21.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_09_21.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/other_locations/marawi_tweets_09_21.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/raw/marawi_tweets_09_22.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_09_22.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/other_locations/marawi_tweets_09_22.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/raw/marawi_tweets_09_23.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_09_23.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/other_locations/marawi_tweets_09_23.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/raw/marawi_tweets_09_24.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_09_24.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/other_locations/marawi_tweets_09_24.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/raw/marawi_tweets_09_25.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_09_25.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/other_locations/marawi_tweets_09_25.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/raw/marawi_tweets_09_26.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_09_26.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/other_locations/marawi_tweets_09_26.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/raw/marawi_tweets_09_27.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_09_27.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/other_locations/marawi_tweets_09_27.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/raw/marawi_tweets_09_28.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_09_28.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/other_locations/marawi_tweets_09_28.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/raw/marawi_tweets_09_29.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_09_29.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/other_locations/marawi_tweets_09_29.csv")

# csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/raw/marawi_tweets_09_30.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_09_30.csv",
#                    "../marawi_tweets_with_location/marawi_tweets_september/official/prayformarawi_tweets/other_locations/marawi_tweets_09_30.csv")

csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/raw/marawi_tweets_10_01.csv",
                   "../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_10_01.csv",
                   "../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/other_locations/marawi_tweets_10_01.csv")

csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/raw/marawi_tweets_10_02.csv",
                   "../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_10_02.csv",
                   "../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/other_locations/marawi_tweets_10_02.csv")

csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/raw/marawi_tweets_10_03.csv",
                   "../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_10_03.csv",
                   "../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/other_locations/marawi_tweets_10_03.csv")

csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/raw/marawi_tweets_10_04.csv",
                   "../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_10_04.csv",
                   "../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/other_locations/marawi_tweets_10_04.csv")

csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/raw/marawi_tweets_10_05.csv",
                   "../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_10_05.csv",
                   "../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/other_locations/marawi_tweets_10_05.csv")

csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/raw/marawi_tweets_10_06.csv",
                   "../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_10_06.csv",
                   "../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/other_locations/marawi_tweets_10_06.csv")

csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/raw/marawi_tweets_10_07.csv",
                   "../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_10_07.csv",
                   "../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/other_locations/marawi_tweets_10_07.csv")

csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/raw/marawi_tweets_10_08.csv",
                   "../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_10_08.csv",
                   "../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/other_locations/marawi_tweets_10_08.csv")

csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/raw/marawi_tweets_10_09.csv",
                   "../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_10_09.csv",
                   "../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/other_locations/marawi_tweets_10_09.csv")

csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/raw/marawi_tweets_10_10.csv",
                   "../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_10_10.csv",
                   "../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/other_locations/marawi_tweets_10_10.csv")

csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/raw/marawi_tweets_10_11.csv",
                   "../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_10_11.csv",
                   "../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/other_locations/marawi_tweets_10_11.csv")

csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/raw/marawi_tweets_10_12.csv",
                   "../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_10_12.csv",
                   "../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/other_locations/marawi_tweets_10_12.csv")

csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/raw/marawi_tweets_10_13.csv",
                   "../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_10_13.csv",
                   "../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/other_locations/marawi_tweets_10_13.csv")

csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/raw/marawi_tweets_10_14.csv",
                   "../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_10_14.csv",
                   "../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/other_locations/marawi_tweets_10_14.csv")

csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/raw/marawi_tweets_10_15.csv",
                   "../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_10_15.csv",
                   "../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/other_locations/marawi_tweets_10_15.csv")

csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/raw/marawi_tweets_10_16.csv",
                   "../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_10_16.csv",
                   "../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/other_locations/marawi_tweets_10_16.csv")

csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/raw/marawi_tweets_10_17.csv",
                   "../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_10_17.csv",
                   "../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/other_locations/marawi_tweets_10_17.csv")

csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/raw/marawi_tweets_10_18.csv",
                   "../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_10_18.csv",
                   "../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/other_locations/marawi_tweets_10_18.csv")

csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/raw/marawi_tweets_10_19.csv",
                   "../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_10_19.csv",
                   "../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/other_locations/marawi_tweets_10_19.csv")

csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/raw/marawi_tweets_10_20.csv",
                   "../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_10_20.csv",
                   "../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/other_locations/marawi_tweets_10_20.csv")

csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/raw/marawi_tweets_10_21.csv",
                   "../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_10_21.csv",
                   "../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/other_locations/marawi_tweets_10_21.csv")

csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/raw/marawi_tweets_10_22.csv",
                   "../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_10_22.csv",
                   "../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/other_locations/marawi_tweets_10_22.csv")

csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/raw/marawi_tweets_10_23.csv",
                   "../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_10_23.csv",
                   "../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/other_locations/marawi_tweets_10_23.csv")
csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/raw/marawi_tweets_10_24.csv",
                   "../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_10_24.csv",
                   "../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/other_locations/marawi_tweets_10_24.csv")

csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/raw/marawi_tweets_10_25.csv",
                   "../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_10_25.csv",
                   "../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/other_locations/marawi_tweets_10_25.csv")

csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/raw/marawi_tweets_10_26.csv",
                   "../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_10_26.csv",
                   "../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/other_locations/marawi_tweets_10_26.csv")

csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/raw/marawi_tweets_10_27.csv",
                   "../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_10_27.csv",
                   "../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/other_locations/marawi_tweets_10_27.csv")

csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/raw/marawi_tweets_10_28.csv",
                   "../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_10_28.csv",
                   "../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/other_locations/marawi_tweets_10_28.csv")

csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/raw/marawi_tweets_10_29.csv",
                   "../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_10_29.csv",
                   "../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/other_locations/marawi_tweets_10_29.csv")

csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/raw/marawi_tweets_10_30.csv",
                   "../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_10_30.csv",
                   "../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/other_locations/marawi_tweets_10_30.csv")

csv_read_and_write("../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/raw/marawi_tweets_10_31.csv",
                   "../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/philippines_tweets/marawi_tweets_10_31.csv",
                   "../marawi_tweets_with_location/marawi_tweets_october/official/prayformarawi_tweets/other_locations/marawi_tweets_10_31.csv")
