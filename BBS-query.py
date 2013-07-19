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
sql_query = cur.execute("""SELECT (BBS_counts.statenum * 1000 + BBS_counts.route) AS RouteID, BBS_species.genus AS Genus, BBS_species.species AS Species, BBS_routes.lati AS latitude, BBS_routes.loni AS longitude, BBS_counts.Aou AS AOU, BBS_counts.SpeciesTotal AS Abundance FROM BBS_counts
    JOIN BBS_species 
    ON BBS_counts.Aou == BBS_species.AOU
    JOIN BBS_routes
    ON BBS_counts.route == BBS_routes.route
    WHERE BBS_counts.countrynum == "840" AND BBS_counts.RPID == "101" AND BBS_species.id_to_species == "1" AND BBS_counts.YEAR == "2005";""")

BBS_data = cur.fetchall()

# Set up output parameters

BBS_header = (['Route_ID','Genus','Species','AOU','Abundance'])
BBS_filename = 'BBS_extracted.csv'


# Call data output function
output_data(BBS_filename, BBS_header, BBS_data)         
