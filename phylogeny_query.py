""" Script to extract species names from tree & stick into taxa abundance database """
# Import modules
from Bio import Phylo
import urllib2
import csv
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

# Extract species names from files, put into string.
def PhyloCommons_species_list(species_list_file, tree_name):
    species_list_webified = ['http://phylocommons.org/query/prune=True&format=newick&taxa=']
    species_list = import_data(species_list_file)
    for record in species_list:
        #Get genus, species
        species_list_webified = species_list_webified + [[record[3]] + ['+'] + [[record[4]] + ['%2C']]] 
        
    species_list_webified = species_list_webified + [tree_name]                                             
    return species_list_webified    

#Get species names from files, put into web query, get pruned tree.
BBS_filename = 'BBS_extracted.csv'
mcdb_filename = 'MCDB_extracted.csv'

mammal_tree_name = '&tree=bininda-emonds_mammals'
bird_tree_name = '&tree=jetz_birds'

# Get URLs.
BBS_URL = PhyloCommons_species_list(BBS_filename, bird_tree_name)
MCDB_URL = PhyloCommons_species_list(mcdb_filename, mammal_tree_name)

BBS_tree_result = urllib2.urlopen(BBS_URL)
BBS_tree = BBS_tree_result.read()

mcdb_tree_result = urllib2.urlopen(MCDB_URL)
mcdb_tree = mcdb_tree_result.read()


output_data(BBS_tree)
output_data(mcdb_tree)




