"""Script to extract data for chapter 1 from databases"""
# Import modules
import csv
import string
import psycopg2
import getpass

#Import data from a .csv file
def import_data(filename):
    datafile = open(filename, 'r')
    datareader = csv.reader(datafile, delimiter=',')
    
    data = []
    
    for row in datareader:
        data.append(row)

    return data

#Write outputs to .csv file 
def output_data(filename, header, data):
    output_file = open(filename, "wb")
    datawriter = csv.writer(output_file)
    datawriter.writerow(header)
    datawriter.writerows(data)
    output_file.close()
    return filename

""" Get password for postgresql"""
key = getpass.getpass()


""" Set up database capabilities """
# Set up ability to query data
con= psycopg2.connect(host= "localhost", database="bbs", user="postgres", password= key)
cur = con.cursor()

# Query to extract BBS data for analysis
# (BBS_tablename.statenum * 1000 + BBS_tablename.route) creates a unique identifier for the BBS routes.
# Countrynum = 840 selects for United States records.
# RPID = 101 selects for standard routes.
sql_query = cur.execute("""SELECT 
    routes.lati AS latitude, 
    routes.loni AS longitude,
    species.family AS Family,
    species.genus AS Genus, 
    species.species AS Species,
    BirdMapKey.species_code AS Filecode,
    counts.SpeciesTotal AS Abundance 
FROM 
    bbs.counts,
    bbs.species,
    bbs.routes,
    bbs.weather,
    bbs.BirdMapKey
WHERE
    counts.Aou = species.AOU AND
    (counts.statenum * 1000 + counts.route) = (routes.statenum * 1000 + routes.route) AND
    (counts.statenum * 10000000 + counts.route * 10000 + counts.year) = (weather.statenum * 10000000 + weather.route * 10000 + weather.year) AND
    (BirdMapKey.genus || BirdMapKey.species) = (species.genus || species.species) AND
    counts.countrynum = 840 AND 
    counts.RPID = 101 AND 
    species.sporder = 'Passeriformes' AND 
    counts.YEAR = 2005;""")

BBS_data = cur.fetchall()

cur.close

# Set up import for map keys

bird_key_file = 'bird_maps_key.csv'

# Import map key data
birds_with_maps = import_data(bird_key_file)

# Check to make sure each BBS species has a map; append name code to file

# Set up output parameters

BBS_header = (['Latitude', 'Longitude','Family','Genus','Species', 'Filecode','Abundance'])
BBS_filename = 'BBS_extracted.csv'


# Call data output function
output_data(BBS_filename, BBS_header, BBS_data)         
