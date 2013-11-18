""" Script to extract species names from tree & stick into taxa abundance database """
# Import modules
from Bio import Phylo
import urllib2
import string
import getpass
import psycopg2

#Get species names from files, put into web query, get pruned tree.


