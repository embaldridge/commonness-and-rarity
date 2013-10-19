"""Script to extract data for chapter 1 from databases"""
# Import modules
import csv
import string
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

""" Get password for postgresql"""
key = getpass.getpass()


""" Set up database capabilities """
# Set up ability to query data
con_string = "host='localhost' dbname='mcdb' user='postgres' password=" + key
print(con_string)
con = psycopg2.connect(con_string)
cur = con.cursor()

# Query will go here

mcdb_data = cur.fetchall()

# Set up output parameters

mcdb_header = (['Latitude', 'Longitude','Genus','Species','Abundance'])
mcdb_filename = 'MCDB_extracted.csv'


# Call data output function
output_data(mcdb_filename, mcdb_header, mcdb_data)         
