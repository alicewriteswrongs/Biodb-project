#!/usr/bin/python

#a quick script to parse a FASTA file and then insert it into a mysqlDB
#starting with the CSBs, because they seem like the easiest thing to start with
#this script assumes that the data is located in biodb_project/data (where it is on my laptop)
#######

#########HEADER#########

import MySQLdb

#########FUNCTIONS#########

####DATABASE CONNECTION####

#the below is just copied from yozen code
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

####FASTA PARSING####

def read_file(file):
    """
    Just reads in a file at the location it is passed
    """
    with open (file, "r") as myfile:
        data = myfile.read()
    return data

##functions for dealing with our various datafiles (parsing them into lists)##

#csb functions#
def format_csb(data):
    """
    Inserts our CSB files into the CSB table, expects a long string
    (normal result of calling read_file on csb.fasta)
    Returns a nicely formatted list which we can iterate through with a query function
    """
    data = data.replace('>','') #remove the > character from fasta headers
    data = data.split('\n')  #split string into list based on newline character
    data.pop()   #remove '' (last item in list)
    return data

#minicircle functions
def format_minicircle(data):
    """
    Takes the contents of a minicircle file and returns a list of identifiers and sequences
    (in order [id,sequence,id,sequence,....])
    This function is appropriate for the small one (genbank dataset)
    """
    seqout = []
    datasplit = data.split('>')
    datasplit.pop(0)
    for i in datasplit:
        split = i.split('\n')
        header = split[0]
        split.pop(0)
        seq = ''
        for i in split:
            seq += i
        seqout.append(header)
        seqout.append(seq)
    return seqout

def format_insert_minicircle(filein,cursor,connection,datasetid):
    """
    takes a file containing minicircle data and reads it in one line at a time
    this is necessary for the larger files (pacbio, hongsimpson)
    """
    header = ''
    seq = ''
    with open(filein) as file:
        for line in enumerate(file):
            count, txt = line
            if count % 2 == 0:
                if header == '':
                    header = txt
                else:
                    query = """
                    INSERT INTO minicircles(datasetid,sequence,description) VALUES ('%d','%s','%s');
                    """ % (datasetid,seq,header)
                    cursor.execute(query)
                    header = txt
            else:
                seq = txt
    connection.commit()
                    
def format_insert_smRNA(filein):
    """
    Takes a filepath for the smRNA file, inserts the data into the smRNA table.
    Need to do this line-by-line, using same algorithm as for big minicircles, but
    need to parse header to get copy number out.
    """
    copynumber = 0
    idnum = 0
    seq = ''
    with open(filein) as seqfile:
        for line in enumerate(seqfile):
            count, txt = line
            if count % 2 == 0:
                if idnum == '':
                    copynumber = int(txt.split('-')[1])
                    idnum = int(txt.split('-')[0].replace('>',''))
                else:
                    query = """
                    INSERT INTO smallrna(smid, sequence, copynum) VALUES ('%s','%s','%d');
                    """ % (idnum, seq, copynumber)
                    cursor.execute(query)
                    idnum = int(txt.split('-')[0].replace('>',''))
                    copynumber = int(txt.split('-')[1])
            else:
                seq = txt
    connection.commit()



        
        















def format_smRNA(data):
    """
    Takes the contents of the smallRNA fasta file and returns a list of id, seq, and 
    copy number (in order [id, copynum, seq, id, copynum, seq....])
    """
    seqout = []
    data = data.replace('>','') #remove the > character from fasta headers
    datasplit = data.split('\n')
    print datasplit
    j = 0
    for item in datasplit:
	if j in range(0,len(datasplit),2):
		split = item.split('-')
		id = split[0]
		copynum = split[1] 
		seqout.append(id)
		seqout.append(copynum)
		j +=1
	else:
		seqout.append(item)
		j +=1
    return seqout


####INSERTING RECORDS####

def insert_csb(fasta,cursor,connection):
    """
    takes a formatted fasta list (from format_csb) and a cursor, and executes queries to
    insert the data in the list into the database connection specified by the cursor
    """
    i = 0
    while i < len(fasta):
       query = """
       INSERT INTO csb(csbid,sequence) VALUES ('%s', '%s');
       """ % (fasta[i], fasta[i+1])
       cursor.execute(query)
       i += 2
    connection.commit()
    #note: need commit on any 'update' or 'insert' type of query (where a table is changed)

def insert_minicirc(fasta,cursor,connection,datasetid):
    """
    Takes a formatted list (from format_minicircle) and a cursor, and executes queries to
    insert the data in the list into the database connection specified by the cursor
    Needs arguments: fasta, cursor, connection, datasetid
    Also recall that this is only usable for smaller datasets
    """
    i = 0
    while i < len(fasta):
        query = """
        INSERT INTO minicircles(datasetid,sequence,description) VALUES ('%d','%s','%s');
        """ % (datasetid,fasta[i+1],fasta[i]) #fasta[i+1] is sequence
        cursor.execute(query)                 #fasta[i] is the desc. header
        i += 2
    connection.commit()
    
 

########END FUNCTIONS#########


########MAIN#########

#We can write scripts below here to add each of our types of data to the database
#Just comment out the ones you don't need (if, for instance, a table is already 
#correctly populated).

##BIOED SCRIPT
#if you uncomment everything here and run it on bioed it should insert everything

#CSB
#we'll start with the CSBs (easiest!)

cursor, connection = connect_db('msad')

#read in the file
filein = "/var/www/data/msad/csb_sequences/csb.fasta"
csb_data = read_file(filein)

#format and insert
csb_formatted = format_csb(csb_data)
insert_csb(csb_formatted,cursor,connection)

#csbs should be good now, next is:
#minicircles!

#first the easy ones (genbank)

filein = "/var/www/data/msad/minicircles_sequences/genbank_minicircles.fasta"
minicirc_data = read_file(filein)
minicirc_format = format_minicircle(minicirc_data)
insert_minicirc(minicirc_format,cursor,connection,1)

#now the more difficult ones (computationally speaking)

#pacbio
filein = "/var/www/data/msad/minicircles_sequences/pacbio_minicircles_filtered_maxiremoved.fasta"
format_insert_minicircles(filein,cursor,connection,2)

#hong-simpson
filein = "/var/www/data/msad/minicircles_sequences/HongSimpson.fasta"
format_insert_minicircles(filein,cursor,connection,3) 

#good on the minicircles, now we need to handle the smRNAs
#(similar to large file minicircle method)

