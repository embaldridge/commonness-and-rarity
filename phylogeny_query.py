""" Script to extract species names from tree & stick into taxa abundance database """
# Import modules
from Bio import Phylo
import string
import getpass
import psycopg2

#Get species names from phylogenetic tree.
def get_species_names(filepath):
    trees = Phylo.parse(filepath, "newick")  #Opens tree 
    names = []
    for tree in trees:
        tips = tree.get_terminals()

        for tip in tips:
            print tip
            names = names + [tip]
    
    return names

# Set up parameters for getting the name data
bird_tree_file = "data/AllBirdsHackett1.tre"
mammal_tree_file = "data/mammal-supertree.tre"


# Bird data extraction and putting into database

# Call function to get bird names
bird_key_data = get_species_names(bird_tree_file)

# Set up ability to query bird key data
con= psycopg2.connect(host= "localhost", database="bbs", user="postgres", password= passwd)
cur = con.cursor()


# Create database for bird key data 
cur.execute("DROP TABLE IF EXISTS bird_phylogeny")
con.commit()

cur.execute("CREATE TABLE bbs.bird_phylogeny(family varchar, genus varchar, species varchar, species_code varchar);")
con.commit()

# Insert data into bird key table
cur.executemany("INSERT INTO bbs.bird_phylogeny (family, genus, species, species_code) VALUES(%s,%s,%s,%s)", bird_key_data)
con.commit()

# Close communication with the database
cur.close()
con.close()




# Mammal data extraction and insertion into database

# Call function to get mammal data
mammal_key_data = get_species_names(mammal_tree_file)

# Get password for postgresql
passwd = getpass.getpass()

# Set up ability to query mammal key data
con= psycopg2.connect(host= "localhost", database="mcdb", user="postgres", password= passwd)
cur = con.cursor()

# Create table for mammal key data 
cur.execute("DROP TABLE IF EXISTS mammal_phylogeny")
con.commit()

cur.execute("CREATE TABLE mcdb.mammal_phylogeny(family varchar, genus varchar, species varchar, species_code varchar);")
con.commit()

# Insert data into mammal key table
cur.executemany("INSERT INTO mcdb.mammal_phylogeny(family, genus, species, species_code) VALUES(%s,%s,%s,%s)", mammal_key_data)
con.commit()

# Close communication with the database
cur.close()
con.close()


