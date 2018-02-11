# coding=utf-8
import csv
import urllib
from bs4 import BeautifulSoup
import re
from geopy.geocoders import Nominatim
geolocator = Nominatim()
from geopy.exc import GeocoderTimedOut
URL_INIT = 'https://twitter.com/'

file_to_read = "read.csv"
file_to_write = "write.csv"
list_of_found_userlocations = []
list_of_nonfound_userlocations = []

#--------------------------------------------------------------------------------------------------
def csv_read_and_write(read_path, write_path):
    with open(write_path ,'w') as outFile:
        fileWriter = csv.writer(outFile)
        with open(read_path,'r') as inFile:
            fileReader = csv.DictReader(inFile, delimiter=';')
            for row in fileReader:
                username = row["username"]
                print("username = " + username)
                location = findLocation(username)
                if location is None:
                    data = [row["username"],
                            row["date"],
                            row["retweets"],
                            row["favorites"],
                            row["text"],
                            row["geo"],
                            row["mentions"],
                            row["hashtags"],
                            row["id"],
                            row["permalink"]]
                else:
                    data = [row["username"],
                            row["date"],
                            row["retweets"],
                            row["favorites"],
                            row["text"],
                            location,
                            row["mentions"],
                            row["hashtags"],
                            row["id"],
                            row["permalink"]]
                fileWriter.writerow(data)

#----------------------------------------------------------------------
def parse_url(tweet_user):
    url = URL_INIT+ tweet_user.strip('@')
    return url


def findLocation(user):
    try:
        url = parse_url(user)
        print("\turl is + " + url)
        response = urllib.urlopen(url)
    except:
        print("error in opening the url")
        return
    html = response.read()
    soup = BeautifulSoup(html, "lxml")
    location = soup.find('span','ProfileHeaderCard-locationText').text.encode('utf8').strip('\n').strip()
    if location:
        print("\tlocation is found = " + location)
        if ',' in location:
            splitted_location = location.split(',')
        else:
            splitted_location = re.split('|;|-|/|°|#', location)
        try:
            print(splitted_location)
            if splitted_location:
                located_location = geolocator.geocode(splitted_location[0], timeout=100)
            else:
                located_location = geolocator.geocode(location, timeout=100)
            if located_location:
                # user_plus_location = (user, located_location)
                # list_of_found_userlocations.append(user_plus_location)
                return located_location
            else:
                # user_plus_incorrect_location = (user, location)
                # list_of_nonfound_userlocations.append(user_plus_incorrect_location)
                return
        except GeocoderTimedOut as e:
            print("Error: geocode failed on input %s with message %s"%(location, e))
#--------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    # # data = ["username;date;retweets;favorites;text;geo;mentions;hashtags;id;permalink",
    # #        "",
    # #         "Jules,Dicki,Lake Nickolasville".split(","),
    # #         "Dedric,Medhurst,Stiedemannberg".split(",")
    # #         ]
    # # path = file_to_write
    # # csv_writer(data, path)
    # with open("read.csv") as f_obj:
    #     csv_dict_reader(f_obj)
    csv_read_and_write(file_to_read, file_to_write)