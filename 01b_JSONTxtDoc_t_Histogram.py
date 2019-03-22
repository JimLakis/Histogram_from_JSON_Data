# Python v3.6
# March, 2019

#import urllib.request
import json
#import time
import pandas as pd
#import sys
#import numpy as np
import matplotlib.pyplot as plt


def produce_histogram(magnitude_per_code_dataframe):
    """ Produce a histogram from the magnitude per code dataframe """
    ax = magnitude_per_code_dataframe.plot.hist(bins=36, alpha=1)
    ax.set_xlabel('magnitude')
    plt.show()

def extract_magnitude_per_code(dictionary_obj):
    """ Extracts the number of quakes reported in the dictionary report then loop over report extracting magnitude of quakes per id code"""
    def total_quakes(dictionary_obj):
        """ Extracts the number of quakes reported """
        if 'count' in dictionary_obj['metadata']:
            number_of_quakes = dictionary_obj['metadata']['count']
        return number_of_quakes
    
    def extract_mags(number_of_quakes, dictionary_obj):
        """ Loops over the report to extract the magnitude per quake for each record and stores all key/value pairs in a dictionary """
        magnitude_per_code_dictionary = {}
        for i in range(number_of_quakes):
            k = dictionary_obj['features'][i]['id']
            v = dictionary_obj['features'][i]['properties']['mag']
            magnitude_per_code_dictionary[str(k)] = float(v)
        return magnitude_per_code_dictionary
    
    def convert_to_dataframe(magnitude_per_code_dictionary):
        """ Convert the magnitude per code dictionary to a Pandas dataframe """
        magnitude_per_code_dataframe = pd.DataFrame.from_dict(magnitude_per_code_dictionary, orient='index')
        return magnitude_per_code_dataframe

    number_of_quakes = total_quakes(dictionary_obj)
    magnitude_per_code_dictionary = extract_mags(number_of_quakes, dictionary_obj)
    del dictionary_obj
    magnitude_per_code_dataframe = convert_to_dataframe(magnitude_per_code_dictionary)
    return magnitude_per_code_dataframe

def file_to_dictionary():
        """ Opening a text doc formtted as JSON and loading the contents into a dictionary """
        with open('JSON_data.txt') as file_obj:
            dictionary_obj = json.load(file_obj)
        file_obj.close()
        return dictionary_obj


def main():
    dictionary_obj = file_to_dictionary()
    magnitude_per_code_dataframe = extract_magnitude_per_code(dictionary_obj)
    produce_histogram(magnitude_per_code_dataframe)

    
    
if __name__ == "__main__":
    main()