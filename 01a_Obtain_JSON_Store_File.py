# Python v3.6
# March, 2019

import urllib.request
#import json
#import time
#import pandas as pd


def save_json_file(json_obj):
        """ Writes the JSON feed data to a text file """
        with open('JSON_data.txt', 'w+') as file_obj:
            file_obj.write(json_obj)
        file_obj.close()

def get_json(url):
    """ Opening an HTTP connection to the desired site, retreiving the JSON information and returning the JSON object. """
    def open_connection(url):
        """ Opening an HTTP connection to the desired site and returning an HTTP object. """
        http_response_obj = urllib.request.urlopen(url)
        return http_response_obj
    
    def acquire_json(http_response_obj):
        """ Reading in the JSON information and returning a JSON object. """
        json_obj = http_response_obj.read().decode("utf-8")
        return json_obj
    
    http_response_obj = open_connection(url)
    json_obj = acquire_json(http_response_obj)
    
    return json_obj


def main():
    url_str = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_month.geojson"
    
    json_obj = get_json(url_str)
    save_json_file(json_obj)
    print('Done')
  
            
if __name__ == "__main__":
    main()