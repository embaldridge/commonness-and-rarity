""" Extracts species names from .dbf files and associated with filename."""

# Import modules
import csv
import glob
import os
import string
from dbfpy import dbf

# Write outputs to .csv file 
def output_data(filename, header, data):
    output_file = open(filename, "wb")
    datawriter = csv.writer(output_file)
    datawriter.writerow(header)
    datawriter.writerows(data)
    output_file.close()
    return filename

# Get list of .dbf files in map directory
def file_list(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            if files.endswith(".dbf"):
                print os.path.join(root, filename)
                return map_list


#Set up file directory parameters
mammals_folder = '/data/Mammals_3.0'
birds_folder = '/data/Passeriformes'


# Set up output parameters
key_header = (['Family', 'Genus','Species', 'Filename'])
mammal_key_filename = 'mammal_maps_key.csv'
bird_key_filename = 'bird_maps_key.csv'


# Read dbf and write family, genus, species into file
def make_key(filename):
    db = dbf.Dbf(filename)
    rec = string.split(db[2])
    return key

# Call file list function
mammal_file_list = file_list(mammals_folder)
bird_file_list = file_list(birds_folder)

# Call data output function
output_data(mammal_key_filename, key_header, mammal_key_data)

output_data(bird_key_filename, key_header, bird_key_data)  