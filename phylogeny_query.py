""" Script to extract species names from tree & stick into taxa abundance database """
# Import modules
from Bio import Phylo
import urllib2
import string
import getpass
import psycopg2

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

#Get species names from files, put into web query, get pruned tree.
BBS_filename = 'BBS_extracted.csv'
mcdb_filename = 'MCDB_extracted.csv'

BBS_data = import_data(BBS_filename)
mcdb_data = import_data(mcdb_filename)



