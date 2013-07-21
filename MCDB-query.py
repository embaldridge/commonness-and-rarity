"""Script to extract data for chapter 1 from databases"""
# Import modules
import csv
import string
import psycopg2

# Write outputs to .csv file 
def output_data(filename, header, data):
    output_file = open(filename, "wb")
    datawriter = csv.writer(output_file)
    datawriter.writerow(header)
    datawriter.writerows(data)
    output_file.close()
    return filename

""" Set up database capabilities """
# Set up ability to query data
con = psycopg2.connect(database='mcdb', user='postgres')
cur = con.cursor()

# Query will go here

mcdb_data = cur.fetchall()

# Set up output parameters

mcdb_header = (['Latitude', 'Longitude','Genus','Species','Abundance'])
mcdb_filename = 'MCDB_extracted.csv'


# Call data output function
output_data(mcdb_filename, mcdb_header, mcdb_data)         
