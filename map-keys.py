""" Extracts species names from .dbf files and associated with filename."""

# Import modules
import csv
import string

# Write outputs to .csv file 
def output_data(filename, header, data):
    output_file = open(filename, "wb")
    datawriter = csv.writer(output_file)
    datawriter.writerow(header)
    datawriter.writerows(data)
    output_file.close()
    return filename

# Set up output parameters
key_header = (['Family', 'Genus','Species', 'Filename'])
mammal_key_filename = 'mammal_maps_key.csv'
bird_key_filename = 'bird_maps_key.csv'


# Call data output function
output_data(mammal_key_filename, key_header, mammal_key_data)

output_data(bird_key_filename, key_header, bird_key_data)  