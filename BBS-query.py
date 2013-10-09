"""Script to extract data for chapter 1 from databases"""
# Import modules
import csv
import sqlite3 as dbapi
import string

#Write outputs to .csv file 
def output_data(filename, header, data):
    output_file = open(filename, "wb")
    datawriter = csv.writer(output_file)
    datawriter.writerow(header)
    datawriter.writerows(data)
    output_file.close()
    return filename

""" Set up database capabilities """
# Set up ability to query data
con = dbapi.connect('data/bbsdb.sqlite')
cur = con.cursor()

# Switch con data type to string
con.text_factory = str

# Query to extract BBS data for analysis
# (BBS_tablename.statenum * 1000 + BBS_tablename.route) creates a unique identifier for the BBS routes.
# BBS_species.id_to_species = 1 selects for records that have been identified to species- excludes uncertain ID records.
# Countrynum = 840 selects for United States records.
# RPID = 101 selects for standard routes.
sql_query = cur.execute("""SELECT (BBS_weather.statenum * 10000000 + BBS_weather.route * 10000 + BBS_weather.year) AS RouteYear, (BBS_counts.statenum * 1000 + BBS_counts.route) AS RouteID, BBS_species.sporder AS SpOrder, BBS_species.genus AS Genus, BBS_species.species AS Species, BBS_routes.lati AS latitude, BBS_routes.loni AS longitude, BBS_counts.Aou AS AOU, BBS_counts.SpeciesTotal AS Abundance FROM BBS_counts
    JOIN BBS_species 
    ON BBS_counts.Aou == BBS_species.AOU
    JOIN BBS_routes
    ON (BBS_counts.statenum * 1000 + BBS_counts.route) == (BBS_routes.statenum * 1000 + BBS_routes.route)
    JOIN BBS_weather
    ON (BBS_counts.statenum * 10000000 + BBS_counts.route * 10000 + BBS_counts.year) == (BBS_weather.statenum * 10000000 + BBS_weather.route * 10000 + BBS_weather.year)
    WHERE BBS_counts.countrynum == "840" AND BBS_counts.RPID == "101" AND BBS_species.sporder == "Passeriformes" AND BBS_counts.YEAR == "2005";""")

BBS_data = cur.fetchall()

# Set up output parameters

BBS_header = (['Route_ID','Genus','Species','AOU','Abundance'])
BBS_filename = 'BBS_extracted.csv'


# Call data output function
output_data(BBS_filename, BBS_header, BBS_data)         