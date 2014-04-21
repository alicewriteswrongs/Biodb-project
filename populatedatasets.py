#!/usr/bin/python

###This is a quick script to insert data into the dataset table
###necessary to have data in this table to insert minicircle data
###(datasetid foreign key is not_null in minicircle table)

###add datasets

import MySQLdb

##Database connection stuff
def connect_db(dbase):
    """
    connected to the database dbase, user and password is hardcoded (for now)
    """
    #make a connection object
    connection = MySQLdb.connect (host="localhost", db=dbase, user="benpote", passwd="password") #highly secure password
    #get a cursor object from that
    cursor = connection.cursor()
    return cursor, connection

def close_db(cursor, connection):
    """
    close db connection
    """
    cursor.close()
    connection.close()

def run_query(cursor, query):
    """
    Pass it a cursor object and a text mysql query and get results!
    """
    cursor.execute(query)
    rows = cursor.fetchall()
    return rows



#currently just adds two datasets, pretty easy to add more
#(delete records in the table, and more to the dictionary below, rerun script)
datasets = {1:'genbank dataset',2:'pacbio dataset',3:'hong-simpson dataset'}

def add_datasets(cursor,connection):
    for i in datasets:
        query = """
        INSERT INTO dataset(did,description) VALUES ('%d', '%s');
        """ % (i,datasets[i])
        cursor.execute(query)
    connection.commit()

###run it!

#a couple times this has worked properly in ipython, but not
#when calling it from the commandline - ??

cursor, connection = connect_db('msad')
add_datasets(cursor,connection)
close_db(cursor, connection)
