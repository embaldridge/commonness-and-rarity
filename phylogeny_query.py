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

# Query BBS data.
base_url= 'http://phylocommons.org/query/prune=True&format=newick
BBS_query_url&taxa='
mammal_tree_name= '&tree=bininda-emonds_mammals'

= 'http://phylocommons.org/query/prune=True&format=newick&taxa=Homo+sapiens%2CGorilla+gorilla%2CPan+paniscus%2CPan+troglodytes&tree=bininda-emonds_mammals'
 
result = urllib2.urlopen(my_query_url)
tree = result.read()

output_data(tree)





