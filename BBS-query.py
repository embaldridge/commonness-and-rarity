"""Script to extract data for chapter 1 from databases"""
# Import modules
import csv
import string
import psycopg2
import getpass

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
con_string = "host='localhost' dbname='bbs' user='postgres' password=" + key
con = psycopg2.connect(con_string)
cur = con.cursor()

# Query to extract BBS data for analysis
# (BBS_tablename.statenum * 1000 + BBS_tablename.route) creates a unique identifier for the BBS routes.
# BBS_species.id_to_species = 1 selects for records that have been identified to species- excludes uncertain ID records.
# Countrynum = 840 selects for United States records.
# RPID = 101 selects for standard routes.
sql_query = cur.execute("""SELECT 
    (weather.statenum * 10000000 + weather.route * 10000 + weather.year) AS RouteIDYear,
    (counts.statenum * 1000 + counts.route) AS RouteID, 
    species.sporder AS SpOrder,
    species.family AS Family,
    species.genus AS Genus, 
    species.species AS Species, 
    routes.lati AS latitude, 
    routes.loni AS longitude, 
    counts.Aou AS AOU, 
    counts.SpeciesTotal AS Abundance 
FROM 
    bbs.counts,
    bbs.species,
    bbs.routes,
    bbs.weather
WHERE
    counts.Aou = species.AOU AND
    (counts.statenum * 1000 + counts.route) = (routes.statenum * 1000 + routes.route) AND
    (counts.statenum * 10000000 + counts.route * 10000 + counts.year) = (weather.statenum * 10000000 + weather.route * 10000 + weather.year) AND
    counts.countrynum = 840 AND 
    counts.RPID = 101 AND 
    species.sporder = 'Passeriformes' AND 
    counts.YEAR = 2005;""")

BBS_data = cur.fetchall()

# Set up output parameters

BBS_header = (['Route_ID','Genus','Species','AOU','Abundance'])
BBS_filename = 'BBS_extracted.csv'


# Call data output function
output_data(BBS_filename, BBS_header, BBS_data)         
