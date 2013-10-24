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

# Read dbf and write family, genus, species into file
def make_key(filenames):
    key = []
    for files in filenames:
        db = dbf.Dbf(files)
        print(db[0])
        rec = db[0]
        key = key + rec
        return key

# Get list of .dbf files in map directory
mammal_files = glob.glob('data/Mammals_3.0/*/*.dbf')
bird_files = glob.glob('data/Passeriformes/*/*.dbf')

# Set up output parameters
key_header = (['Family', 'Genus','Species', 'Filename'])
mammal_key_filename = 'mammal_maps_key.csv'
bird_key_filename = 'bird_maps_key.csv'

# Call map key function
mammal_key_data = make_key(mammal_files)
print(mammal_key_data)
bird_key_data = make_key(bird_files)

# Call data output function
#output_data(mammal_key_filename, key_header, mammal_key_data)
#output_data(bird_key_filename, key_header, bird_key_data)  