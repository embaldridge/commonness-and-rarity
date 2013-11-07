""" Extracts species names from .dbf files and associated with filename."""

# Import modules
import csv
import glob
import string
from dbfpy import dbf
import psycopg2
import getpass



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
        # Extract species code
        path = filename.split("/") # Splits path name by /
        file_ext = path[-1] # Obtains filename without path
        species_code = file_ext.split("_pl.dbf") # Separates species code from shapefile type (pl) and file extension.
        
        # Extract metadata from file
        db = dbf.Dbf(filename) # Open dbf file into variable db
        record = db[0] # Get record from the first record in the database
        
        # Associate metadata with species code
        key = key + [[record[3]] + string.split(record[1]) + [species_code[0]]] # key = family + genus + species + species code
        
        db.close()
    return key


# Get list of .dbf files in map directory
mammal_files = glob.glob('data/Mammals_3.0/*/*_pl.dbf')
bird_files = glob.glob('data/Passeriformes/*/*_pl.dbf')

# Call map key function
mammal_key_data = make_key(mammal_files)
bird_key_data = make_key(bird_files)


""" Set up database parameters and insert data into respective databases """
# Get password for postgresql
password = getpass.getpass()

# Set up ability to query mammal key data
con_string = "host='localhost' dbname= 'mcdb' user='postgres' password=" + password
con = psycopg2.connect(con_string)
cur = con.cursor()

# Create table for mammal key data 
cur.execute("DROP TABLE IF EXISTS MammalMapKey")
con.commit()

cur.execute("CREATE TABLE MammalMapKey(family varchar, genus varchar, species varchar, species_code varchar);")

# Insert data into mammal key table
cur.executemany("INSERT INTO MammalMapKey(family, genus, species, species_code) VALUES(%s,%s,%s,%s)", mammal_key_data)

# Make the changes to the database persistent
con.commit()

# Close communication with the database
cur.close()
con.close()

# Set up ability to query bird key data
con_string = "host='localhost' dbname= 'bbs' user='postgres' password=" + password
con = psycopg2.connect(con_string)
cur = con.cursor()

# Create database for mammal key data 
cur.execute("DROP TABLE IF EXISTS BirdMapKey")
con.commit()

cur.execute("CREATE TABLE BirdMapKey(family varchar, genus varchar, species varchar, species_code varchar);")

# Insert data into mammal key table
cur.executemany("INSERT INTO BirdMapKey(family, genus, species, species_code) VALUES(%s,%s,%s,%s)", bird_key_data)
con.commit()

# Make the changes to the database persistent
con.commit()

# Close communication with the database
cur.close()
con.close()


# Set up output parameters
key_header = (['Family', 'Genus','Species', 'Species code'])
mammal_key_filename = 'mammal_maps_key.csv'
bird_key_filename = 'bird_maps_key.csv'


# Call data output function
output_data(mammal_key_filename, key_header, mammal_key_data)
output_data(bird_key_filename, key_header, bird_key_data)  