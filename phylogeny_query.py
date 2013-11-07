""" Script to extract species names from tree & stick into taxa abundance database """
# Import modules
import dendropy

""" Set up database parameters and insert data into respective databases """
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

# Set up ability to query bird key data
con= psycopg2.connect(host= "localhost", database="bbs", user="postgres", password= passwd)
cur = con.cursor()


# Create database for mammal key data 
cur.execute("DROP TABLE IF EXISTS bird_phylogeny")
con.commit()

cur.execute("CREATE TABLE bbs.bird_phylogeny(family varchar, genus varchar, species varchar, species_code varchar);")
con.commit()

# Insert data into mammal key table
cur.executemany("INSERT INTO bbs.bird_phylogeny (family, genus, species, species_code) VALUES(%s,%s,%s,%s)", bird_key_data)
con.commit()

# Close communication with the database
cur.close()
con.close()
