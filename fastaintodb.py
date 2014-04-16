#a quick script to parse a FASTA file and then insert it into a mysqlDB
#starting with the CSBs, because they seem like the easiest thing to start with
#this script assumes that the data is located in biodb_project/data (where it is on my laptop)
#######

import MySQLdb

#the below is just copied from yozen code
def connect_db(dbase):
    #make a connection object
    connection = MySQLdb.connect (host="localhost", db=dbase, user="benpote", passwd="password") #highly secure password
    #get a cursor object from that
    cursor = connection.cursor()
    return cursor, connection

def close_db(cursor, connection):
    cursor.close()
    connection.close()

def run_query(cursor, query):
    cursor.execute(query)
    rows = cursor.fetchall()
    return rows

#we want to actually connect to our database
cursor, connection = connect_db('msad')

#a really boring example query
query = """
SHOW TABLES;
"""
#get the results!
results = run_query(cursor, query)
#print to see if it works
print results
#close the connection to our database 
close_db(cursor, connection)
