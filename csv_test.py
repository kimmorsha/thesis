# -*- coding: utf-8 -*-

import csv
import urllib
from bs4 import BeautifulSoup
import re
from geopy.geocoders import Nominatim
geolocator = Nominatim()
from geopy.exc import GeocoderTimedOut
URL_INIT = 'https://twitter.com/'

file_read = "../tweets_csv/marawi_tweets_may/marawi_tweets_05_23_to_10_24.csv"
file_write = "../tweets_csv/marawi_tweets_may/tweets_05_23_to_05_24.csv"
#----------------------------------------------------------------------------------------------------------
def csv_dict_reader(file_obj):
    """
    Read a CSV file using csv.DictReader
    """
    reader = csv.DictReader(file_obj, delimiter=';')
    for line in reader:
        
#---------------------------------------------------------------------------------------------------------
def parse_url(tweet_user):
    url = URL_INIT+ tweet_user.strip('@')
    return url


def findLocation(user):
    try:
        url = parse_url(user)
        print("url is + " + url)
        response = urllib.urlopen(url)
    except:
        print("error in opening the url")
        # continue
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
                #write it in 
            else:
                located_location = geolocator.geocode(location, timeout=100)
            if located_location:
                user_plus_location = (user, located_location)
                list_of_found_userlocations.append(user_plus_location)
            else:
                user_plus_incorrect_location = (user, location)
                list_of_nonfound_userlocations.append(user_plus_incorrect_location)
        except GeocoderTimedOut as e:
            print("Error: geocode failed on input %s with message %s"%(location, e))

#--------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    with open("../tweets_csv/marawi_tweets_may/marawi_tweets_05_23_to_10_24.csv") as f_obj:
        csv_dict_reader(f_obj)