#script to just insert the Hong-simpson reads


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


def read_file(file):
    """
    Just reads in a file at the location it is passed
    """
    with open (file, "r") as myfile:
        data = myfile.read()
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
    

cursor, connection = connect_db('msad')
filein = "/var/www/data/msad/minicircles_sequences/HongSimpson.fasta"
hongsimpsondata = readfile(filein)
hongformatted = format_minicircle(hongsimpsondata)
insert_minicirc(hongformatted)
