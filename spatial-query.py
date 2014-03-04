""" Takes geographic ranges for each species, determines what ranges could potentially occur there."""  

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

# Query to extract viable BBS routes for analysis
# (BBS_tablename.statenum * 1000 + BBS_tablename.route) creates a unique identifier for the BBS routes.
# Countrynum = 840 selects for United States records.
# RPID = 101 selects for standard routes.
sql_query = cur.execute("""SELECT 
    routes.lati AS latitude, 
    routes.loni AS longitude    
FROM 
    bbs.routes,
    bbs.weather
WHERE
    (routes.statenum * 1000 + routes.route) = (weather.statenum * 1000 + weather.route) AND
    weather.countrynum = 840 AND weather.rpid = 101 AND weather.year = 2005;""")

BBS_potential_routes = cur.fetchall()

cur.close


""" Set up database capabilities """
# Set up ability to query data
con= psycopg2.connect(host= "localhost", database="mcdb", user="postgres", password= key)
cur = con.cursor()

# MCDB potential sites query.
sql_query = cur.execute("""SELECT 
  sites.latitude, 
  sites.lonitude  
FROM 
  mcdb.sites;""")

mcdb_potential_sites = cur.fetchall()    

cur.close

