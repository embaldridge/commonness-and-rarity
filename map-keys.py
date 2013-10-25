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
    for filename in filenames:
        path = filename.split("/") # Splits path name by /
        file_ext = path[-1] # Obtains filename without path
        species_code = file_ext.split("_pl.dbf") # Separates species code from shapefile type (pl) and file extension.
        db = dbf.Dbf(filename) # Open dbf file into variable db
        record = db[0] # Get record from the first record in the database
        key = key + [[record[3]] + string.split(record[1]) + [species_code[0]]] # key = family + genus + species + species code
        db.close()
    return key

# Get list of .dbf files in map directory
mammal_files = glob.glob('data/Mammals_3.0/*/*_pl.dbf')
bird_files = glob.glob('data/Passeriformes/*/*_pl.dbf')

# Set up output parameters
key_header = (['Family', 'Genus','Species', 'Species code'])
mammal_key_filename = 'mammal_maps_key.csv'
bird_key_filename = 'bird_maps_key.csv'

# Call map key function
mammal_key_data = make_key(mammal_files)
bird_key_data = make_key(bird_files)

# Call data output function
output_data(mammal_key_filename, key_header, mammal_key_data)
output_data(bird_key_filename, key_header, bird_key_data)  