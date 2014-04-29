#Biological Databases final project

contains the files for our biological databases final project

Currently:

* fastaintodb.py - inserts our data into the appropriate tables
* maketables.sql - SQL commands to make the tables we want in our database
* populatedatasets.py - inserts the records for the 'dataset' table
* hongsimposon.py - inserst just the hong-simpson sequences
* droptables.sql - drops the tables in the right order (foreign key constraints)
* proposal
    * proposal.tex
    * proposal.pdf
    * ERdiagram.pdf
    * ERdiagram-crop.pdf
    * ERdiagram.dia
* test.txt - some hints about using git

##Jalview

* jalview is what we're using to embed alignments into our 'display' page
* have it working in a basic sense (can display a test fasta alignment)
* it wants us to package our data in a .zip

##Using fastaintodb.py:

The script is broken up into several sections. This script should be run (on bioed) after:

* Running maketables.sql and verifying table structure
* Running populatedatasets.py

And that should be it! Note that fastaintodb.py Just gets in the sequence data - it doesn't
insert any of our alignment data. As of now it can get all of our sequence data into our table
structure. The smallRNA dataset is very large, however, so on my (Ben's) laptop I've only 
tested a small subset (first 10000 lines).

It appears that the script works! Still need to do some confirmation on bioed.

###Hong-Simpson problems

Original version of fastaintodb.py script didn't insert the Hong-Simpson.fasta correctly.
Updated script so now it does, also wrote an additional script (hongsimpson.py) which inserts
them on their own.

####Definitions:

This holds definitions for all of the functions we need

####MAIN

This has commands and function calls written out to insert the various kinds of data.

Make sure to comment out ones you don't need! 
